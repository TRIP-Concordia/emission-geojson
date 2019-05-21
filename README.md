emission-geojson
===============

## Usage
1. Clone this repository and download place a JSON dump in the `./data` directory
2. Install Python dependencies in virtualenv (named `convert` in examples)
   ```bash
   (convert) $ pip install -r requirements.txt
   ```
3. Convert the .json file to .geojson points data
   ```bash
   (convert) $ python convert_to_geojson.py -f data/2019-05-21.2019-05-21.timeline
   ```
