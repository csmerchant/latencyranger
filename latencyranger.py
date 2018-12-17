import socket
import sys
from threading import Thread

#defining important variables for connections to the gameservers & other sockets
gamesocket = None #we get the game socket once we connect to the gameserver
sockhost = '0.0.0.0' #0.0.0.0 by default
