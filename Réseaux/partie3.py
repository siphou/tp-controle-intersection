import time
import socket
import network
from machine import Pin

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    i = 0
    while not wlan.isconnected():
        print(f"temps d'attente {i}s - Waiting for connection...")
        time.sleep(1)
        i += 1
    print("WiFi :", wlan.ifconfig())
    return wlan.ifconfig()[0]

ssid = "Projet"
password = ""
ip = connect_wifi()

HOST = "172.16.12.121"   # IP du serveur fournie par le prof
PORT = 5001

rouge = Pin(20, Pin.OUT)
orange = Pin(19, Pin.OUT)
vert = Pin(18, Pin.OUT)

def envoyer_etat():
    etat = "bb" + str(rouge.value()) + str(orange.value()) + str(vert.value())
    print("Envoi :", etat)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        s.send(etat.encode())
        s.close()
    except OSError as e:
        print("Erreur socket :", e)

try:
    while True:
        rouge.on(); orange.off(); vert.off()
        envoyer_etat()
        time.sleep(3)

        rouge.off(); orange.on(); vert.off()
        envoyer_etat()
        time.sleep(2)

        rouge.off(); orange.off(); vert.on()
        envoyer_etat()
        time.sleep(4)

except KeyboardInterrupt:
    print("Arrêt demandé")
    rouge.off(); orange.off(); vert.off()
    envoyer_etat()  # enverra bb000 pour dire “tout éteint”
