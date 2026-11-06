"""Render CitationMap CSV records in the same quiet blue style as the visitor map."""
from collections import defaultdict
from html import escape
from importlib.resources import files
import json

import folium


def popup_text(value):
    # Folium interpolates HTML in JavaScript template literals.
    return escape(value).replace('`', '&#96;').replace('$', '&#36;').replace('\\', '&#92;')


def render_map(rows):
    chart = folium.Map(
        location=[0, 0], zoom_start=0, tiles=None, crs='EPSG4326',
        min_zoom=-3, zoom_snap=0, scroll_wheel_zoom=False,
        world_copy_jump=False, max_bounds=True,
    )
    countries = json.loads(files('citation_map').joinpath('world_countries.geojson').read_text())
    folium.GeoJson(countries, style_function=lambda _: {
        'fillColor': '#c3cfdd', 'color': '#ffffff', 'weight': 0.3, 'fillOpacity': 1,
    }, attribution='<a href="https://www.naturalearthdata.com/">Natural Earth</a> · <a href="https://ror.org/">ROR</a> · <a href="https://github.com/ChenLiu-1996/CitationMap">CitationMap</a>').add_to(chart)
    institutions = defaultdict(set)
    for row in rows:
        key = (row['affiliation'], float(row['latitude']), float(row['longitude']))
        institutions[key].add(row['citing author name'])
    for (institution, lat, lon), authors in institutions.items():
        content = '<strong>' + popup_text(institution) + '</strong><br>' + '<br>'.join(popup_text(x) for x in sorted(authors))
        folium.CircleMarker(
            [lat, lon], radius=3, color='#ffffff', weight=0.7,
            fill=True, fill_color='#4b87b9', fill_opacity=0.9,
            tooltip=popup_text(institution), popup=folium.Popup(content, max_width=320),
        ).add_to(chart)
    chart.get_root().header.add_child(folium.Element('''<style>
      .leaflet-container { background: #fff; font-family: Arial, sans-serif; }
      .leaflet-control-attribution { font-size: 9px; }
      .leaflet-popup-content { max-width: calc(100vw - 70px); max-height: 240px; overflow: auto; line-height: 1.5; }
      @media(max-width:300px) {
        .leaflet-control-zoom { display: none; }
        .leaflet-control-attribution { font-size: 7px; }
      }
    </style>'''))
    name = chart.get_name()
    html = chart.get_root().render()
    bounds = f'''<script>
      {name}.fitBounds([[-90,-180],[90,180]]);
      window.addEventListener('resize', function () {{
        {name}.invalidateSize();
        {name}.fitBounds([[-90,-180],[90,180]]);
      }});
    </script>'''
    html = html.replace('</html>', '') + bounds + '\n</html>'
    return html, len(institutions)
