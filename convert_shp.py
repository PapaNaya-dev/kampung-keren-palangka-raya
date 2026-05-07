import shapefile
import json
import os

sf = shapefile.Reader(r'D:\project_eric\kampung-keren-palangka-raya\data_kawasan')
fields = [f[0] for f in sf.fields[1:]]

features = []
for sr in sf.shapeRecords():
    props = {}
    for i, fname in enumerate(fields):
        val = sr.record[i]
        if val is None:
            props[fname] = None
        elif isinstance(val, (int, float)):
            props[fname] = val
        else:
            props[fname] = str(val).strip() if str(val).strip() else None
    
    geom = sr.shape.__geo_interface__
    features.append({
        'type': 'Feature',
        'properties': props,
        'geometry': geom
    })

geojson = {
    'type': 'FeatureCollection',
    'name': 'Kawasan_Kampung_Keren',
    'crs': {'type': 'name', 'properties': {'name': 'urn:ogc:def:crs:OGC:1.3:CRS84'}},
    'features': features
}

os.makedirs(r'D:\project_eric\kampung-keren-palangka-raya\data', exist_ok=True)

with open(r'D:\project_eric\kampung-keren-palangka-raya\data\kawasan.geojson', 'w', encoding='utf-8') as f:
    json.dump(geojson, f, ensure_ascii=False, indent=2)

print('GeoJSON created with', len(features), 'features')
for feat in features:
    p = feat['properties']
    print(f"  {p['Kawasan']} - {p['Kelurahan']} ({p['Kecamatan']})")
