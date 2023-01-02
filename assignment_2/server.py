import random, socket, sys


def server_program():
    MAX = 65535
    PORT = 1061
    questions = dict()
    
    questions[0] = 'what is red?'
    questions[1] = 'what is OOP?'
    questions[2] = 'how to avoid annoying people?'

    if 1 <= len(sys.argv) <= 2:
        host = sys.argv[1] if len(sys.argv) > 1 else socket.gethostbyname("localhost")
        server = socket.socket()        
        server.bind((host, PORT))
        server.listen()
        print ('Listening at', server.getsockname())
        conn, address = server.accept()
        while True:
            data = conn.recv(MAX).decode()
            if data:
                print ('The client at ', address, ' says:', repr(data))
                # message = 'Your data was %d bytes' % len(data)
                message = questions[random.randint(0, len(questions) - 1)]
                conn.send(message.encode())
            else:
                print ('Pretending to drop packet from', address)
                break
        print('Stop listening...')
    else: 
        print ('usage: python server.py [ <interface> ] ') 
        sys.exit(2)


if __name__ == "__main__":
    server_program()