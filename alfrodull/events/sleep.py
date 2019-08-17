import os

import dbus

class Sleep():
    def __init__(self, animation):
        self.animation = animation

        self.manager = None
        self.fd = None

    def register(self, callback):
        self.callback = callback

        bus = dbus.SystemBus()
        proxy = bus.get_object('org.freedesktop.login1', '/org/freedesktop/login1')
        self.manager = dbus.Interface(proxy, dbus_interface='org.freedesktop.login1.Manager')

        self.inhibit()

        bus.add_signal_receiver(
            self.handle_signal,
            'PrepareForSleep',
            'org.freedesktop.login1.Manager',
            'org.freedesktop.login1'
        )

    def inhibit(self):
        self.fd = self.manager.Inhibit("sleep",
                                      "light-controller",
                                       "Light Animation",
                                       "delay")

    def handle_signal(self, value):
        if value:
            self.callback(self)

            if self.fd:
                os.close(self.fd.take())
        else:
            self.inhibit()
