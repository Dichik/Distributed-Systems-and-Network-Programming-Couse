import socket, pickle

from entities.message import Message

MAX = 1024
PORT = 1060

def server_program():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    hostname = socket.gethostbyname("localhost")
    server.bind((hostname, PORT))

    server.listen()
    print ("Listening at", server.getsockname())

    conn, address = server.accept()
    isConnected = True
    while isConnected:
        encoded_data = conn.recv(MAX)
        data: Message = pickle.loads(encoded_data)
        if data:
            option = data.getOption()
            obj = data.getObj()
            print(option.value)
            print ("The client at", address, "says something")
            message = "test message"
            conn.send(pickle.dumps(message))
        else:
            isConnected = False
            print ('Pretending to drop packet from', address)
    print('Stop listening...')


if __name__ == "__main__":
    server_program()