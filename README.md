# Alfrodull
Alfrodull is a utility that automatically controls lights based on the a computers events.

The lights will turn off when the computer suspends, and turn on when the computer returns from the suspended state.
The idea is that the led strips are attached behind or close to the computers monitors, making it look like the lights
turn on and off with the displays.

Right now the only supported devices are those from [blinksticks](https://www.blinkstick.com/). More can be supported if
requested and I can get ahold of them.

## Install
TBD

## Usage
TBD

### Config File
Alfrodull is configured with a configuration file, this is where the effect, color and events are specified.
Colors are defined as hex values ex. `#ff00ff`, the values will be checked when the program is started and
throw an exception if they can't be parsed. Passing a null value to the color is parsed as turning off the lights.
Right now only predefined events and effects can be used, the possible options are defined below.

| Event | Description |
| --- | --- |
| Turn On | After the first boot or when the applicationn is first run. |
| Turn Off | Before the computer turns off. |
| Lock | Before the computer locks. |
| Sleep | Before the computer goes to sleep. |

| Effect | Description |
| --- | --- |
| Fade | Fades from the current color or if the color is null turn off. |
| Outside In | Starts from the outside and changes light one by one to the inside. |
| Inside Out | Opposite of Outside In. |
| Knight Rider | Think the front of K.I.T.T. |

```yml
---
device:
  type: blinkstick

events:
  - event: Shutdown
    color: null
    effect: fade

  - event: Turn On
    color: #ffffff
    effect: Inside Out
```

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
