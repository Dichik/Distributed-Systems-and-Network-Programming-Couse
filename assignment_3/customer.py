class Customer(): 
    def __init__(self, name, surname, username, password) -> None:
        self.name = name
        self.surname = surname
        self.username = username
        self.password = password
        self.talks = {}
    
    def addTalk(self, user):
        username = user.getUsername()
        self.talks[username] = []

    def addMessage(self, message, user):
        username = user.getUsername()
        self.talks[username].append(message)

    def getMessage(self, user):
        username = user.getUsername()
        return self.talks[username]
    
    def getUsername(self):
        return self.username