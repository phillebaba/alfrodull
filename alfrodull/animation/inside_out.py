import time

class InsideOut():
    def __init__(self, speed=0.04):
        self.speed = speed

    def animate(self, device, color):
        led_count = device.led_count()
        max_value = int((led_count / 2))
        for i in range(max_value):
            device.set(max_value +  i, color)
            device.set(max_value - i - 1, color)
            time.sleep(self.speed)
