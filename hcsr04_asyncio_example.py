from hcsr04 import HCSR04
import uasyncio as asyncio
# Educabord GPIO 4-> PB2. 0->PB1,
# 26->LED1, 15EXPCS, 14->ROT ENC PB, 34->POTM
ultrasonic = HCSR04(15, 34)

async def distance():
    while True:
        print(f"distance: {ultrasonic.distance_cm()} CM")
        await asyncio.sleep_ms(1000)
        
loop = asyncio.get_event_loop()
loop.create_task(distance())
loop.run_forever()
