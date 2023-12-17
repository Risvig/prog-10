from time import ticks_us, ticks_diff
# gem starttidspunkt i microsekunder
start = ticks_us()

for n in range(33):
    n *= 33.0
#bereng tidsforskellen mellem start og slut tidspunkt
delta = ticks_diff(ticks_us(), start)
print (f"It took the loop [delta] microseconds to execute")
