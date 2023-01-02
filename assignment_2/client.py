import socket, sys


def client_program():
    if 1 <= len(sys.argv) <= 2:
        host = sys.argv[1] if len(sys.argv) > 1 else socket.gethostbyname("localhost")
        PORT = 1061
        MAX = 65535

        client_socket = socket.socket()
        client_socket.connect((host, PORT))
        print ('Client socket name is', client_socket.getsockname())

        message = 'let\'s begin' 
        delay = 0.1
        while message.lower().strip() != 'bye':
            client_socket.send(message.encode())
            client_socket.settimeout(delay)
            
            try:
                data = client_socket.recv(MAX).decode()
            except socket.timeout:
                delay *= 2 # wait even longer for the next request
                if delay > 2.0:
                    raise RuntimeError('I think the server is down')
                print('Received from server: ' + data)
            except:
                raise
            else:
                print ('The server says', repr(data))
            message = input("enter your answer -> ")

        client_socket.close()
    else:
        print ('usage: python client.py [ <interface> ] ') 
        sys.exit(2)


if __name__ == '__main__':
    client_program()