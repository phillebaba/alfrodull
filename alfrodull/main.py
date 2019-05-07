"""
Main script to start dbus notifiation and application loop.
"""
import sys
import argparse
import importlib

import dbus
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib
import yaml

from alfrodull.event.sleep import Sleep
from alfrodull.animation.outside_in import OutsideIn

def read_and_validate_configuration(file_path):
    """
    Reads the content of the specifed file_path
    and tries to parse it's content into a config object.
    """
    with open(file_path, 'r') as stream:
        try:
            config_dict = yaml.safe_load(stream)
        except yaml.YAMLError as error:
            print(error)
            return None

    for (key, value) in config_dict.items():
        if key == "device":
            device = importlib.import_module("devices.{}".format(value)).create()
        elif key == "events":
            events = []
            for item in value:
                event = Sleep(**item)
                events.append(event)

    if not device or not events:
        return None

    return (device, events)

class Application():
    def __init__(self, config_file_path):
        config = read_and_validate_configuration(config_file_path)
        if not config:
            print("Could not parse configuration file")
            sys.exit(1)

        self.device = config[0]
        self.events = config[1]

        print("Starting Alfrodull")

        # Setup DBUS notifications
        DBusGMainLoop(set_as_default=True)
        bus = dbus.SystemBus()

        for event in self.events:
            event.subscribe(bus, self.handle_event)

        self.handle_event()

        try:
            loop = GLib.MainLoop()
            loop.run()
        except KeyboardInterrupt:
            loop.quit()

    def handle_event(self, *args):
        """
        Handles triggered dbus event.
        """
        print(args)
        event = self.events[0]
        outside_in = OutsideIn()
        outside_in.animate(self.device, event.color)

def main():
    """
    Main method.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("config")
    args = parser.parse_args()

    Application(args.config)

if __name__ == "__main__":
    main()
