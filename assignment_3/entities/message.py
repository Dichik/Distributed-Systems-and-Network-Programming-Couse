

from entities.option import Option


class Message:
    def __init__(self, option: Option, obj) -> None:
        self.option = option
        self.obj = obj
    
    def get_option(self) -> Option:
        return self.option

    def get_obj(self):
        return self.obj