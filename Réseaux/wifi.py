import time
import socket
import network

def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    i = 0
    while not wlan.isconnected():
        print(f"temps d'attente {i}s - Waiting for connection...")
        time.sleep(1)
        i += 1
    print(wlan.ifconfig())
    ip = wlan.ifconfig()[0]
    print(f"Connected on {ip}")
    time.sleep(1)
    return ip

ssid = 'Projet'
password = ''
ip = connect()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = '172.16.12.121'
PORT = 5001
s.connect((HOST, PORT))

message = ''
while message != 'z':
    message = input('Texte à envoyer : ')
    s.send(message.encode())
    print('Message envoyé au serveur')
    print('Attente de la réponse...')
    print('Le serveur a envoyé ', s.recv(1024).decode('utf-8'))

s.send(b'z')
s.shutdown(socket.SHUT_RDWR)
s.close()
