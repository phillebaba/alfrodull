"""
Main script to start dbus notifiation and application loop.
"""
import sys
import time
import os

import dbus
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib
from blinkstick import blinkstick

ANIMATION_SPEED = 0.04

class LightController:
    def __init__(self, bstick, color, led_count):
        """Starts main application loop."""
        self.bstick = bstick
        self.color = color
        self.led_count = led_count
        self.file_descriptor = None

        # Setup DBUS notifications
        DBusGMainLoop(set_as_default=True)
        bus = dbus.SystemBus()
        proxy = bus.get_object('org.freedesktop.login1', '/org/freedesktop/login1')
        self.login1 = dbus.Interface(proxy, dbus_interface='org.freedesktop.login1.Manager')
        bus.add_signal_receiver(
            self.handle_sleep,
            'PrepareForSleep',
            'org.freedesktop.login1.Manager',
            'org.freedesktop.login1'
        )
        loop = GLib.MainLoop()

        self.handle_sleep(False)
        time.sleep(1)
        self.handle_sleep(True)
        time.sleep(1)
        self.handle_sleep(False)

        try:
            loop.run()
        except KeyboardInterrupt:
            loop.quit()

    def handle_sleep(self, value):
        """Handles sleep notifications."""
        print("Sleep notification with value {}".format(value))

        if value:
            self.turn_off()

            if self.file_descriptor:
                os.close(self.file_descriptor.take())
        else:
            self.turn_on()
            self.file_descriptor = self.login1.Inhibit("sleep", "myapps", "because I want it", "delay")

    def turn_off(self):
        """Turns off all of the lights."""
        max_value = int((self.led_count / 2))
        for i in reversed(range(max_value)):
            self.bstick.set_color(index=self.led_count - 1 - i, red=0, green=0, blue=0)
            self.bstick.set_color(index=i, red=0, green=0, blue=0)
            time.sleep(ANIMATION_SPEED)

    def turn_on(self):
        """Turns on light with specified color."""
        max_value = int((self.led_count / 2))
        for i in range(max_value):
            self.bstick.set_color(index=self.led_count - 1 - i, name=self.color)
            self.bstick.set_color(index=i, name=self.color)
            time.sleep(ANIMATION_SPEED)

def main():
    """Main method."""
    print("Starting Light Controller")

    # Setup Blinkstick
    bstick = blinkstick.find_first()
    if not bstick:
        print("Blinkstick not found.")
        sys.exit(1)

    led_count = bstick.get_led_count()

    # Get light color
    if len(sys.argv) == 2:
        color = sys.argv[1]
    else:
        color = "white"

    LightController(bstick, color, led_count)

    print("Stopping Light Controller")


if __name__ == "__main__":
    main()
