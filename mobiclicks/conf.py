import sys
from django.conf import settings


defaults = {
    'CPA_TOKEN_SESSION_KEY': 'mobiclicks_cpatoken',
    'CPA_TOKEN_PARAMETER_NAME': 'cpa',
    'CPA_SECURITY_TOKEN': None,
    'ACQUISITION_TRACKING_URL': 'http://t.mobiclicksdirect.com/acquisition',
    'CLICK_CONFIRMATION_URL': 'http://t.mobiclicksdirect.com/advertiser',
    'TRACK_REGISTRATIONS': True,
    'CONFIRM_CLICKS': True,
}


def init_configuration():
    settings_dict = getattr(settings, 'MOBICLICKS', {})

    for key, default_value in defaults.iteritems():
        setattr(sys.modules[__name__], key,
                settings_dict.get(key, defaults[key]))


init_configuration()
