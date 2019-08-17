import dbus

class Wakeup():
    def __init__(self, animation):
        self.animation = animation

        self.manager = None

    def register(self, callback):
        self.callback = callback

        bus = dbus.SystemBus()
        proxy = bus.get_object('org.freedesktop.login1', '/org/freedesktop/login1')
        self.manager = dbus.Interface(proxy, dbus_interface='org.freedesktop.login1.Manager')

        bus.add_signal_receiver(
            self.handle_signal,
            'PrepareForSleep',
            'org.freedesktop.login1.Manager',
            'org.freedesktop.login1'
        )

    def handle_signal(self, value):
        if not value:
            self.callback(self)
