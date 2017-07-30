import pytest
import location


@pytest.fixture
def places():
    """
    Define some lat-lng data for use in location related tests
    """
    return {'london': (51.507351, -0.127758),
            'murmansk': (68.958524, 33.08266),
            'buenos aires': (-34.603684, -58.381559),
            'melbourne': (-37.813628, 144.963058),
            'pontianak': (0.0, -109.20),
            'mumbai': (19.0760, 72.8777),
            'delhi': (28.7041, 77.1025),
            'bangalore': (12.9716, 77.5946),
            'hyderabad': (17.3850, 78.4867),
    }


class TestLocation:
    """This class is just grouping the tests together,
    to keep the structure parallel with the source class.
    """

    def test_country_uk(self, places):
        lat, lng = places['london']
        loc = location.Location(lat, lng)
        assert loc.country == 'UK'

    def test_country_russia(self, places):
        lat, lng = places['murmansk']
        loc = location.Location(lat, lng)
        assert loc.country == 'Russian Federation'

    def test_country_argentina(self, places):
        lat, lng = places['buenos aires']
        loc = location.Location(lat, lng)
        assert loc.country == 'Argentina'

    def test_country_australia(self, places):
        lat, lng = places['melbourne']
        loc = location.Location(lat, lng)
        assert loc.country == 'Australia'

    @pytest.mark.xfail()
    def test_country_indonesia(self, places):
        lat, lng = 'pontianak'
        loc = location.Location(lat, lng)
        assert loc.country == 'Indonesia'

    @pytest.mark.parametrize(('placename', 'expected'), [
        ('london', 'northern'),
        ('murmansk', 'northern'),
        ('buenos aires', 'southern'),
        ('melbourne', 'southern'),
        ('pontianak', 'southern'),
    ])
    def test_hemisphere(self, places, placename, expected):
        lat, lng = places[placename]
        loc = location.Location(lat, lng)
        assert loc.hemisphere == expected
