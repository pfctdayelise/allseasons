import seasons
import pytest
from datetime import datetime


def test_astronomical_dates():
    result = seasons.astronomical_dates(2017)
    expected = {'dec': datetime(2017, 12, 21, 16, 27, 48, 281359),
                'june': datetime(2017, 6, 21, 4, 24, 17, 882888),
                'sept': datetime(2017, 9, 22, 20, 1, 41, 290341),
                'march': datetime(2017, 3, 20, 10, 28, 37, 516239)}
    assert result == expected


def test_between_two_values():
    dates = seasons.astronomical_dates(2017)
    july = datetime(2017, 7, 3, 1, 1, 1)
    assert seasons.between(july, 'march', 'sept')
    assert seasons.between(july, 'march', 'dec')
    assert seasons.between(july, 'june', 'sept')
    assert seasons.between(july, 'june', 'dec')
    assert seasons.between(july, 'march', None)
    assert seasons.between(july, 'june', None)
    assert seasons.between(july, None, 'sept')
    assert seasons.between(july, None, 'dec')
    assert not seasons.between(july, 'march', 'june')
    assert not seasons.between(july, 'sept', 'dec')
    assert not seasons.between(july, None, 'march')
    assert not seasons.between(july, None, 'june')
    assert not seasons.between(july, 'sept', None)
    assert not seasons.between(july, 'dec', None)


class TestSeason:

    def test_valid_for_southern_meteo_3_july(self):
        date = datetime(1983, 7, 3, 1, 1, 1)
        result = {(s.name, s.valid_for(date))
                   for s in seasons.southern_meteo.seasons}
        expected = {('spring', False),
                    ('summer', False),
                    ('autumn', False),
                    ('winter', True)
        }
        assert result == expected


class TestSeasons:

    @pytest.mark.parametrize(('seasonset', 'expected'), [
        (seasons.northern_meteo, 'summer'),
        (seasons.northern_astro, 'summer'),
        (seasons.southern_meteo, 'winter'),
        (seasons.southern_astro, 'winter'),
    ])
    def test_get_season_3_july(self, seasonset, expected):
        date = datetime(1983, 7, 3, 1, 1, 1)
        assert seasonset.get_season(date) == expected

    @pytest.mark.parametrize(('seasonset', 'expected'), [
        (seasons.northern_meteo, 'spring'),
        (seasons.northern_astro, 'winter'),
        (seasons.southern_meteo, 'autumn'),
        (seasons.southern_astro, 'summer'),
    ])
    def test_get_season_20_march(self, seasonset, expected):
        """This date falls between the astronomical and meteorological seasons
        """
        date = datetime(2017, 3,20, 1, 1, 1)
        assert seasonset.get_season(date) == expected


class TestLocation:

    @pytest.mark.parametrize(('lat', 'lng', 'expected'), [
        (51.507351, -0.127758, 'northern'),  # London
        (68.958524, 33.08266, 'northern'),  # Murmansk
        (-34.603684, -58.381559, 'southern'),  # Buenos Aires
        (-37.813628, 144.963058, 'southern'),  # Melbourne
        (0.0, -109.20, 'southern'),  #Pontianak
    ])
    def test_hemisphere(self, lat, lng, expected):
        loc = seasons.Location(lat, lng)
        assert loc.hemisphere == expected
