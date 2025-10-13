from machine import Pin
from time import sleep, ticks_ms

DELAI_BASE = 5  

led_rouge = Pin(18, Pin.OUT)
led_verte = Pin(20, Pin.OUT)
led_orange = Pin(19, Pin.OUT)
bp = Pin(15, Pin.IN, Pin.PULL_UP)

def allumer_led(pin):
    pin.value(1)

def eteindre_led(pin):
    pin.value(0)

def attendre_verte(delai):
    debut = ticks_ms()
    while (ticks_ms() - debut) < delai * 1000:
        if bp.value() == 0:  # 
            print("passage ")
            while bp.value() == 0:
                pass  
            sleep(0.2)  
            break
        sleep(0.1)

def sequence_feu(delai):
    allumer_led(led_verte)
    attendre_verte(delai)
    eteindre_led(led_verte)

    allumer_led(led_orange)
    sleep(delai / 2)
    eteindre_led(led_orange)

    allumer_led(led_rouge)
    sleep(delai / 2)
    eteindre_led(led_rouge)

def extinction_leds():
    eteindre_led(led_rouge)
    eteindre_led(led_verte)
    eteindre_led(led_orange)

def main():
    try:
        while True:
            sequence_feu(DELAI_BASE)
    except KeyboardInterrupt:
        extinction_leds()
        print("Programme interrompu proprement.")

main()
