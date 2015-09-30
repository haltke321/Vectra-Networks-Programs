__author__ = 'Kyle Haltenhoff'

import socket, threading

HOST = ''
PORT = 36002

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

print '----------Server Online-------------'

def messageServer(conn, addr, ID):

    print 'Connected by ', str(addr)

    openingMessage = 'Hello Client'
    conn.sendall(openingMessage)

    conn.sendall(str(ID))

    messageFile = open('messages.txt', 'a')

    done = False

    while not done:

        data = conn.recv(1024)

        if data == 'quit':

            done = True
            messageFile.close()
            conn.close()

        else:

            conn.sendall(data)
            messageFile.write(addr[0] + ": " + data + '\n')


i = 1

while True:

    conn, addr = s.accept()
    threading.Thread(target=messageServer, args=(conn, addr, i)).start()
    i+=1