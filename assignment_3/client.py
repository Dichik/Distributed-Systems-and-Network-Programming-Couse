import socket

MAX = 1064
PORT = 1060

def client_program():
    client = socket.socket()
    hostname = socket.gethostbyname("localhost")
    client.connect((hostname, PORT))
    print ("Client socket name is", client.getsockname())

    isConnected = True
    while isConnected:
        message = input("enter message ->")
        client.send(message.encode())
        data = client.recv(MAX).decode()
        if data:
            print("Received from server:", data)
        else:
            isConnected = False
            print("terminating...")


if __name__ == "__main__":
    client_program()