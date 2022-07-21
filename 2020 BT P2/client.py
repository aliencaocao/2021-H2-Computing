import socket

io = socket.socket()
io.connect(('127.0.0.1', 4069))
data = ''
while data != 'You Win!':
    guess = input('Enter guess (A-Z): ')
    io.send(guess.encode() + b'\n')
    data = ''
    while '\n' not in data:
        data += io.recv(1024).decode()
    data = data.strip()
    print(data)
io.close()