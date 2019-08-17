import time

import pytest

from alfrodull.devices.blinkstick import Blinkstick

@pytest.fixture
def device():
    time.sleep(0.5)
    return Blinkstick()
