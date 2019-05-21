#!/usr/bin/env python3
import click
from collections import OrderedDict
import json
from pathlib import Path


@click.command()
@click.option('-f', '--file', 'filepath',
              required=True,
              help='Converts e-mission .json dump file to .geojson')
def convert(filepath):
    emission_data = None
    with open(filepath, 'r') as emission_f:
        emission_data = json.loads(emission_f.read())


    geojson_data = {
        'type': 'FeatureCollection',
        'features': []
    }
    point_cols = ['accuracy', 'altitude', 'bearing', 'elapsedRealtimeNanos',
                  'filter', 'fmt_time', 'latitude', 'longitude', 'sensed_speed', 'ts']
    for coordinate in emission_data:
        data = coordinate['data']
        if 'latitude' in data and 'longitude' in data:
            point = {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [data['longitude'], data['latitude']]
                },
                'properties': {}
            }
            for col in point_cols:
                point['properties'][col] = data[col]
            geojson_data['features'].append(point)


    path = Path(filepath).resolve()
    out_fn = '{parent}/{fn}.geojson'.format(parent=path.parent, fn=path.stem)
    with open(out_fn, 'w') as geojson_f:
        geojson_f.write(json.dumps(geojson_data))


if __name__ == '__main__':
    convert()
