import socket

MAX = 1064
PORT = 1060

def is_exit(message):
    return message == 'q' or message == 'quit'

def client_program():
    client = socket.socket()
    hostname = socket.gethostbyname("localhost")
    client.connect((hostname, PORT))
    print ("Client socket name is", client.getsockname())
    print("Running on port", PORT)

    while True:
        message = input("guess number: ")
        if is_exit(message):
            break
        client.send(message.encode())
        data = client.recv(MAX).decode()
        if data:
            print("Received from server:", data)
            if data == "success":
                break


if __name__ == "__main__":
    client_program()