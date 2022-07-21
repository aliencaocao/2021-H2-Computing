import socket
import string
import random
import threading

io = socket.socket()
io.bind(('127.0.0.1', 4069))
io.listen()


def handle(client_socket):
    print('Connection from', client_socket)
    letter = random.choice(string.ascii_uppercase)
    print(letter)
    guess = ''
    while guess != letter:
        guess = ''
        while '\n' not in guess:
            guess += client_socket.recv(1024).decode()
        guess = guess.strip()
        if guess == letter:
            client_socket.send(b'You Win!\n')
        else:
            hint = b'The answer is before your letter.\n' if guess > letter else b'The answer is after your letter.\n'
            client_socket.send(hint)
    client_socket.close()


while True:
    client_socket, client_address = io.accept()
    threading.Thread(target=handle, args=(client_socket,)).start()
    io.close()
    exit()
