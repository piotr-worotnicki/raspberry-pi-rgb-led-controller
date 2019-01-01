from django.shortcuts import render, redirect, get_object_or_404
from led.models import CurrentLedState, Profile


def index(request):
    profiles = Profile.objects.all()
    current_profile = CurrentLedState.get_solo().profile
    return render(request, "profiles.html", context={'profiles':profiles, 'current_profile':current_profile})


def change_profile(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    CurrentLedState.get_solo().change_profile(profile)
    return redirect('index')
