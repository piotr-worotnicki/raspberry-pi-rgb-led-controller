import subprocess

from django.conf import settings

call_template = u'echo "{pin}={value}" > /dev/pi-blaster'


def set_color(r, g, b):
    resolution = float(255)
    subprocess.Popen(call_template.format(**{'pin': settings.RED_PIN, 'value': r / resolution}))
    subprocess.Popen(call_template.format(**{'pin': settings.GREEN_PIN, 'value': g / resolution}))
    subprocess.Popen(call_template.format(**{'pin': settings.BLUE_PIN, 'value': b / resolution}))
