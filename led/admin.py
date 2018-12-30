from django.contrib import admin

# Register your models here.
from solo.admin import SingletonModelAdmin

from led.models import Profile, LedState, CurrentLedState


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(LedState)
class LedStateAdmin(admin.ModelAdmin):
    pass

@admin.register(CurrentLedState)
class CurrentLedStateAdmin(SingletonModelAdmin):
    pass