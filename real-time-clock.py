from machine import RTC
rtc = RTC()

# år, måned, dag på måneden, ugedag, timer, minutter, sekunder og micro-sekunder day_of_the_week rtc.datetime() [3] # 0 indekseret

﻿day_of_the_week = rtc.datetime() [3] # 0 indekseret

print(f"It's the {day_of_the_week}. day of the week")
