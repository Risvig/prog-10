from machine import Pin, deepsleep
from time import sleep
from neopixel import NeoPixel
from random import randint

n = 12
p = 26
np = neopixel.NeoPixel(Pin(p, Pin.OUT), n)

red = randint(0, 255)
green = randint(0, 255)
blue = randint(0, 255)

wake_pin = Pin(0, Pin.IN, Pin.PULL_UP)
esp32.wake_on_ext0(pin = wake_pin,
                   level = esp32.WAKEUP_ALL_LOW)
deepsleep()

print(f"random color on neopixel")

for i in range(n):
    np[pixel] = (red, green, blue)

np.write

print(f"ESP32 woke up from deepsleep")
sleep(2)
print(f"ESP32 going to deepsleep")
deepsleep(1000)