
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


## Neighborhood data

The NYC neighborhoods GeoJSON is from PediaCities: metadata and downloads available at
http://catalog.opendata.city/dataset/pediacities-nyc-neighborhoods

## License

GPL v3+
