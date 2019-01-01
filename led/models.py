from __future__ import unicode_literals

from django.db import models
from solo.models import SingletonModel


class Profile(models.Model):
    name = models.CharField(max_length=255)
    hold_time = models.IntegerField()  # ms
    fade_time = models.IntegerField()  # ms

    def __str__(self):
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

    def __str__(self):
        return '{} #{}'.format(self.profile.name, self.order)


class CurrentLedState(SingletonModel):
    profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, null=True)

    def change_profile(self, profile):
        self.profile = profile
        self.save()
