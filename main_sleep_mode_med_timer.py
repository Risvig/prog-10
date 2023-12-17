from machine import Pin, deepsleep
from time import sleep

#bruger en timer

sleep_time_ms = 4000
led1 = Pin(26, Pin.OUT)
led1.value(1)
sleep(2)
led1.value(0)

print(f"ESP32 will now sleep for [sleep_time_ms/1000] seconds")
deepsleep(4000)
