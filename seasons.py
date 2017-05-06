#!/usr/bin/env python

import ephem


class Location:
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng

    @property
    def hemisphere(self):
        if self.lat > 0:
            return "northern"
        return "southern"


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


class Seasons:
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
        return 'Seasons({})'.format(self.name)

    def get_season(self, date):
        for season in self.seasons:
            if season.valid_for(date):
                return season.name


def astronomical_dates(year):
    y = str(year)
    march = ephem.next_spring_equinox(y).datetime()
    june = ephem.next_summer_solstice(y).datetime()
    sept = ephem.next_autumn_equinox(y).datetime()
    dec = ephem.next_winter_solstice(y).datetime()
    return dict(march=march, june=june, sept=sept, dec=dec)


def between(date, first_date, second_date):
    eqxs = astronomical_dates(date.year)
    c1 = eqxs[first_date] <= date if first_date else True
    c2 = date < eqxs[second_date] if second_date else True
    return c1 and c2


northern_meteo = Seasons('meteorological', [
    Season('spring', lambda d: 3 <= d.month < 6),
    Season('summer', lambda d: 6 <= d.month < 9),
    Season('autumn', lambda d: 9 <= d.month < 12),
    Season('winter', lambda d: d.month == 12 or d.month < 3)],
    lambda loc: loc.hemisphere == 'northern')

southern_meteo = Seasons('meteorological', [
    Season('spring', lambda d: 9 <= d.month < 12),
    Season('summer', lambda d: d.month == 12 or d.month < 3),
    Season('autumn', lambda d: 3 <= d.month < 6),
    Season('winter', lambda d: 6 <= d.month < 9)],
    lambda loc: loc.hemisphere == 'southern')

northern_astro = Seasons('astronomical', [
    Season('spring', lambda d: between(d, 'march', 'june')),
    Season('summer', lambda d: between(d, 'june', 'sept')),
    Season('autumn', lambda d: between(d, 'sept', 'dec')),
    Season('winter',
           lambda d: between(d, None, 'march') or between(d, 'dec', None))],
    lambda loc: loc.hemisphere == 'northern')
    
southern_astro = Seasons('astronomical', [
    Season('spring', lambda d: between(d, 'sept', 'dec')),
    Season('summer',
           lambda d: between(d, None, 'march') or between(d, 'dec', None)),
    Season('autumn', lambda d: between(d, 'march', 'june')),
    Season('winter', lambda d: between(d, 'june', 'sept'))],
    lambda loc: loc.hemisphere == 'southern')


season_sets = (
    northern_meteo,
    southern_meteo,
    northern_astro,
    southern_astro,
    )
