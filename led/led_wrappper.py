import subprocess

from django.conf import settings

call_template = u'echo "{pin}={value}" > /dev/pi-blaster'


def set_color(r, g, b):
    print call_template.format({u'pin': settings['RED_PIN'], u'value': r})
    print call_template.format({u'pin': settings['GREEN_PIN'], u'value': g})
    print call_template.format({u'pin': settings['BLUE_PIN'], u'value': b})
