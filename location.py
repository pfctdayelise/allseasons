from functools import partial
import geocoder
from ratelimit import NomatimRateLimitCache

location_cache = NomatimRateLimitCache(partial(geocoder.osm, method='reverse'))


class Location:
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng

    @property
    def hemisphere(self):
        if self.lat > 0:
            return "northern"
        return "southern"

    @property
    def country(self):
        g = location_cache(self.lat, self.lng)
        translations = {
            'РФ': 'Russian Federation',
        }
        return translations.get(g.country, g.country)


