from django.shortcuts import render
from led.models import CurrentLedState


def index(request):
    r = g = b = 50
    if request.POST:
        r = int(request.POST['red'])
        g = int(request.POST['green'])
        b = int(request.POST['blue'])
        CurrentLedState.get_solo().set_color(r, g, b)

    return render(request, "sliders.html", context={'r': r, 'g': g, "b": b})
