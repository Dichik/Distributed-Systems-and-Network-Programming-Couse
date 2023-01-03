import socket

MAX = 1024
PORT = 1060

def server_program():
    server = socket.socket()
    hostname = socket.gethostbyname("localhost")
    server.bind((hostname, PORT))

    server.listen()
    print ("Listening at", server.getsockname())

    conn, address = server.accept()
    isConnected = True
    while isConnected:
        data = conn.recv(MAX).decode()
        if data:
            print ("The client at", address, "says:", repr(data))
            message = "test message"
            conn.send(message.encode())
        else:
            isConnected = False
            print ('Pretending to drop packet from', address)
    print('Stop listening...')


if __name__ == "__main__":
    server_program()