import sys

import dbus
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib
from blinkstick import blinkstick

bstick = None
led_count = 0
color = "White"

def handle_sleep(value):
    print ("System about to hibernate or suspend")
    print(value)
    if value == 1:
        turn_off()
    elif value == 0:
        turn_on()

def turn_off():
    data = [0] * led_count * 3
    bstick.set_led_data(0, data)

def turn_on():
    for i in range(0, led_count):
        bstick.set_color(channel=0, index=i, name=color)

def main():
    global bstick, led_count, color

    # Setup Blinkstick
    bstick = blinkstick.find_first()
    led_count = bstick.get_led_count()

    # Get light color
    if len(sys.argv) == 2:
        color = sys.argv[1]

    print("Starting Light Controller with color {}".format(color))

    # Set initial color
    turn_on()

    # Setup DBUS Notifications
    DBusGMainLoop(set_as_default=True)
    bus = dbus.SystemBus()
    bus.add_signal_receiver(               # define the signal to listen to
        handle_sleep,                      # callback function
        'PrepareForSleep',                 # signal name
        'org.freedesktop.login1.Manager',  # interface
        'org.freedesktop.login1'           # bus name
    )

    loop = GLib.MainLoop()

    try:
        loop.run()
    except KeyboardInterrupt:
        loop.quit()

if __name__ == "__main__":
    main()
