import pytest

from alfrodull.devices.blinkstick import Blinkstick
from alfrodull.animation.inside_out import InsideOut

testdata = [
    ("#000000", "#ffffff"),
    ("#ffffff", "#000000"),
    ("#ad1219", "#05ff20")
]

@pytest.mark.parametrize("start,end", testdata)
def test(device, start, end):
    device.set_all(start)
    animation = InsideOut()
    animation.animate(device, end)
