import time
import django


def get_average(c1, c2, w1, w2):
    return (c1*(w2-w1) + c2 * w1) / w2


def led_control_loop():
    time_resolution = 100
    timer = 0
    current_led_state = CurrentLedState.get_solo()
    profile = current_led_state.profile
    led_states = LedState.objects.from_profile(profile)
    led_state_index = 0
    current_led_state.set_color(led_states[led_state_index].red,
                                led_states[led_state_index].green,
                                led_states[led_state_index].blue)

    next_led_state_index = (led_state_index + 1) % len(led_states)
    fading = False

    while True:
        new_profile = CurrentLedState.get_solo().profile
        if profile.pk != new_profile.pk:
            profile = new_profile
            led_states = LedState.objects.from_profile(profile)
            led_state_index = 0
            timer = 0
            fading = False

        timer += time_resolution
        if not fading and timer >= profile.hold_time:
            timer = 0
            next_led_state_index = (led_state_index + 1) % len(led_states)
            fading = True

        if fading:
            if timer < profile.fade_time:
                red = get_average(led_states[led_state_index].red,
                                  led_states[next_led_state_index].red,
                                  timer,
                                  profile.fade_time)
                green = get_average(led_states[led_state_index].green,
                                    led_states[next_led_state_index].green,
                                    timer,
                                    profile.fade_time)
                blue = get_average(led_states[led_state_index].blue,
                                   led_states[next_led_state_index].blue,
                                   timer,
                                   profile.fade_time)

                current_led_state.set_color(red, green, blue)
            else:
                fading = False
                timer = 0
                led_state_index = next_led_state_index
                current_led_state.set_color(led_states[led_state_index].red,
                                            led_states[led_state_index].green,
                                            led_states[led_state_index].blue)
        time.sleep(time_resolution / 1000)


if __name__ == '__main__':
    django.setup()
    from led.models import CurrentLedState, LedState

    led_control_loop()
