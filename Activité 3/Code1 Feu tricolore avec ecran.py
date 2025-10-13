from machine import Pin, I2C
from time import sleep, ticks_ms
from grove_lcd_i2c import Grove_LCD_I2C

LCD_SDA = Pin(0)
LCD_SCL = Pin(1)
LCD_ADDR = 62
i2c = I2C(0, sda=LCD_SDA, scl=LCD_SCL)
lcd = Grove_LCD_I2C(i2c, LCD_ADDR, True)

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
        restant = delai - ((ticks_ms() - debut) // 1000)
        lcd.clear()
        lcd.write(f"Feu vert : {restant}s\n")
        if bp.value() == 0:
            lcd.clear()
            lcd.write("Passage demande\n")
            while bp.value() == 0:
                pass
            sleep(0.2)
            break
        sleep(0.5)

def attendre_orange(delai):
    for i in range(int(delai), 0, -1):
        lcd.clear()
        lcd.write(f"Feu orange : {i}s\n")
        sleep(1)

def afficher_passage_autorise(duree):
    for i in range(duree, 0, -1):
        lcd.clear()
        lcd.write(f"Passage autorise\nPietons : {i}s")
        sleep(1)

def sequence_feu(delai):
    allumer_led(led_verte)
    attendre_verte(delai)
    eteindre_led(led_verte)

    allumer_led(led_orange)
    attendre_orange(delai / 2)
    eteindre_led(led_orange)

    allumer_led(led_rouge)
    afficher_passage_autorise(int(delai / 2))
    eteindre_led(led_rouge)

def extinction_leds():
    eteindre_led(led_rouge)
    eteindre_led(led_verte)
    eteindre_led(led_orange)
    lcd.clear()
    lcd.write("Systeme eteint\n")

def main():
    try:
        while True:
            sequence_feu(DELAI_BASE)
    except KeyboardInterrupt:
        extinction_leds()
        print("Programme interrompu proprement.")

main()

