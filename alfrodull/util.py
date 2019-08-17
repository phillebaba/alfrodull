import yaml

import importlib

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
                # Import event class
                event_type = item["type"]
                event_module = importlib.import_module("events.{}".format(event_type.lower()))
                event_class = getattr(event_module, event_type)

                # Import animation class
                animation_type = item["animation"]["type"]
                del item["animation"]["type"]
                animation_module = importlib.import_module("animation.{}".format(animation_type.lower().replace(" ", "_")))
                animation_class = getattr(animation_module, animation_type.replace(" ", ""))

                # Create event instance
                event = event_class(animation=animation_class(**item["animation"]))
                events.append(event)

    if not device or not events:
        return None

    return (device, events)

def hex_to_RGB(hex):
    """ "#FFFFFF" -> [255,255,255] """
    # Pass 16 to the integer function for change of base
    return [int(hex[i:i+2], 16) for i in range(1, 6, 2)]

def RGB_to_hex(RGB):
    """ [255,255,255] -> "#FFFFFF" """
    # Components need to be integers for hex to make sense
    RGB = [int(x) for x in RGB]
    return "#"+"".join(["0{0:x}".format(v) if v < 16 else
                        "{0:x}".format(v) for v in RGB])

def linear_gradient(start_hex, finish_hex, steps):
    """
    Returns a gradient list of (n) colors between
    two hex colors. start_hex and finish_hex
    should be the full six-digit color string,
    inlcuding the number sign ("#FFFFFF")
    """
    # Starting and ending colors in RGB form
    s = hex_to_RGB(start_hex)
    f = hex_to_RGB(finish_hex)
    # Initilize a list of the output colors with the starting color
    rgb_list = [s]
    # Calcuate a color at each evenly spaced value of t from 1 to n
    for step in range(1, steps):
        # Interpolate RGB vector for color at the current value of t
        curr_vector = [
            int(s[j] + (float(step)/(steps-1))*(f[j]-s[j]))
            for j in range(3)
        ]
        # Add it to our list of output colors
        rgb_list.append(curr_vector)

    #return rgb_list
    return [RGB_to_hex(rgb) for rgb in rgb_list]
