from __future__ import unicode_literals

from django.db import models
from solo.models import SingletonModel

from led.led_wrappper import set_color


class CurrentLedState(SingletonModel):
    red = models.IntegerField(default=1)
    green = models.IntegerField(default=1)
    blue = models.IntegerField(default=1)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super(CurrentLedState, self).save(force_insert, force_update, using, update_fields)
        set_color(self.red, self.green, self.blue)

    @classmethod
    def fade(cls, red, green, blue):
        current_led_state = cls.get_solo()
        current_led_state.red = red
        current_led_state.green = green
        current_led_state.blue = blue
        current_led_state.save()