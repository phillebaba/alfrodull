# Light Controller
Light Controller is a small python script to control [blinksticks](https://www.blinkstick.com/) lights.
The lights will turn off when the computer suspends, and turn on when the computer returns from the suspended state.
The idea is that the led strips are attached behind or close to the computers monitors, making it look like the lights
turn on and off with the displays.

This script depends on DBus signals from [logind](https://www.freedesktop.org/wiki/Software/systemd/logind/), specifically `PrepareForSleep`.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
