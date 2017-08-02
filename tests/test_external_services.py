import pytest
from libs import external_services


@pytest.mark.external
def test_get_address_from_latlng_success(caplog):
    """
    This test could be flaky (ie pass or fail unpredictably)
    if the OpenStreetMap server has problems!
    """
    lat, lng = (-37.813628, 144.963058)
    result = external_services.get_address_from_latlng(lat, lng)
    assert result.country == 'Australia'
    assert 'get_address_from_latlng: successfully looked up 1 latlng' in caplog.text


def test_get_address_from_latlng_failure(osm_is_down):
    """Simulate where the OpenStreetMap server is down and we get
    a ReadTimeout. osm_is_down is a pytest fixture, defined in conftest.py
    """
    lat, lng = (-37.813628, 144.963058)
    result = external_services.get_address_from_latlng(lat, lng)
    assert result.country == False


def test_send_mail_safely_success(mailserver_is_good):
    error = external_services.send_mail_safely('Subject',
                                               'Body of email',
                                               'me@me.com',
                                               'you@you.com')
    assert not error
    # One message was "sent"
    assert len(mailserver_is_good) == 1
