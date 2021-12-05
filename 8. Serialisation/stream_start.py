"""Streaming pickle example"""
import pickle

#u lieu d'écrire un client et un serveur, nous allons utiliser la paire de sockets, 
# qui crée deux sockets connectés
from socket import socketpair

from moves import move1, move2, move3, move4

#Creation des deux sockets connectés: une pour l'ecriture, une autre pr la lecture

# Serialize

# De-serialize