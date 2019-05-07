import time

class OutsideIn():
    def __init__(self, speed=0.04):
        self.speed = speed

    def animate(self, device, color):
        led_count = device.led_count()
        max_value = int((led_count / 2))
        for i in range(max_value):
            print(i)
            device.set(led_count - 1 - i, color)
            device.set(i, color)
            time.sleep(self.speed)
