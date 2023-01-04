

class Customer: 
    def __init__(self, name, surname, username, password) -> None:
        self.name = name
        self.surname = surname
        self.username = username
        self.password = password
        self.talks = {}
    
    def add_talk(self, username) -> None:
        self.talks[username] = []

    def add_message(self, username, message) -> None:
        self.talks[username].append(message)

    def get_message(self, username):
        return self.talks[username]
    
    def get_username(self):
        return self.username

    def __str__(self) -> str:
        return "\nName: " + self.name \
                + "\nSurname: " + self.surname \
                + "\nUsername: " + self.password