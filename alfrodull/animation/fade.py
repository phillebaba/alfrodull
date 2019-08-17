import time

from alfrodull import util

class Fade():
    def __init__(self, color, duration=0.3, steps=20):
        self.color = color
        self.duration = duration
        self.steps = steps

    def animate(self, device):
        delay = self.duration/self.steps
        current_color = device.get_current_color()
        gradient = util.linear_gradient(current_color, self.color, self.steps)
        for step in gradient:
            device.set_all(step)
            time.sleep(delay)
