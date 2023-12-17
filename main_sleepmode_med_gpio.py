from machine import Pin, deepsleep
from time import sleep
import esp32
# Denne fil skal lægge som ESP32 som main.py
print ("hello")
wake_pin = Pin(0, Pin.IN, Pin.PULL_UP)
sleep(4)
esp32.wake_on_ext0(pin = wake_pin,
                   level = esp32.WAKEUP_ALL_LOW)
deepsleep()
