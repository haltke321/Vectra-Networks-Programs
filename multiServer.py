__author__ = 'Kyle Haltenhoff'

import socket, threading, time

HOST = ''
PORT = 36001
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

print '---------Server Online------------'

def server(conn, addr, ID):

    startingMessage = 'Hello Client, how are you?'
    conn.sendall(startingMessage)

    conn.sendall(str(ID))

    print 'Connected by ', str(addr)

    finished = False

    while not finished:

        data = conn.recv(1024)

        if data == "quit":

            finished = True
            conn.close()

        else:

            conn.sendall(data)

i = 1
while True:

    conn, addr = s.accept()
    threading.Thread(target=server, args=(conn, addr, i)).start()

    i+=1