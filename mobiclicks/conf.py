import sys

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


defaults = {
    'CPA_TOKEN_SESSION_KEY': 'mobiclicks_cpatoken',
    'CPA_TOKEN_PARAMETER_NAME': 'cpa',
    'CLICK_REF_PARAMETER_NAME': 'pollen8_click_ref',
    'CPA_SECURITY_TOKEN': None,
    'ACQUISITION_TRACKING_URL': 'http://t.mobiclicksdirect.com/acquisition',
    'CLICK_CONFIRMATION_URL': 'http://t.mobiclicksdirect.com/advertiser',
    'TRACK_REGISTRATIONS': True,
    'CONFIRM_CLICKS': True,
}


def init_configuration():
    settings_dict = getattr(settings, 'MOBICLICKS', {})

    if settings_dict.get('CPA_SECURITY_TOKEN', None) is None:
        raise ImproperlyConfigured("Setting MOBICLICKS['CPA_SECURITY_TOKEN']"
                                   " is required")

    for key, default_value in defaults.iteritems():
        setattr(sys.modules[__name__], key,
                settings_dict.get(key, defaults[key]))


init_configuration()
