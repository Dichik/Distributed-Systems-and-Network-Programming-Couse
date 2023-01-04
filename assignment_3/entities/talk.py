from entities.connection import Connection

class Talk(Connection):
    def __init__(self, from_username, to_username, talk) -> None:
        super().__init__(from_username, to_username)
        self.talk = talk

    def get_talk(self):
        return self.talk