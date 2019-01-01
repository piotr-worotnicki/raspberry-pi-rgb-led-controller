import time

import django

from led.led_wrappper import set_color


def get_average(c1, c2, w1, w2):
    return (c1 * (w2 - w1) + c2 * w1) / w2


class LedLoop(object):
    time_resolution = 50  # in ms
    timer = 0
    profile = None
    led_states = []
    led_state_index = 0
    fading = False
    next_led_state_index = 0

    def __init__(self) -> None:
        super().__init__()
        self.reset()

    def reset(self):
        self.timer = 0
        self.profile = CurrentLedState.get_solo().profile
        self.led_states = LedState.objects.from_profile(self.profile)
        self.led_state_index = 0
        self.next_led_state_index = (self.led_state_index + 1) % len(self.led_states)
        self.fading = False

        set_color(self.led_states[self.led_state_index].red,
                  self.led_states[self.led_state_index].green,
                  self.led_states[self.led_state_index].blue)

    def loop(self):
        while True:
            if self.profile.pk != CurrentLedState.get_solo().profile.pk:
                self.reset()

            self.timer += self.time_resolution

            if not self.fading and self.timer >= self.profile.hold_time:
                self.timer = 0
                self.next_led_state_index = (self.led_state_index + 1) % len(self.led_states)
                self.fading = True

            if self.fading:
                if self.timer < self.profile.fade_time:
                    red = get_average(self.led_states[self.led_state_index].red,
                                      self.led_states[self.next_led_state_index].red,
                                      self.timer,
                                      self.profile.fade_time)
                    green = get_average(self.led_states[self.led_state_index].green,
                                        self.led_states[self.next_led_state_index].green,
                                        self.timer,
                                        self.profile.fade_time)
                    blue = get_average(self.led_states[self.led_state_index].blue,
                                       self.led_states[self.next_led_state_index].blue,
                                       self.timer,
                                       self.profile.fade_time)

                    set_color(red, green, blue)
                else:
                    self.fading = False
                    self.timer = 0
                    self.led_state_index = self.next_led_state_index
                    set_color(self.led_states[self.led_state_index].red,
                              self.led_states[self.led_state_index].green,
                              self.led_states[self.led_state_index].blue)
            time.sleep(self.time_resolution / 1000)



if __name__ == '__main__':
    django.setup()
    from led.models import CurrentLedState, LedState

    loop = LedLoop()
    loop.loop()
