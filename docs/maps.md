# Homepage maps

The sidebar (desktop) and footer (mobile) share one map card with Visitors and
Citations tabs. The original whos.amung.us site ID is unchanged. The visitor
tracker is initialized once; switching tabs does not create another visit tracker.
The citation iframe loads on first selection.

## Refresh citation data

Use Python with Chrome installed:

```sh
python3 -m venv .venv-citation-map
.venv-citation-map/bin/pip install -r scripts/citation-map-requirements.txt
.venv-citation-map/bin/python scripts/update_citation_map.py
```

Keep the Chrome window open and complete Google Scholar verification when prompted.
The script uses CitationMap 6.7 and the profile `aPlu2rYAAAAJ`. The default is the
upstream limit of 8 concurrent affiliation lookups; `--workers 2` reduces it.

Raw affiliation snapshots, ROR match caches and the review CSV are under
`tmp/citation-map/`, excluded from Git and Jekyll. Rerunning reuses `raw-affiliations.json` and cached ROR matches. To fetch fresh
Scholar data, remove `raw-affiliations.json` first. To regenerate after correcting the CSV, use `--from-csv`.

Only a successful result with located citation records replaces
`assets/maps/citations.html` and `_data/citation_map.json`. Before pushing, review
location matches in `tmp/citation-map/citations.csv`. Full affiliation strings are
resolved with the [ROR affiliation API](https://ror.readme.io/docs/api-affiliation).
Only an explicit `chosen` result with one institutional location is included;
unmatched or multi-location results are listed in `unresolved-affiliations.json`.
Matches remain approximate and may identify a parent institution. Multiple
affiliations in one profile may yield only one institution. Authors without linked Scholar profiles or resolvable
locations will be missing. Affiliations are current profile affiliations, not
necessarily affiliations at the time of citation.

The generated map uses embedded Natural Earth boundaries and Folium's CDN assets.
`render_citation_map.py` applies the same 2:1 world view, white background, muted
blue land, and blue dots as the visitor widget. CitationMap supplies citation/author data and ROR supplies institution coordinates; this local renderer supplies the shared visual style.
The card credits [CitationMap](https://github.com/ChenLiu-1996/CitationMap).
An unavailable result displays a preparation message instead of fabricated pins.

## Visitor history

The existing free whos.amung.us widget remains active. Its public map shows current
and some historical visitors, not an export of the full visit history. No complete
historical export has been obtained. Do not remove the old tracking ID or claim
that existing history was migrated when changing providers.

The user chose to retain whos.amung.us. Do not introduce a replacement analytics
service or migrate history as part of the citation-map integration.
