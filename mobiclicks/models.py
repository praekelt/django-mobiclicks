from django.contrib.auth.signals import user_logged_in
from django.utils import timezone

from mobiclicks import conf
from mobiclicks.tasks import track_registration_acquisition


def check_for_new_user_and_track(sender, **kwargs):
    '''
    Check that the user came to the site via a
    MobiClicks ad and that the user is newly
    created. If so, track the registraiton acquisition.
    '''
    request = kwargs['request']
    user = kwargs['user']

    if (conf.CPA_TOKEN_SESSION_KEY in request.session and
            (timezone.now() - user.date_joined).total_seconds() < 1):
        track_registration_acquisition.delay(
            request.session[conf.CPA_TOKEN_SESSION_KEY]
        )
        del request.session[conf.CPA_TOKEN_SESSION_KEY]


if conf.TRACK_REGISTRATIONS:
    user_logged_in.connect(check_for_new_user_and_track)
