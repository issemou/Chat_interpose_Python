
import socket

HOST_IP = "127.0.0.1"
HOST_PORT = 32000

s = socket.socket()

print(f"Connexion au serveur {HOST_IP}, port {HOST_PORT}")
try:
    s.connect((HOST_IP, HOST_PORT))
except ConnectionRefusedError:
    print("ERREUR : impossible de se connecter au serveur")
else:
    print("Connecté au serveur")
    s.close()
