# Yaml loader
from yaml import safe_load

# Pathlib
from pathlib import Path

class Reader:
    """ File reader """

    def __open_file(self, filepath: str):
        """ Get parsed content from file """
        f = open(filepath, 'r')
        return safe_load(f)

    def get_content(self, filepath: str):
        """ Get content from file """ 
        content = self.__open_file(filepath)

        return content
