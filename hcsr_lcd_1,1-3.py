from hcsr04 import HCSR04
from time import sleep
from gpio_lcd import GpioLcd
from machine import Pin, PWM
import uasyncio as asyncio
# Educabord GPIO 4-> PB2. 0->PB1,
# 26->LED1, 15EXPCS, 14->ROT ENC PB, 34->POTM

led1_pwm = PWM(Pin(26, Pin.OUT))
led1_pwm.duty(1023)

lcd = GpioLcd(rs_pin=Pin(27), enable_pin=Pin(25),
                  d4_pin=Pin(33), d5_pin=Pin(32),
                  d6_pin=Pin(21), d7_pin=Pin(22),
                  num_lines=4, num_columns=20)

ultrasonic = HCSR04(15, 34)

async def lcd_distance():
    while True:
        print(f"distance: {ultrasonic.distance_cm():.2f}")
        lcd.clear()
        lcd.putstr(f"Distance: {ultrasonic.distance_cm():.2f}")
        await asyncio.sleep(1)
        
async def led1_brightness_distance():
    while True:
        dist = int(ultrasonic.distance_cm())
        if dist < 0:
            dist = 0
        led1_pwm.duty(int(dist * 2.5575))
        await asyncio.sleep(1)
        
loop = asyncio.get_event_loop()
loop.create_task(lcd_distance())
loop.create_task(led1_brightness_distance())
loop.run_forever()