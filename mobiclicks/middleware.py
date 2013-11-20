from django.conf import settings


CPA_TOKEN_PARAMETER_NAME = (getattr(settings, 'MOBICLICKS', {})
                            .get('CPA_TOKEN_PARAMETER_NAME', 'cpa'))
CPA_TOKEN_SESSION_KEY = 'mobiclicks_cpatoken'


class MobiClicksMiddleware(object):
    '''
    If a request is redirected from MobiClicks,
    stores the acquisition code in the session
    so that conversions can be tracked later.
    '''

    def process_request(self, request):
        if CPA_TOKEN_PARAMETER_NAME in request.GET:
            request.session[CPA_TOKEN_SESSION_KEY] = \
                request.GET[CPA_TOKEN_PARAMETER_NAME]
