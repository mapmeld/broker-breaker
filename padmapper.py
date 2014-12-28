# padmapper.py
# GPLv3+ licensed by Nick Doiron
# scan PadMapper for relevant sublets in New York City area
# screen-scraper, so probably going to break continually
# probably against ToS, oops

from dateutil.parser import parse
import json, urllib2

def get_listings(grid):
  south = str(grid[0])
  west = str(grid[1])
  north = str(grid[2])
  east = str(grid[3])

  listings = []

  jdata = urllib2.urlopen('http://www.padmapper.com/reloadMarkersJSON.php?eastLong=' + east + '&northLat=' + north + '&westLong=' + west + '&southLat=' + south + '&cities=false&showPOI=false&limit=3150&minRent=1000&maxRent=1350&searchTerms=&maxPricePerBedroom=6000&minBR=0&maxBR=1&minBA=1&maxAge=7&imagesOnly=true&phoneReq=false&cats=false&dogs=false&noFee=false&showSubs=true&showNonSubs=true&showRooms=false&showVac=false&userId=-1&cl=true&pl=true&aptsrch=true&rnt=true&airbnb=true&ood=true&af=true&rltr=true&zoom=15&favsOnly=false&onlyHQ=true&showHidden=false&am=false&workplaceLat=0&workplaceLong=0&maxTime=0').read()
  markers = json.loads(jdata)

  for marker in markers:
    true_url = 'https://www.padmapper.com/show.php?id=' + marker["id"]
    scrape = urllib2.urlopen(true_url).read().lower()
    if scrape.find('http://www.padlister.com/listings/') > -1:
      true_url = scrape[ scrape.find('http://www.padlister.com/listings/') : ]
      true_url = true_url[ 0 : true_url.find('"') ]
      scrape = urllib2.urlopen(true_url).read()
    elif scrape.find('meta http-equiv="refresh"') > -1:
      true_url = scrape[ scrape.find('url=') + 4 : scrape.rfind('"') ]
      scrape = urllib2.urlopen(true_url).read()
    scrape = scrape.lower().replace('  ', ' ')
    print(scrape)

    # disqualifiers
    disqualifiers = ['12 months', 'women only', 'hipster']
    disqualified = False
    for disqualifier in disqualifiers:
      if scrape.find(disqualifier.lower()) > -1:
        print('found disqualified')
        disqualified = True
        break
    if disqualified:
      continue

    listing = {}
    listing["location_data"] = {}
    listing["location_data"]["lat"] = float(marker["lat"])
    listing["location_data"]["lng"] = float(marker["lng"])

    listing["url"] = true_url

    if scrape.find('date="20') > -1:
      get_date = scrape[scrape.find('date="20') + 6 : ]
      get_date = get_date[ : get_date.find('"') ]
      listing["start"] = parse(get_date)
    elif scrape.find('<h5>available</h5>') > -1:
      get_date = scrape[scrape.find('<h5>available</h5>') + 18 : ]
      get_date = get_date[ : get_date.find("</li>") ]
      listing["start"] = parse(get_date)
    else:
      listing["start"] = None

    listings.append(listing)

  return listings
