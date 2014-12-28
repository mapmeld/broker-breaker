# airbnb.py
# GPLv3+ licensed by Nick Doiron
# scan Airbnb for relevant sublets in New York City area
# screen-scraper, so probably going to break continually
# probably against ToS, oops

import urllib2, json

def get_listings(grid):
  south = grid[0]
  west = grid[1]
  north = grid[2]
  east = grid[3]

  listings = []

  jdata = urllib2.urlopen('https://www.airbnb.com/search/search_results?page=1&location=Bedford-Stuyvesant%2C+Brooklyn%2C+NY%2C+United+States&checkin=01%2F01%2F2015&checkout=02%2F01%2F2015&price_min=1000&price_max=1365').read()
  results = json.loads(jdata)["results"].lower().replace('  ', ' ').split('col-sm-12')

  for rental in results:
    # places must have reviews
    if (rental.find('reviews') == -1) or (rental.find(' 0 reviews') > -1):
      print("rejected rental without reviews")
      continue

    listing = {}

    # extract URL
    url = 'https://www.airbnb.com' + rental[rental.find('data-url') + 10 : ]
    url = url[ : url.find('"') ]
    listing["url"] = url
    print(url)

    # check URL of listing for disqualifiers
    scrape = urllib2.urlopen(url).read().lower().replace('  ', ' ')
    disqualifiers = ['women only', 'hipster']
    disqualified = False
    for disqualifier in disqualifiers:
      if scrape.find(disqualifier.lower()) > -1:
        print('found disqualifying phrase')
        disqualified = True
        break
    if disqualified:
      continue

    listing["location_data"] = {}
    lat = rental[rental.find('data-lat') + 10 : rental.find('data-lng') ]
    lat = lat[ : lat.find('"') ]
    lng = rental[rental.find('data-lng') + 10 : ]
    lng = lng[ : lng.find('"') ]
    listing["location_data"]["lat"] = float(lat)
    listing["location_data"]["lng"] = float(lng)

    # Airbnb rentals begin when I want them to begin
    listing["start"] = None

    listings.append(listing)

  return listings
