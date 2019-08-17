# Alfrodull
Alfrodull is a utility that controls lights based on the a computers events.

The lights can be turned off when the computer sleepd, and turn on when the computer wakes up. The original use case was to attach an led strip behind the monitor that turn on and off as the display does. But much more can be doen as additional events can easily be added. For example blinking the lights when notifications are received or tracking CPU usage and warning when it passes a threshold.

Right now the only supported devices are those from [blinksticks](https://www.blinkstick.com/). More can be added if requested and I can get ahold of them.

## Install
```bash
pip install alfrodull
```

## Usage
Simply start alfrodull and pass a configuration file path as input.
```bash
alfrodull config.yml
```
Alfrodull could for example be started in xinit or i3wm config.

## Configuration
Alfrodull is configured with a file, this is where the event, animation and, color are specified. Colors are defined as hex values ex. `#ff00ff`, the values will be checked when the program is started and throw an exception if they can't be parsed. Passing a null value to the color is parsed as turning off the lights. Below are the currently supported events and animations that can be used.

| Event | Description |
| --- | --- |
| Init | After the applicationn is first run |
| Shutdown | Before the computer turns off |
| Sleep | Before the computer goes to sleep |
| Wakeup | After the computer wakes up |

| Effect | Description |
| --- | --- |
| Fade | Fades from the current color or if the color is null turn off. |
| Outside In | Starts from the outside and changes light one by one to the inside. |
| Inside Out | Opposite of Outside In. |

```yml
device: blinkstick
events:
  - type: "Init"
    animation:
      type: "Fade"
      color: "#ffffff"
  - type: "Sleep"
    animation:
      type: "Inside Out"
      color: "#000000"
  - type: "Wakeup"
    animation:
      type: "Outside In"
      color: "#ffffff"
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
