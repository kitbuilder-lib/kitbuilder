# Parser
from .parser import Parser

class Kit:
    __parser: Parser = None

    def __init__(self, filepath: str):
        self.__parser = Parser(filepath)

    def build(self):
        return self.__parser.build()
