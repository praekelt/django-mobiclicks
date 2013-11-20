from django.conf import settings
from django.test import TestCase
from django.test.utils import override_settings
from django.test.client import RequestFactory
from django.utils.importlib import import_module

from mobiclicks.middleware import MobiClicksMiddleware, CPA_TOKEN_SESSION_KEY


class RequestFactoryTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        # set up a session
        settings.SESSION_ENGINE = 'django.contrib.sessions.backends.file'
        engine = import_module(settings.SESSION_ENGINE)
        store = engine.SessionStore()
        store.save()
        self.session = store
        self.factory.cookies[settings.SESSION_COOKIE_NAME] = store.session_key

    def make_request(self, url, method='get'):
        request = getattr(self.factory, method)(url)
        request.session = self.session
        return request


class MiddlewareTestCase(RequestFactoryTestCase):

    def test_default_settings(self):
        cpatoken = 'foo'
        request = self.make_request('/?cpa=%s' % cpatoken)
        middleware = MobiClicksMiddleware()
        middleware.process_request(request)
        self.assertIn(CPA_TOKEN_SESSION_KEY, self.session)
        self.assertEquals(self.session[CPA_TOKEN_SESSION_KEY], cpatoken)
