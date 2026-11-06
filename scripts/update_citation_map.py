"""Generate the homepage citation map. Install: pip install citation-map==6.7.

Run from any directory; caches and the review CSV stay in ignored tmp/.
Use --from-csv to regenerate after manually reviewing/correcting the CSV.
Google Scholar may require you to complete a CAPTCHA in the opened Chrome window.
"""
import argparse
import csv
import json
import math
from datetime import datetime
from zoneinfo import ZoneInfo
from pathlib import Path
from citation_map.citation_map import find_all_citing_authors, find_all_citing_affiliations

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / 'tmp' / 'citation-map'
OUTPUT = ROOT / 'assets' / 'maps' / 'citations.html'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--from-csv', action='store_true')
    parser.add_argument('--workers', type=int, default=8, help='Concurrent affiliation lookups (CitationMap default: 8)')
    args = parser.parse_args()
    if not 1 <= args.workers <= 8:
        parser.error('--workers must be between 1 and 8')
    WORK.mkdir(parents=True, exist_ok=True)
    csv_path = WORK / 'citations.csv'
    if not args.from_csv:
        raw_path = WORK / 'raw-affiliations.json'
        if raw_path.exists():
            rows = json.loads(raw_path.read_text())
        else:
            authors = find_all_citing_authors('aPlu2rYAAAAJ')
            rows = find_all_citing_affiliations(authors, num_processes=args.workers)
            raw_path.write_text(json.dumps(rows, ensure_ascii=False))
        from resolve_citation_affiliations import resolve
        if not resolve(rows, WORK):
            raise RuntimeError('No confirmed institutions; keeping the previous map unchanged.')
    def has_location(row):
        try:
            lat, lon = float(row['latitude']), float(row['longitude'])
            return math.isfinite(lat) and math.isfinite(lon) and -90 <= lat <= 90 and -180 <= lon <= 180
        except (KeyError, ValueError, TypeError):
            return False

    with csv_path.open() as stream:
        located = [row for row in csv.DictReader(stream) if has_location(row)]
    if not located:
        raise RuntimeError('No located citations; keeping the previous map unchanged.')
    from render_citation_map import render_map
    html, institution_count = render_map(located)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(html)
    metadata = {
        'updated': datetime.now(ZoneInfo('America/New_York')).strftime('%Y-%m-%d'),
        'scholar_id': 'aPlu2rYAAAAJ',
        'located_records': len(located),
        'institutions': institution_count,
        'source': 'Google Scholar via CitationMap 6.7; institution coordinates via ROR',
    }
    (ROOT / '_data' / 'citation_map.json').write_text(json.dumps(metadata, indent=2) + '\n')
    print('Saved', OUTPUT, 'with', len(located), 'located citation-author records.')


if __name__ == '__main__':
    main()
