import pytest


@pytest.fixture()
def osm_is_down(monkeypatch):
    """Simulate that OpenStreetMap is down and calling
    its API raises a requests ReadTimeoutError.
    """
    import requests
    import geocoder

    def fake_osm(latlng, method='reverse'):
        raise requests.exceptions.ReadTimeout()

    monkeypatch.setattr(geocoder, 'osm', fake_osm)
