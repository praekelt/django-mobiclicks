from mobiclicks import conf


class MobiClicksMiddleware(object):
    '''
    If a request is redirected from MobiClicks,
    stores the acquisition code in the session
    so that conversions can be tracked later.
    Also does click confirmation if it is enabled.
    '''

    def process_request(self, request):
        if conf.CPA_TOKEN_PARAMETER_NAME in request.GET:
            request.session[conf.CPA_TOKEN_SESSION_KEY] = \
                request.GET[conf.CPA_TOKEN_PARAMETER_NAME]
            # track the ad landing
