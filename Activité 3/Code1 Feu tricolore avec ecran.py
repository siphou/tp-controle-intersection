from machine import Pin
from time import sleep
from grove_lcd_i2c import Grove_LCD_I2C

lcd = Grove_LCD_I2C(2, scl=Pin(3), sda=Pin(2))
led_rouge = Pin(18, Pin.OUT)
led_orange = Pin(19, Pin.OUT)
led_verte = Pin(20, Pin.OUT)
bp = Pin(15, Pin.IN, Pin.PULL_UP)

def Attendre(delai):
    for i in range(delai):
        if bp.value() == 0:
            lcd.setText("Passage demande")
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
        for i in range(8, 0, -1):
            lcd.setText("Passage autorise\nTemps restant: {}s".format(i))
            sleep(1)

except KeyboardInterrupt:
    led_rouge.off()
    led_orange.off()
    led_verte.off()
    lcd.setText("Systeme arrete")

