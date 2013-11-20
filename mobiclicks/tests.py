from django.conf import settings
from django.dispatch import receiver
from django.test import TestCase
from django.test.client import RequestFactory
from django.test.signals import setting_changed
from django.utils.importlib import import_module

from mobiclicks.middleware import MobiClicksMiddleware
from mobiclicks import conf


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
    cpatoken = 'foo'

    def test_default_settings(self):
        request = self.make_request('/?cpa=%s' % self.cpatoken)
        middleware = MobiClicksMiddleware()
        middleware.process_request(request)
        self.assertIn(conf.CPA_TOKEN_SESSION_KEY, self.session)
        self.assertEquals(self.session[conf.CPA_TOKEN_SESSION_KEY],
                          self.cpatoken)

    def test_custom_settings(self):
        with self.settings(MOBICLICKS={
            'CPA_TOKEN_SESSION_KEY': 'foo_session_key',
            'CPA_TOKEN_PARAMETER_NAME': 'foo_param_name'}
        ):
            self.assertEqual(conf.CPA_TOKEN_SESSION_KEY, 'foo_session_key')
            self.assertEqual(conf.CPA_TOKEN_PARAMETER_NAME, 'foo_param_name')

            request = self.make_request('/?cpa=%s' % self.cpatoken)
            middleware = MobiClicksMiddleware()
            middleware.process_request(request)
            self.assertNotIn(conf.CPA_TOKEN_SESSION_KEY, self.session)

            request = self.make_request('/?foo_param_name=%s' % self.cpatoken)
            middleware.process_request(request)
            self.assertIn(conf.CPA_TOKEN_SESSION_KEY, self.session)
            self.assertEquals(self.session[conf.CPA_TOKEN_SESSION_KEY],
                              self.cpatoken)


@receiver(setting_changed)
def settings_changed_handler(sender, **kwargs):
    if kwargs['setting'] == 'MOBICLICKS':
        conf.init_configuration()
