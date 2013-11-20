from mobiclicks import conf
from mobiclicks.tasks import confirm_click


class MobiClicksMiddleware(object):
    '''
    If a request is redirected from MobiClicks,
    stores the acquisition code in the session
    so that conversions can be tracked later.
    Also does click confirmation if it is enabled.
    '''

    def process_request(self, request):
        # store the CPA token for later acquisition tracking
        if conf.CPA_TOKEN_PARAMETER_NAME in request.GET:
            request.session[conf.CPA_TOKEN_SESSION_KEY] = \
                request.GET[conf.CPA_TOKEN_PARAMETER_NAME]

        # confirm the ad click-through, if enabled
        if (conf.CONFIRM_CLICKS and
                conf.CLICK_REF_PARAMETER_NAME in request.GET):
            confirm_click.delay(request.GET[conf.CLICK_REF_PARAMETER_NAME])
