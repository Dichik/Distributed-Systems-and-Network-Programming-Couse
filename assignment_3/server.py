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
            message = None
            if option == Option.REGISTER:
                obj: Customer = pickle.loads(data.get_obj())
                username = obj.get_username()
                database[username] = obj
                if username not in database.keys():
                    message = "username is not valid, please register"
                else:
                    message = "user was registered successfully"
            elif option == Option.CONNECT:
                obj: Connection = pickle.loads(data.get_obj())
                from_username = obj.get_from()
                to_username = obj.get_to()
                if from_username not in database.keys() \
                    or to_username not in database.keys():
                    message = "specify correctly both usernames"
                else:
                    database[from_username].add_talk(to_username)
                    message = "connection was created successfully"
            elif option == Option.CREATE_TALK:
                obj: Talk = pickle.loads(data.get_obj())
                from_username = obj.get_from()
                to_username = obj.get_to()
                talk = obj.get_talk()
                if from_username not in database.keys() \
                    or to_username not in database.keys():
                    message = "specify correctly both usernames"
                else:
                    database[from_username].add_message(to_username, talk)
                    message = "message was added successfully"
            elif option == Option.GET_TALK:
                obj: Connection = pickle.loads(data.get_obj())
                from_username = obj.get_from()
                to_username = obj.get_to()

                if from_username not in database.keys() \
                    or to_username not in database.keys():
                    message = "specify correctly both usernames"
                else:
                    message = database[from_username].get_message(to_username)
            
            conn.send(message.encode())
        else:
            isConnected = False
            print ('Pretending to drop packet from', address)
    print('Stop listening...')


if __name__ == "__main__":
    server_program()