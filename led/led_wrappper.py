import subprocess

from django.conf import settings

call_template = u'echo "{pin}={value}" > /dev/pi-blaster'


def set_color(r, g, b):
    resolution = float(255)
    print(call_template.format(**{'pin': settings.RED_PIN, 'value': r / resolution}))
    subprocess.Popen(call_template.format(**{'pin': settings.RED_PIN, 'value': r / resolution}))
    print(call_template.format(**{'pin': settings.GREEN_PIN, 'value': g / resolution}))
    subprocess.Popen(call_template.format(**{'pin': settings.GREEN_PIN, 'value': g / resolution}))
    print(call_template.format(**{'pin': settings.BLUE_PIN, 'value': b / resolution}))
    subprocess.Popen(call_template.format(**{'pin': settings.BLUE_PIN, 'value': b / resolution}))
