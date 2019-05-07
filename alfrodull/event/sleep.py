import os

import dbus

class Sleep():
    def __init__(self, name, color, effect):
        self.name = name
        self.color = color
        self.effect = effect

        self.file_descriptor = None
        self.login1 = None

    def subscribe(self, bus, handler_function):
        proxy = bus.get_object('org.freedesktop.login1', '/org/freedesktop/login1')
        self.login1 = dbus.Interface(proxy, dbus_interface='org.freedesktop.login1.Manager')
        bus.add_signal_receiver(
            handler_function,
            'PrepareForSleep',
            'org.freedesktop.login1.Manager',
            'org.freedesktop.login1'
        )

    def lock(self):
        self.file_descriptor = self.login1.Inhibit("sleep",
                                                   "light-controller",
                                                   "Light Animation",
                                                   "delay")

    def release(self):
        if self.file_descriptor:
            os.close(self.file_descriptor.take())
