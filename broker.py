# broker.py
# GPLv3+ licensed by Nick Doiron
# scan Airbnb and PadMapper for relevant sublets in New York City area
# screen-scraper, so probably going to break continually
# probably against ToS for both websites, oops

from datetime import datetime
import urllib2, json

import airbnb, padmapper, neighborhoods

the_good_ones = []

def get_commute_time(location_data):
  # call Google Directions API with transit
  # return value in minutes
  my_url = 'https://maps.googleapis.com/maps/api/directions/json?mode=transit&departure_time=1419862179&origin=' + str(location_data["lat"]) + "," + str(location_data["lng"]) + '&destination=25%20W%2053rd%20St,%20NYC&api_key=AIzaSyBekR41_LoUo5X_FCijNZgQDgdyVofNIB0'
  jdata = urllib2.urlopen(my_url).read()
  response = json.loads(jdata)
  try:
    return int(response["routes"][0]["legs"][0]["duration"]["value"] / 60)
  except:
    print(jdata)
    return 0

def __main__():
  # get start date from user? Currently Jan 01, 2015
  start_date = '01/01/2015'

  # parse start date
  month_day = start_date.split('/')
  start_date = datetime(int(month_day[2]), int(month_day[0]), int(month_day[1]))

  # define previously-visited neighborhoods
  old_neighborhoods = []

  # define search areas (currently one neighborhood)
  south = 40.68696
  west = -73.96839
  north = 40.70161
  east = -73.94267

  passes = [
    [south, west, north, east],
    # [south2, west2, north2, east2]
  ]

  for p in passes:
    listings = []

    # search Airbnb.com/sublet for one month
    # filter by price of $1,000 - $1,350
    # do all high-zoom passes to get the most results
    airbnb_listings = airbnb.get_listings(p, start_date)
    print("Read " + str(len(airbnb_listings)) + " listings on Airbnb")
    listings += airbnb_listings

    # search PadMapper for sublets
    # filter by price of $1,000 - $1,350
    # do all high-zoom passes to get the most results
    padmapper_listings = padmapper.get_listings(p)
    print("Read " + str(len(padmapper_listings)) + " listings on PadMapper")
    listings += padmapper_listings

    # filter all listings into just the good ones
    for listing in listings:
      location_data = listing["location_data"]

      # get start date - compare to user start date
      # could add some flexibility
      if (listing["start"] is not None) and (start_date > listing["start"]):
        print("eliminated a rental that opened too early")
        continue

      # get neighborhood name from GeoJSON
      neighborhood = neighborhoods.find_neighborhood(location_data)

      # don't recycle neighborhoods
      if neighborhood in old_neighborhoods:
        print("eliminated a rental in one of your old neighborhoods")
        continue

      # get commute time of successful listings
      commute_time = get_commute_time(location_data)

      # if everything still looks good, add it to the good ones
      if (commute_time < 60):
        good_listing = {}
        good_listing["url"] = listing["url"]
        good_listing["start"] = listing["start"]
        good_listing["neighborhood"] = neighborhood
        good_listing["commute"] = commute_time
        # good_listing["latlng"] = [location_data["lat"], location_data["lng"]]
        the_good_ones.append(good_listing)

  # do some sorting on the_good_ones ?

  # output the listings
  print(the_good_ones)

__main__()
