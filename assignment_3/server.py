import socket, pickle

from entities.message import Message
from entities.option import Option

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
            option = data.getOption()
            obj = data.getObj()

            if option == Option.REGISTER:
                username = obj.getUsername()
                database[username] = obj
            elif option == Option.CONNECT:
                from_username = obj.getFrom()
                to_username = obj.getTo()
                database[from_username].addTalk(to_username)
            elif option == Option.TALK:
                from_username = obj.getFrom()
                to_username = obj.getTo()
                talk = obj.getTalk()
                database[from_username].addMessage(to_username, talk)

            print ("The client at", address, "says something")
            message = "test message"
            conn.send(pickle.dumps(message))
        else:
            isConnected = False
            print ('Pretending to drop packet from', address)
    print('Stop listening...')


if __name__ == "__main__":
    server_program()