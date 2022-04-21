import socket

msg = ''
while msg != 'Bye':
    msg = input('Enter a message: ')
    if msg != 'Bye':
        io = socket.socket()
        io.connect(('127.0.0.1', 4069))
        io.sendall(msg.encode())
        r = io.recv(1024)
        print(r.decode())
io.close()
exit()
