from django.shortcuts import render
from led.led_wrappper import set_color


def index(request):
    r = g = b = 50
    if request.POST:
        r = int(request.POST['red'])
        g = int(request.POST['green'])
        b = int(request.POST['blue'])
        set_color(r, g, b)

    return render(request, "sliders.html", context={'r': r, 'g': g, "b": b})
