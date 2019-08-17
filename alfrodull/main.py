"""
Main script to start dbus notifiation and application loop.
"""
import sys
import argparse
import os

import dbus
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib

from alfrodull.animation.fade import Fade
from alfrodull import util

class Application():
    def __init__(self, config_file_path):
        config = util.read_and_validate_configuration(config_file_path)
        if not config:
            print("Could not parse configuration file")
            sys.exit(1)

        self.device = config[0]
        self.events = config[1]
        self.fd = None

        print("Starting Alfrodull")

        for event in self.events:
            event.register(self.callback)

        try:
            loop = GLib.MainLoop()
            loop.run()
        except KeyboardInterrupt:
            print("Stopping Alfrodull")
            loop.quit()
            Fade(color="#000000").animate(self.device)

    def callback(self, event):
        event.animation.animate(self.device)

def main():
    """
    Main method.
    """
    DBusGMainLoop(set_as_default=True)

    parser = argparse.ArgumentParser()
    parser.add_argument("config")
    args = parser.parse_args()
    Application(args.config)

if __name__ == "__main__":
    main()
