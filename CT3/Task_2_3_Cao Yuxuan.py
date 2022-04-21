import socket
import pymongo
import threading

conn = pymongo.MongoClient('127.0.0.1', 27017)
moviedb = conn['movieDB']
movie_coll = moviedb['movie']

io = socket.socket()
io.bind(('127.0.0.1', 4069))
io.listen()
msg = ''


def handle(msg, new_io):
    result = movie_coll.find({'Title': msg.decode('utf-8')})
    for i in result:
        new_io.sendall(f'Title: {i["Title"]}, Year: {i["Year"]}, Rated: {i["Rated"]}, Rating: {i["Rating"]}, Runtime: {i["Runtime"]}'.encode('utf-8'))


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
