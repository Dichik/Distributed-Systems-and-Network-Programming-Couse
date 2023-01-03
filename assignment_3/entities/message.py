

from entities.option import Option


class Message:
    def __init__(self, option: Option, obj) -> None:
        self.option = option
        self.obj = obj
    
    def getOption(self) -> Option:
        return self.option

    def getObj(self):
        return self.obj