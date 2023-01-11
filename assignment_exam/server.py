import socket, random

MAX = 1024
PORT = 1060

def generate_number():
    result = 0
    used = []
    for i in range(0, 4):
        x = random.randint(0, 9)
        while x in used:
            x = random.randint(0, 9)
        result = result * 10 + x
        used.append(x)
    return result

def getSameOnPos(actual, to_guess):
    a = str(actual)
    t = str(to_guess)
    result = 0
    for i in range(0, 4):
        if a[i] is t[i]:
            result += 1
    return str(result)

def getSameOnDiff(actual, to_guess):
    a = str(actual)
    t = str(to_guess)
    result = 0
    for i in range(0, 4):
        if a[i] is not t[i] and t[i] in a:
                result += 1
    return str(result)

def form_hint_message(actual, to_guess):
    return "guessed on the same position: " + getSameOnPos(actual, to_guess) \
         + "\nguessed at all: " + getSameOnDiff(actual, to_guess)

def server_program():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    hostname = socket.gethostbyname("localhost")
    server.bind((hostname, PORT))

    server.listen()
    print ("Listening at", server.getsockname())

    number_to_guess = generate_number()
    tries = 10
    print(number_to_guess)

    conn, address = server.accept()
    isConnected = True
    while isConnected and tries > 0:
        data = conn.recv(MAX).decode()
        print("Received from client:", data)
        if data:
            tries -= 1
            message = None
            if data.isnumeric() and len(data) == 4:
                number = int(data)
                if number == number_to_guess:
                    message = "success"
                else:
                    message = form_hint_message(number, number_to_guess)
            else:
                message = "Please enter number of 4 digits"
            
            conn.send(message.encode())
        else:
            isConnected = False
            print ('Pretending to drop packet from', address)
    print('Stop listening...')


if __name__ == "__main__":
    server_program()