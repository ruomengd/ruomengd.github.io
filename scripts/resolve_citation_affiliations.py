"""Resolve full affiliations with ROR; ambiguous matches remain unpublished."""
import csv
import json
import time
from threading import Lock
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests


def resolve(rows, work):
    cache_path = work / 'ror-matches.json'
    cache = json.loads(cache_path.read_text()) if cache_path.exists() else {}
    affiliations = sorted({row[3] for row in rows if row[3]})

    request_lock = Lock()

    def lookup(affiliation):
        for attempt in range(4):
            with request_lock:
                time.sleep(0.25)  # At most four new requests per second.
            try:
                response = requests.get('https://api.ror.org/v2/organizations',
                                        params={'affiliation': affiliation}, timeout=45)
            except requests.RequestException:
                if attempt == 3:
                    raise
                time.sleep(2 * (attempt + 1))
                continue
            if response.status_code == 429 or response.status_code >= 500:
                time.sleep(10 * (attempt + 1))
                continue
            response.raise_for_status()
            chosen = [item['organization'] for item in response.json()['items'] if item.get('chosen')]
            result = None
            if len(chosen) == 1:
                org = chosen[0]
                # Multi-location organizations cannot safely be assigned one city.
                if len(org.get('locations', [])) == 1:
                    place = org['locations'][0]['geonames_details']
                    result = dict(affiliation=next(n['value'] for n in org['names'] if 'ror_display' in n['types']),
                                  latitude=place['lat'], longitude=place['lng'],
                                  city=place['name'], country=place['country_name'], ror_id=org['id'])
            return affiliation, result
        raise RuntimeError('ROR unavailable; rerun to resume cached matches.')

    pending = [a for a in affiliations if a not in cache]
    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = [pool.submit(lookup, affiliation) for affiliation in pending]
        for index, future in enumerate(as_completed(futures), 1):
            affiliation, result = future.result()
            cache[affiliation] = result
            cache_path.write_text(json.dumps(cache, ensure_ascii=False, indent=2))
            if index % 50 == 0:
                print('ROR:', index, '/', len(pending), flush=True)
    located, unresolved = [], set()
    for author, citing, cited, affiliation in rows:
        match = cache.get(affiliation)
        if match:
            located.append(dict(match, **{'citing author name': author, 'citing paper title': citing,
                                         'cited paper title': cited, 'raw affiliation': affiliation}))
        else:
            unresolved.add(affiliation)
    (work / 'unresolved-affiliations.json').write_text(json.dumps(sorted(unresolved), ensure_ascii=False, indent=2))
    if located:
        with (work / 'citations.csv').open('w', newline='') as stream:
            writer = csv.DictWriter(stream, fieldnames=list(located[0]))
            writer.writeheader()
            writer.writerows(located)
    return located
