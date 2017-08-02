import pytest
from libs import location


places = {'london': (51.507351, -0.127758),
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

    @pytest.mark.europe
    @pytest.mark.external
    def test_country_uk(self):
        lat, lng = places['london']
        loc = location.Location(lat, lng)
        assert loc.country == 'UK'

    @pytest.mark.europe
    @pytest.mark.external
    def test_country_russia(self):
        lat, lng = places['murmansk']
        loc = location.Location(lat, lng)
        assert loc.country == 'Russian Federation'

    @pytest.mark.external
    def test_country_argentina(self):
        lat, lng = places['buenos aires']
        loc = location.Location(lat, lng)
        assert loc.country == 'Argentina'

    @pytest.mark.oceania
    @pytest.mark.external
    def test_country_australia(self):
        lat, lng = places['melbourne']
        loc = location.Location(lat, lng)
        assert loc.country == 'Australia'

    @pytest.mark.xfail(reason="Not sure why this fails, can you figure out why?")
    @pytest.mark.oceania
    @pytest.mark.external
    def test_country_indonesia(self):
        lat, lng = 'pontianak'
        loc = location.Location(lat, lng)
        assert loc.country == 'Indonesia'



    def test_hemisphere_melbourne(self):
        lat, lng = places['melbourne']
        loc = location.Location(lat, lng)
        assert loc.hemisphere == 'northern'



    @pytest.mark.parametrize(('placename', 'expected'), [
        ('london', 'northern'),
        ('murmansk', 'northern'),
        ('buenos aires', 'southern'),
        ('pontianak', 'southern'),
    ])
    def test_hemisphere_bulk(self, placename, expected):
        lat, lng = places[placename]
        loc = location.Location(lat, lng)
        assert loc.hemisphere == expected


    def test_hemisphere_errors(self):
        """We don't validate the input, but we expect
        lat and lng to be floats rather than eg strings.
        It's not exactly intentional, but this test is
        documenting that behaviour.
        """
        lat = '37°S'
        lng = '144°E'
        loc = location.Location(lat, lng)
        with pytest.raises(TypeError):
            _hemisphere = loc.hemisphere
        
