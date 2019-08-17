from blinkstick import blinkstick

from alfrodull import util

def create():
    return Blinkstick()

class Blinkstick():
    def __init__(self):
        self.bstick = blinkstick.find_first()

    def led_count(self):
        return self.bstick.get_led_count()

    def get_current_color(self):
        led_data = self.bstick.get_led_data(1)
        return util.RGB_to_hex(led_data)

    def set(self, index, hex_value):
        self.bstick.set_color(index=index, channel=3, hex=hex_value)

    def set_all(self, hex_value):
        rgb = util.hex_to_RGB(hex_value)
        data = [rgb[1], rgb[0], rgb[2]] * self.led_count()
        self.bstick.set_led_data(0, data)
