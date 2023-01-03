# Assignment #3

### Description 

Write a client-server application such that at server side data for registered users is kept (name, surname, username, password). For each user, a list of conversations that they have made with other users is also kept. The conversations are stored in a dictionary where the key is the username of the user with whom the conversation is being made. Add a function to the Customer class for adding a new conversation, and adding a message to an existing conversation.

### User class

To write a class for each user:
```python
class Customer():
    def __init__(self, name, surname ... ):
        self.name, self.surname... = name, surname ...
        self.talks = {}

    def addTalk(self, user):
        ...
    
    def addMessage(self, message, user):
        ...

    def getMessage(self, user):
        ...
```