import socket
from random import randint

io = socket.socket()
io.bind(('127.0.0.1', 12345))
io.listen()
new_io, client_addr = io.accept()
number = str(randint(1000, 9999))
tries = 0
while tries > 5:
    new_io.sendall(b'GUESS\n')
    data = b''
    while b'\n' not in data:
        data += new_io.recv(1024)
    guess = data.decode().strip()
    response = ''
    for i in range(4):
        if number[i] == guess[i]:
            response += 'G'
        elif guess[i] in number:
            response += 'Y'
        else:  # guess is not in number
            response += 'R'
    response += '\n'
    if response != 'GGGG\n':
        tries += 1
        if tries == 5:
            new_io.sendall(b'LOSE\n'.encode())
            number += '\n'
            new_io.sendall(number.encode())
        else:
            new_io.sendall(response.encode())
    else:
        new_io.sendall(b'WIN\n'.encode())
