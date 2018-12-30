from __future__ import unicode_literals

from django.db import models
from solo.models import SingletonModel

from led.led_wrappper import set_color


class Profile(models.Model):
    name = models.CharField(max_length=255)
    hold_time = models.IntegerField()  # ms
    fade_time = models.IntegerField()  # ms

    def __unicode__(self):
        return self.name


class LedStateManager(models.Manager):
    def from_profile(self, profile):
        return self.filter(profile=profile.pk).order_by('order')


class LedState(models.Model):
    order = models.IntegerField(blank=False, null=False)
    red = models.IntegerField(default=0)
    green = models.IntegerField(default=0)
    blue = models.IntegerField(default=0)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    objects = LedStateManager()


class CurrentLedState(SingletonModel):
    red = models.IntegerField(default=1)
    green = models.IntegerField(default=1)
    blue = models.IntegerField(default=1)
    profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, null=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super(CurrentLedState, self).save(force_insert, force_update, using, update_fields)
        set_color(self.red, self.green, self.blue)

    def set_color(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
        self.save()
