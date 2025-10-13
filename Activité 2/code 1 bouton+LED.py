from machine import Pin
from time import sleep

led_rouge = Pin(18, Pin.OUT)
led_orange = Pin(19, Pin.OUT)
led_verte = Pin(20, Pin.OUT)
bp = Pin(15, Pin.IN, Pin.PULL_UP)

def Attendre(delai):
    for _ in range(delai):
        if bp.value() == 0:
            print("Passage demandé")
        sleep(1)

try:
    while True:
        led_rouge.off()
        led_orange.off()
        led_verte.on()
        Attendre(10)

        led_verte.off()
        led_orange.on()
        Attendre(2)

        led_orange.off()
        led_rouge.on()
        Attendre(8)

except KeyboardInterrupt:
    led_rouge.off()
    led_orange.off()
    led_verte.off()

