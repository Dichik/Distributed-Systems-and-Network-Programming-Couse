import socket, pickle

from entities.message import Message
from entities.option import Option
from entities.talk import Talk
from entities.connection import Connection
from entities.customer import Customer

MAX = 1024
PORT = 1060

def server_program():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    hostname = socket.gethostbyname("localhost")
    server.bind((hostname, PORT))

    server.listen()
    print ("Listening at", server.getsockname())
    database = {} # storage for customers

    conn, address = server.accept()
    isConnected = True
    while isConnected:
        encoded_data = conn.recv(MAX)
        data: Message = pickle.loads(encoded_data)
        if data:
            option = data.get_option()

            if option == Option.REGISTER:
                obj: Customer = pickle.loads(data.get_obj())
                username = obj.get_username()
                database[username] = obj
            elif option == Option.CONNECT:
                obj: Connection = pickle.loads(data.get_obj())
                from_username = obj.get_from()
                to_username = obj.get_to()
                database[from_username].add_talk(to_username)
            elif option == Option.TALK:
                obj: Talk = pickle.loads(data.get_obj())
                from_username = obj.get_from()
                to_username = obj.get_to()
                talk = obj.get_talk()
                database[from_username].add_message(to_username, talk)

            print ("The client at", address, "says something")
            message = "test message"
            conn.send(message.encode())
        else:
            isConnected = False
            print ('Pretending to drop packet from', address)
    print('Stop listening...')


if __name__ == "__main__":
    server_program()