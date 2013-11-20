import requests
from celery import task

from mobiclicks import conf


@task()
def confirm_click(click_ref):
    requests.post(conf.CLICK_CONFIRMATION_URL,
                  params={'action': 'clickReceived',
                          'authKey': conf.CPA_SECURITY_TOKEN,
                          'clickRef': click_ref})
