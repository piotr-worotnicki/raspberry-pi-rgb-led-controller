from django.contrib import admin

# Register your models here.
from solo.admin import SingletonModelAdmin

from led.models import Profile, LedState, CurrentLedState


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(LedState)
class LedStateAdmin(admin.ModelAdmin):
    list_display = ['order', 'profile', 'red', 'green', 'blue']
    list_filter = ['profile']


@admin.register(CurrentLedState)
class CurrentLedStateAdmin(SingletonModelAdmin):
    pass
