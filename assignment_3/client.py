import socket, pickle
from message import Message
from option import Option

import customer as c

MAX = 1064
PORT = 1060

def client_program():
    client = socket.socket()
    hostname = socket.gethostbyname("localhost")
    client.connect((hostname, PORT))
    print ("Client socket name is", client.getsockname())

    isConnected = True
    while isConnected:
        print("options:")
        print("1. register user")
        print("2. create connection")
        print("3. create talk")
        option = int(input("enter 1, 2 or 3: "))
        message = None

        if option == Option.REGISTER.value:
            name = input("enter name: ")
            surname = input("enter surname: ")
            username = input("enter username: ")
            password = input("enter password: ")
            customer = c.Customer(name, surname, username, password)
            ... 
            # save customer
            message = Message(
                Option.REGISTER,
                pickle.dumps(customer)
            )
        elif option == Option.CONNECT.value:
            ...
            # take username and username(2) as input
            # create connection
        elif option == Option.TALK.value:
            ...
            # take username and username(2) as input
            # take message from their conversation (what about simulating real conversation?)
            # create talk between users
        else:
            print("invalid option, please try again")
            continue

        client.send(pickle.dumps(message))
        encoded_data = client.recv(MAX)
        data = pickle.loads(encoded_data)
        if data:
            print("Received from server:", data.__str__())
        else:
            isConnected = False
            print("terminating...")


if __name__ == "__main__":
    client_program()