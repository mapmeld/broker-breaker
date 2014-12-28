
# Broker-Breaker

## What?

Broker-Breaker is a Python script which searches Airbnb and PadMapper for listings in New York City and
across the Hudson River in New Jersey.

It filters the listings based on particular criteria:

- available for one or two months (not longer)
- available when I need it
- in a new neighborhood (or at least a new location within a neighborhood)
- accessible to public transit
- short commutes to Midtown
- keywords (I can't rent an apartment if it's only for women; I prefer not to share a bathroom with a cat or dog (true story))

## Why?

Since July, I have been traveling across New York City, living in one neighborhood at a time. It's the only way
to see the city!

As I developed a search process, I began thinking about the most inefficient parts of my search:
- searching frequently for new and high-value listings
- scanning listing text for length of sublet, or obvious rejections
- scanning listing text for its opening time (for example: if I am booked through Nov 25, it is useless for me to see a last minute Nov 1 listing)
- entering addresses in Google Maps to estimate commute for each location
- deciding which neighborhoods to look into
- MOST inefficient: finding, comprehending, researching, and evaluating these factors visually, as a human

## Install and Run

    pip install shapely python-dateutil
    python broker.py

## Sample output

```
[{'url': u'https://www.airbnb.com/rooms/2493601?checkin=01%2f01%2f2015&amp;checkout=02%2f01%2f2015&amp;s=l_vb', 'start': None, 'latlng': [40.67816637284187, -73.94836557805525], 'commute': 38, 'neighborhood': u'Crown Heights'},
{'url': u'https://www.airbnb.com/rooms/840118?checkin=01%2f01%2f2015&amp;checkout=02%2f01%2f2015&amp;s=l_vb', 'start': None, 'latlng': [40.67994995829499, -73.9482002233025], 'commute': 36, 'neighborhood': u'Bedford-Stuyvesant'},
{'url': u'https://www.airbnb.com/rooms/2958344?checkin=01%2f01%2f2015&amp;checkout=02%2f01%2f2015&amp;s=l_vb', 'start': None, 'latlng': [40.688891190511455, -73.94462990215948], 'commute': 36, 'neighborhood': u'Bedford-Stuyvesant'},
{'url': u'https://www.airbnb.com/rooms/4000036?checkin=01%2f01%2f2015&amp;checkout=02%2f01%2f2015&amp;s=l_vb', 'start': None, 'latlng': [40.69335508209533, -73.93323840579242], 'commute': 40, 'neighborhood': u'Bedford-Stuyvesant'},
{'url': u'https://www.airbnb.com/rooms/3262303?checkin=01%2f01%2f2015&amp;checkout=02%2f01%2f2015&amp;s=l_vb', 'start': None, 'latlng': [40.6895028130298, -73.9546369416533], 'commute': 29, 'neighborhood': u'Bedford-Stuyvesant'},
{'url': u'https://www.airbnb.com/rooms/483414?checkin=01%2f01%2f2015&amp;checkout=02%2f01%2f2015&amp;s=l_vb', 'start': None, 'latlng': [40.685858491452855, -73.94837359096758], 'commute': 37, 'neighborhood': u'Bedford-Stuyvesant'},
{'url': u'https://www.airbnb.com/rooms/3401586?checkin=01%2f01%2f2015&amp;checkout=02%2f01%2f2015&amp;s=l_vb', 'start': None, 'latlng': [40.67837952112934, -73.96159161045007], 'commute': 42, 'neighborhood': u'Crown Heights'},
{'url': u'https://www.airbnb.com/rooms/1584938?checkin=01%2f01%2f2015&amp;checkout=02%2f01%2f2015&amp;s=l_vb', 'start': None, 'latlng': [40.68475713618455, -73.94107904138653], 'commute': 47, 'neighborhood': u'Bedford-Stuyvesant'},
{'url': 'http://newyork.craigslist.org/brk/sub/4820082429.html', 'start': datetime.datetime(2015, 1, 1, 0, 0), 'latlng': [40.698973, -73.944096], 'commute': 37, 'neighborhood': u'Bedford-Stuyvesant'},
{'url': 'http://newyork.craigslist.org/brk/sub/4820038063.html', 'start': datetime.datetime(2015, 12, 15, 0, 0), 'latlng': [40.691003, -73.959596], 'commute': 32, 'neighborhood': u'Bedford-Stuyvesant'},
{'url': 'http://newyork.craigslist.org/brk/sub/4820309021.html', 'start': datetime.datetime(2015, 1, 1, 0, 0), 'latlng': [40.693256, -73.959939], 'commute': 35, 'neighborhood': u'Bedford-Stuyvesant'},
{'url': 'http://newyork.craigslist.org/brk/sub/4821444046.html', 'start': datetime.datetime(2015, 1, 1, 0, 0), 'latlng': [40.690546, -73.958578], 'commute': 32, 'neighborhood': u'Bedford-Stuyvesant'},
{'url': 'http://newyork.craigslist.org/brk/sub/4817288477.html', 'start': datetime.datetime(2015, 12, 15, 0, 0), 'latlng': [40.689258, -73.957219], 'commute': 32, 'neighborhood': u'Bedford-Stuyvesant'},
{'url': 'http://newyork.craigslist.org/brk/sub/4818639138.html', 'start': datetime.datetime(2015, 2, 1, 0, 0), 'latlng': [40.696031, -73.943526], 'commute': 40, 'neighborhood': u'Bedford-Stuyvesant'},
{'url': 'http://www.padlister.com/listings/8105495.-0-bedroom-1-bathroom-apartment-at-throop-ave-brooklyn-ny-11206-in-bedford-stuyvesant', 'start': datetime.datetime(2015, 1, 1, 0, 0), 'latlng': [40.6951, -73.9431], 'commute': 32, 'neighborhood': u'Bedford-Stuyvesant'},
{'url': 'http://newyork.craigslist.org/brk/sub/4820376050.html', 'start': datetime.datetime(2015, 1, 1, 0, 0), 'latlng': [40.69302, -73.960004], 'commute': 35, 'neighborhood': u'Bedford-Stuyvesant'},
{'url': 'http://newyork.craigslist.org/brk/nfb/4817389647.html', 'start': datetime.datetime(2015, 1, 1, 0, 0), 'latlng': [40.690546, -73.958578], 'commute': 32, 'neighborhood': u'Bedford-Stuyvesant'},
{'url': 'http://newyork.craigslist.org/brk/sub/4792653235.html', 'start': datetime.datetime(2015, 1, 1, 0, 0), 'latlng': [40.694745, -73.948309], 'commute': 27, 'neighborhood': u'Bedford-Stuyvesant'},
{'url': 'http://newyork.craigslist.org/brk/roo/4817697879.html', 'start': datetime.datetime(2015, 1, 15, 0, 0), 'latlng': [40.688676, -73.951249], 'commute': 31, 'neighborhood': u'Bedford-Stuyvesant'}]
```

## Neighborhood data

The NYC neighborhoods GeoJSON is from PediaCities: metadata and downloads available at
http://catalog.opendata.city/dataset/pediacities-nyc-neighborhoods

## License

GPL v3+
