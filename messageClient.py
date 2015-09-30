__author__ = 'Kyle Haltenhoff'

import socket

HOST = '127.0.0.1'
PORT = 36002

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

done = False

openingMessage = s.recv(1024)
print repr(openingMessage)

ThreadID = s.recv(1024)
print 'Thread ID: ', repr(ThreadID)

while not done:

    echo = raw_input('What message do you wish to send? ')
    s.sendall(echo)
    data = s.recv(1024)

    if echo == 'quit':

        done = True
        s.close()

    else:

        print 'Message Sent: ', echo
        print 'Message Received: ', repr(data)