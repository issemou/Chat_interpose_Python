# SOCKETS RÉSEAU : SERVEUR
#
# socket
#   bind (ip, port)  127.0.0.1 -> localhost
#   listen
#   accept -> socket / (ip, port)
#   close

# already used

import socket

HOST_IP = "127.0.0.1"
HOST_PORT = 32000

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST_IP, HOST_PORT))
s.listen()

print(f"Attente de connexion sur {HOST_IP}, port {HOST_PORT}...")
connection_socket, client_address = s.accept()
print(f"Connexion établie avec {client_address}")


texte_envoye = "Bonjour"
connection_socket.sendall(texte_envoye.encode())


s.close()
connection_socket.close()