import pytest


@pytest.fixture()
def osm_is_down(monkeypatch):
    """Simulate that OpenStreetMap is down and calling
    its API raises a requests ReadTimeoutError.

    We are monkeypatching the geocoder library's 'osm' method.
    """
    import requests
    import geocoder

    def fake_osm(latlng, method='reverse'):
        print('Here I am in the fake_osm method')
        raise requests.exceptions.ReadTimeout()

    # Replace the real method with our fake one.
    # This is basically the same as
    #     geocoder.osm = fake_osm
    # (But monkeypatch will clean up for us.)
    monkeypatch.setattr(geocoder, 'osm', fake_osm)



@pytest.fixture()
def mailserver_is_good(monkeypatch):
    """Simulate that the mail server is working.
    We are monkeypatching the django.core.mail send_mail function -
    at least the version of it imported in our external_services module.
    """
    from libs import external_services

    messages = []

    def fake_send_mail(subj, body, sender, receivers, fail_silently=False):
        print('Here I am in the fake_send_mail method')
        messages.append((subj, body, sender, receivers))

    monkeypatch.setattr(external_services, 'send_mail', fake_send_mail)
    return messages
