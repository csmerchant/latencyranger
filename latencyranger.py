import socket
import sys
from threading import Thread

#defining important variables for connections to the gameservers & other sockets
gamesocket = None #we get the game socket once we connect to the gameserver
sockhost = '0.0.0.0' #0.0.0.0 by default
sockport = 3074 #port 3074 by default, change to whatever port you'd like
tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #tcp socket
tcpconn = tcpsock.connect((sockhost, sockport)) #tcp socket connector
