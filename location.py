from ratelimit import NomatimRateLimitCache
from libs.external_services import get_address_from_latlng

location_cache = NomatimRateLimitCache(get_address_from_latlng)


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



    
