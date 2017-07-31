import pytest
from libs import external_services


@pytest.mark.external
def test_get_address_from_latlng_success():
    """
    This test could be flaky (ie pass or fail unpredictably)
    if the OpenStreetMap server has problems!
    """
    lat, lng = (-37.813628, 144.963058)
    result = external_services.get_address_from_latlng(lat, lng)
    print(result)
    assert result.country == 'Australia'


def test_get_address_from_latlng_failure(osm_is_down):
    """Simulate where the OpenStreetMap server is down and we get
    a ReadTimeout. osm_is_down is a pytest fixture, defined in conftest.py
    """
    lat, lng = (-37.813628, 144.963058)
    result = external_services.get_address_from_latlng(lat, lng)
    print(result)
    assert result.country == False


