import socket
import threading

io = socket.socket()
io.bind(('127.0.0.1', 4069))
io.listen()
msg = ''


def handle(msg, new_io):
    msg = list((reversed(msg.decode())))
    for i in range(len(msg)):
        if msg[i].isupper():
            msg[i] = msg[i].lower()
        elif msg[i].islower():
            msg[i] = msg[i].upper()
    new_io.sendall(''.join(msg).encode('utf-8'))


while True:
    new_io, addr = io.accept()
    print('Connected by', addr)
    msg = new_io.recv(1024)
    if msg != b'Bye':
        thread = threading.Thread(target=handle, args=(msg, new_io))
        thread.start()
    else:
        new_io.close()
        io.close()
