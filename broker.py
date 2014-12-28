# broker.py
# scan Airbnb and PadMapper for relevant sublets in New York City area
# screen-scraper, so probably going to break continually
# probably against ToS for both websites, oops

from datetime import datetime

the_good_ones = []

def get_commute_time(latlng):
  # call Google Directions API with transit
  return 0

def get_neighborhood(latlng):
  # do point-in-polygon on neighborhoods GeoJSON
  return "Bushwick"

def read_airbnb_location():
  # filter out airbnbs without reviews

  return [lat, lng]

def read_padmapper_location():
  return [lat, lng]

def read_sublet(source, body, url):
  # search for filtering keywords

  # get location from listings
  if source == "Airbnb":
    location_data = read_airbnb_location()
  elif source == "PadMapper":
    location_data = read_padmapper_location()

  # get neighborhood name from GeoJSON
  neighborhood = get_neighborhood(location_data)

  # get commute time of successful listings
  commute_time = get_commute_time(location_data)

  # if everything still looks good, add it to the good ones
  the_good_ones << { url: url, neighborhood: neighborhood, commute: commute_time, latlng: location_data }

def __main__():
  # get start date from user
  start_date = input('When are you moving in? MM/DD')

  # parse start date
  month_day = start_date.split('/')
  start_date = datetime(2014, int(month_day[0]), int(month_day[1]))

  # make search grid (currently four areas with more reasonable prices)
  passes = [
    [lat1, lng1],
    [lat2, lng2],
    [lat3, lng3],
    [lat4, lng4]
  ]

  # search Airbnb.com/sublet for one month
  # filter by price of $1,000 - $1,350
  # do all high-zoom passes to get the most results
  for p in passes:
    # get listings from search
    for listing in listings:
      read_sublet("Airbnb", body, url)

  # search PadMapper for sublets
  # filter by price of $1,000 - $1,350
  # do all high-zoom passes to get the most results
  for p in passes:
    # get listings from search
    for listing in listings:
      read_sublet("PadMapper", body, url)

  # do some sorting on the_good_ones ?

  # output the listings
  print(the_good_ones)
