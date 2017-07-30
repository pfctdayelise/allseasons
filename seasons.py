#!/usr/bin/env python

import ephem
import geocoder
from functools import partial
from ratelimit import NomatimRateLimitCache
from datetime import date, datetime


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


class Season:
    def __init__(self, name, valid_for_date):
        """
        @param name: a descriptive name for the season
        @param valid_for_date: a function, datetime => Boolean
        """
        self.name = name
        self.valid_for = valid_for_date

    def __str__(self):
        return 'Season({})'.format(self.name)


class Seasonset:
    def __init__(self, name, seasons, valid_for_loc):
        """
        @param name: a descriptive name for this set of seasons
        @param seasons: a list of Season objects
        @param valid_for_loc: a function, ?location => Boolean
        """
        self.name = name
        self.seasons = seasons
        self.valid_for = valid_for_loc

    def __str__(self):
        return 'Seasonset({})'.format(self.name)

    def __iter__(self):
        return iter(self.seasons)

    def get_season(self, ddate):
        for season in self:
            if season.valid_for(ddate):
                return season.name


def astronomical_dates(year):
    y = str(year)
    march = ephem.next_spring_equinox(y).datetime().date()
    june = ephem.next_summer_solstice(y).datetime().date()
    sept = ephem.next_autumn_equinox(y).datetime().date()
    dec = ephem.next_winter_solstice(y).datetime().date()
    return dict(march=march, june=june, sept=sept, dec=dec)


def between_equinoxes(ddate, first_date, second_date):
    eqxs = astronomical_dates(ddate.year)
    print('eqxs=', eqxs)
    print('type=', type(ddate))
    c1 = eqxs[first_date] <= ddate if first_date else True
    c2 = ddate < eqxs[second_date] if second_date else True
    return c1 and c2


def between_dates(ddate, start, end):
    '''
    @param date: datetime.date object
    @param start: (int, int) representing (month, day) | None
    @param end: (int, int) representing (month, day) | None
    @return: Boolean

    example: (3, 15) represents the 15th March
    '''
    c1 = date(ddate.year, *start) <= ddate if start else True
    c2 = ddate < date(ddate.year, *end) if end else True
    return c1 and c2


northern_meteo = Seasonset('n meteorological', [
    Season('spring', lambda d: 3 <= d.month < 6),
    Season('summer', lambda d: 6 <= d.month < 9),
    Season('autumn', lambda d: 9 <= d.month < 12),
    Season('winter', lambda d: d.month == 12 or d.month < 3)],
    lambda loc: loc.hemisphere == 'northern')

southern_meteo = Seasonset('s meteorological', [
    Season('spring', lambda d: 9 <= d.month < 12),
    Season('summer', lambda d: d.month == 12 or d.month < 3),
    Season('autumn', lambda d: 3 <= d.month < 6),
    Season('winter', lambda d: 6 <= d.month < 9)],
    lambda loc: loc.hemisphere == 'southern')

northern_astro = Seasonset('n astronomical', [
    Season('spring', lambda d: between_equinoxes(d, 'march', 'june')),
    Season('summer', lambda d: between_equinoxes(d, 'june', 'sept')),
    Season('autumn', lambda d: between_equinoxes(d, 'sept', 'dec')),
    Season('winter',
           lambda d: between_equinoxes(d, None, 'march') or between_equinoxes(d, 'dec', None))],
    lambda loc: loc.hemisphere == 'northern')
    
southern_astro = Seasonset('s astronomical', [
    Season('spring', lambda d: between_equinoxes(d, 'sept', 'dec')),
    Season('summer',
           lambda d: between_equinoxes(d, None, 'march') or between_equinoxes(d, 'dec', None)),
    Season('autumn', lambda d: between_equinoxes(d, 'march', 'june')),
    Season('winter', lambda d: between_equinoxes(d, 'june', 'sept'))],
    lambda loc: loc.hemisphere == 'southern')


hindu_calendar = Seasonset('Hindu calendar', [
    Season('Vasanta', lambda d: between_dates(d, (3, 15), (5, 15))),
    Season('Greeshma', lambda d: between_dates(d, (5, 15), (7, 15))),
    Season('Varsha', lambda d: between_dates(d, (7, 15), (9, 15))),
    Season('Sharad', lambda d: between_dates(d, (9, 15), (11, 15))),
    Season('Hemanta', lambda d: between_dates(d, (11, 15), None) or between_dates(d, None, (1, 15))),
    Season('Shishira', lambda d: between_dates(d, (1, 15), (3, 15))),
    ],
                           lambda loc: loc.country == 'India')


season_sets = (
    northern_meteo,
    southern_meteo,
    northern_astro,
    southern_astro,
    hindu_calendar,
    )


def get_valid_seasonsets(location):
    return [ss for ss in season_sets if ss.valid_for(location)]
