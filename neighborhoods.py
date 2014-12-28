# neighborhoods.py
# GPLv3+ licensed by Nick Doiron
# open a neighborhoods GeoJSON file and return the neighborhood of the given location

import json
from shapely.geometry import shape, Point

f = open("nyc-neighborhoods.geojson", "r")
neighborhoods = json.loads(f.read())["features"]
f.close()

def get_name(neighborhood):
  # adapt to your own dataset
  return neighborhood["properties"]["neighborhood"]

def find_neighborhood(location_data):
  # do point-in-polygon on neighborhoods GeoJSON
  lat = float(location_data["lat"])
  lng = float(location_data["lng"])
  pt = Point(lng, lat)

  for neighborhood in neighborhoods:
    polygon = shape(neighborhood["geometry"])
    if polygon.contains(pt):
      return get_name(neighborhood)
  return "unknown"
