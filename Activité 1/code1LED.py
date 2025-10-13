from machine import Pin
from time import sleep

led_rouge = Pin(18, Pin.OUT)
led_orange = Pin(19, Pin.OUT)
led_verte = Pin(20, Pin.OUT)

delai = 10

try:
    while True:
        # Vert
        led_rouge.off()
        led_orange.off()
        led_verte.on()
        sleep(delai)

        # Orange
        led_verte.off()
        led_orange.on()
        sleep(delai * 0.2)

        # Rouge
        led_orange.off()
        led_rouge.on()
        sleep(delai * 0.8)

except KeyboardInterrupt:
    led_rouge.off()
    led_orange.off()
    led_verte.off()
