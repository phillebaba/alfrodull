from alfrodull.devices.blinkstick import Blinkstick
from alfrodull.animation.fade import Fade

def test_on(device):
    device.set_all("#000000")
    animation = Fade()
    animation.animate(device, "#ffffff")

def test_off(device):
    device.set_all("#ffffff")
    animation = Fade()
    animation.animate(device, "#000000")
