import smtplib
import logging
from django.core.mail import send_mail
import geocoder
import requests
import socket

logger = logging.getLogger(__name__)


class NoLocation:
    def __init__(self):
        self.country = False


def get_address_from_latlng_unsafe(lat, lng):
    """Exceptions, what exceptions?!
    """
    g = geocoder.osm([lat, lng], method='reverse')
    return g


def get_address_from_latlng(lat, lng):
    try:
        g = geocoder.osm([lat, lng], method='reverse')
        logger.info('get_address_from_latlng: successfully looked up 1 latlng')
    except requests.exceptions.RequestException as ex:
        g = NoLocation()
        logger.exception('get_address_from_latlng got a RequestException')
    return g


def send_mail_safely(subject, body, sender, receiver):
    error = None
    try:
        send_mail(subject, body, sender, [receiver], fail_silently=False)
        logger.info('send_mail_safely: successfully sent 1 mail')
    except ConnectionRefusedError as ex:
        error = 'The mail server is not available (ConnectionRefusedError)'
        logger.exception('send_mail_safely')
    except smtplib.SMTPServerDisconnected as ex:
        error = 'The mail server unexpectedly disconnected (SMTPServerDisconnected)'
        logger.exception('send_mail_safely')
    except Exception as ex:
        error = 'Unknown error ({0.msg})'.format(ex)
        logger.exception('send_mail_safely')
    return error


