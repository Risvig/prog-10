from machine import WDT, Timer

def reset_watchdog(obj):# callback der feeder watchdog timer
    print ("Feeding the watchdog!")
    wtd.feed() # her feedes wdt med metoden feed

wdt = WDT(timeout=2000) # timeout på 2000 ms

timer_0 = Timer(0) #ESP32 har 4 hardware Timers som kan anvendes
# her initialiseres en periodisk timer som kalder reset_watchdog hver 1.5 sekund
timer_0.init(period=1500, mode=Timer.PERIODIC, callback=reset_watchdog)
