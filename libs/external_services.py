import smtplib
import logging
from django.core.mail import send_mail

logger = logging.getLogger(__name__)


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
