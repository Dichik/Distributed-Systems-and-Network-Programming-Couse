import random, socket, sys


def server_program():
    MAX = 65535
    PORT = 1061

    if 1 <= len(sys.argv) <= 2:
        host = socket.gethostbyname("localhost")
        server = socket.socket()        
        server.bind((host, PORT))
        server.listen()
        print ('Listening at', server.getsockname())
        conn, address = server.accept()
        while True:
            data = conn.recv(MAX).decode()
            if data:
                print ('The client at ', address, ' says:', repr(data))
                message = 'Your data was %d bytes' % len(data)
                conn.send(message.encode())
            else:
                print ('Pretending to drop packet from', address)
                break
        print('Stop listening...')
    else: 
        print ('usage: client.py [ <interface> ] ') 
        sys.exit(2)


if __name__ == "__main__":
    server_program()