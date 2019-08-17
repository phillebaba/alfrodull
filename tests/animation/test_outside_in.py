import pytest

from alfrodull.devices.blinkstick import Blinkstick
from alfrodull.animation.outside_in import OutsideIn

testdata = [
    ("#000000", "#ffffff"),
    ("#ffffff", "#000000"),
    ("#ad1219", "#05ff20")
]

@pytest.mark.parametrize("start,end", testdata)
def test_on(device, start, end):
    device.set_all(start)
    outside_in = OutsideIn()
    outside_in.animate(device, end)
