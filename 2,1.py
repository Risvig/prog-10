from machine import Pin, deepsleep
from time import sleep
import esp32

led1 =Pin (26, Pin.OUT)


wake_pin = Pin(0, Pin.IN, Pin.PULL_UP)
esp32.wake_on_ext0(pin = wake_pin,
                   level = esp32.WAKEUP_ALL_LOW)
deepsleep()

for i in range(10):
    led1.value(not led1.value())
    sleep(0.2)

print(f"ESP32 woke up from deepsleep")
sleep(4)
print(f"ESP32 going to deepsleep")
deepsleep()