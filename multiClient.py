__author__ = 'Kyle Haltenhoff'

import socket, threading, time

HOST = '127.0.0.1'
PORT = 36001
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

finished = False

startingMessage = s.recv(1024)
print repr(startingMessage)

threadID = s.recv(1024)
print 'Client Number: ', repr(threadID)

while not finished:

    echo = raw_input('What message do you wish to send? ')

    if echo == 'quit':

        finished = True
        s.close()

    else:

        s.sendall(echo)
        data = s.recv(1024)

        print 'Message Sent: ', echo
        print 'Message Received: ', repr(data)
