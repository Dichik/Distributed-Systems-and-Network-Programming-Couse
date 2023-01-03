

class Connection:
    def __init__(self, from_username, to_username) -> None:
        self.from_username = from_username
        self.to_username = to_username

    def get_from(self):
        return self.from_username

    def get_to(self):
        return self.to_username