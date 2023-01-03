import socket, pickle


from entities.message import Message
from entities.option import Option
from entities.connection import Connection
from entities.customer import Customer
from entities.talk import Talk

MAX = 1064
PORT = 1060

def handle_register_option() -> Message:
    name = input("enter name: ")
    surname = input("enter surname: ")
    username = input("enter username: ")
    password = input("enter password: ")

    customer = Customer(name, surname, username, password)
    return Message(
        Option.REGISTER,
        pickle.dumps(customer)
    )

def handle_connect_option() -> Message:
    from_username = input("enter from_username: ")
    to_username = input("enter to_username: ")

    connection = Connection(from_username, to_username)
    return Message(
        Option.CONNECT,
        pickle.dumps(connection)
    )

def handle_talk_option():
    from_username = input("enter from_username: ")
    to_username = input("enter to_username: ")
    talk = input("enter talk: ")

    talk = Talk(from_username, to_username, talk)
    return Message(
        Option.TALK,
        pickle.dumps(talk)
    )

def get_option_from_input():
    print("options:")
    print("1. register user")
    print("2. create connection")
    print("3. create talk")
    option = int(input("enter 1, 2 or 3: "))
    return option

def client_program():
    client = socket.socket()
    hostname = socket.gethostbyname("localhost")
    client.connect((hostname, PORT))
    print ("Client socket name is", client.getsockname())

    isConnected = True
    while isConnected:
        option = get_option_from_input()

        message = None
        if option == Option.REGISTER.value:
            message = handle_register_option()
        elif option == Option.CONNECT.value:
            message = handle_connect_option()
        elif option == Option.TALK.value:
            message = handle_talk_option()
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