from machine import Pin
import time

btn_pin = Pin(5, Pin.IN, Pin.PULL_UP)

dernier_appui = 0
DELAI_REBOND = 200  

def callback(pin):
    global dernier_appui
    maintenant = time.ticks_ms()
    if time.ticks_diff(maintenant, dernier_appui) > DELAI_REBOND:
        print("Bouton appuyé")
        dernier_appui = maintenant

btn_pin.irq(trigger=Pin.IRQ_FALLING, handler=callback)
