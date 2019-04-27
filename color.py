import sys

from blinkstick import blinkstick

def main():
    if len(sys.argv) == 2:
        color = sys.argv[1]
    else:
        color = "white"

    print("Changing to color " + color)

    bstick = blinkstick.find_first()
    led_count = bstick.get_led_count()

    for i in range(0, led_count):
        bstick.set_color(channel=0, index=i, name=color)

if __name__ == "__main__":
    main()
