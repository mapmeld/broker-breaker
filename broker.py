# broker.py
# GPLv3+ licensed by Nick Doiron
# scan Airbnb and PadMapper for relevant sublets in New York City area
# screen-scraper, so probably going to break continually
# probably against ToS for both websites, oops

from datetime import datetime

import airbnb, padmapper, neighborhoods

the_good_ones = []

def get_commute_time(latlng):
  # call Google Directions API with transit
  # return value in minutes
  return 0

def __main__():
  # get start date from user
  start_date = '01/01'

  # parse start date
  month_day = start_date.split('/')
  start_date = datetime(2015, int(month_day[0]), int(month_day[1]))

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
    listings += airbnb.get_listings(p)

    # search PadMapper for sublets
    # filter by price of $1,000 - $1,350
    # do all high-zoom passes to get the most results
    listings += padmapper.get_listings(p)

    # filter all listings into just the good ones
    for listing in listings:
      location_data = listing["location_data"]

      # get start date - compare to user start date
      # could add some flexibility
      if (listing["start"] is not None) and (start_date > listing["start"]):
        continue

      # get neighborhood name from GeoJSON
      neighborhood = neighborhoods.find_neighborhood(location_data)

      # don't recycle neighborhoods
      if neighborhood in old_neighborhoods:
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
        good_listing["latlng"] = [location_data["lat"], location_data["lng"]]
        the_good_ones.append(good_listing)

  # do some sorting on the_good_ones ?

  # output the listings
  print(the_good_ones)

__main__()
