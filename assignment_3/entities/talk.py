from connection import Connection

class Talk(Connection):
    def __init__(self, from_username, to_username, talk) -> None:
        super(from_username, to_username)
        self.talk = talk

    def getTalk(self):
        return self.talk