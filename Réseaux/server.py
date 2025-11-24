import socket

try:
    print("Démarrage du serveur")

    # définition du socket
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Liaison du socket avec IP et port. Dans le cas d'un serveur on peut
    # laisser l'adresse IP à vide ce qui signifie que toutes les interfaces
    # réseaux sont prises en compte
    s.bind(('',5001))
    # mise en écoute
    s.listen()
    # et attente d'un client
    client,adresse=s.accept()
    print('connecté avec l\'adresse et le port : ',adresse)
    message=""
    while message!='z':
        message=client.recv(1024).decode('utf-8')
        print(message.rstrip())
        resp=client.send(bytes('Bien reçu\\r\\n','utf-8'))
    s.close()
    client.close()

except KeyboardInterrupt:
    s.close()
    client.close()
    exit()
