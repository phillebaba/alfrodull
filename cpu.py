from blinkstick import blinkstick
import psutil

bstick = blinkstick.find_first()

if bstick is None:
    print("No BlinkSticks found...")
else:
    print("Displaying CPU usage (Green = 0%, Amber = 50%, Red = 100%)")
    print("Press Ctrl+C to exit")

    led_count = bstick.get_led_count()

    # Go into a forever loop
    while True:
        cpu = psutil.cpu_percent(interval=1)
        intensity = int(255 * cpu / 100)

        for i in range(0, led_count):
            bstick.set_color(index=i, red=intensity, green=255 - intensity, blue=0)
