import socket

newsocket = socket.socket()
newsocket.connect(('127.0.0.1', 12345))

print('Message Interpretation:')
print('G: correct digit at the correct position')
print('Y: correct digit at the wrong position')
print('R: wrong digit')
print()

while True:
    data = b''
    while b'\n' not in data:
        data += newsocket.recv(1024)

    data = data.decode().strip()
    if data == 'WIN':
        print('You win!')
        break
    elif data == 'LOSE':
        print('You lose the game!')
        ans = newsocket.recv(1024).decode().strip()
        print("Correct code is:", ans)
        break
    elif data == 'GUESS':
        guess = input('Enter guess (1000-9999):') + '\n'
        newsocket.sendall(guess.encode())
    else:
        print('Your message is:', data)
        print()
newsocket.close()
