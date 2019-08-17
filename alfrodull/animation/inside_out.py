import time

class InsideOut():
    def __init__(self, color, speed=0.04):
        self.color = color
        self.speed = speed

    def animate(self, device):
        led_count = device.led_count()
        max_value = int((led_count / 2))
        for i in range(max_value):
            device.set(max_value +  i, self.color)
            device.set(max_value - i - 1, self.color)
            time.sleep(self.speed)
