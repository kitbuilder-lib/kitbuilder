# Reader
from ..reader import Reader

# Environment
from ..environment import Environment

# Meta
from ..meta import Meta

# Function
from ..function import Function

# Factory
from ..factory import Factory

# Constants
from ..constants import (
    GLOBAL_DESC_DEF,
    GLOBAL_ENV_DEF,
    GLOBAL_FUNC_DEF,
    GLOBAL_NAME_DEF,
    GLOBAL_IMPORT_DEF,
    GLOBAL_CONSTRUCT_DEF
)

# Utils
from ..utils import (
    get_type
)

# Error handling
from ..errors import (
    raise_type_error
)

class Parser:
    __content = None

    __meta: Meta = Meta()
    __environment: Environment = Environment()
    __functions: list = []
    __factory: Factory = Factory()
    __construct: list = []

    def __init__(self, filepath:str):
        """ KitBuilder Parser """
        self.__content = Reader().get_content(filepath)

        self.__parse()

    def __parse(self):
        for key in self.__content:
            self.__set_meta(key)
            self.__set_env(key)
            self.__set_imports(key)
            self.__set_construct(key)
            self.__set_functions(key)
        
    def __set_construct(self, key: str) -> None:
        if key == GLOBAL_CONSTRUCT_DEF:
            construct_list = self.__content[key]

            if type(construct_list) != list:
                raise_type_error("Constructor argument", "List", get_type(construct_list))
            
            self.__construct = construct_list

    def __set_functions(self, key: str) -> None:
        if key == GLOBAL_FUNC_DEF:
            funcs_obj = self.__content[key]

            if type(funcs_obj) != dict:
                raise_type_error("Function object", "Object", get_type(funcs_obj))

            for funcs_key in funcs_obj:
                func = funcs_obj[funcs_key]

                if type(func) != dict:
                    raise_type_error("Function", "Object", get_type(func))

                self.__functions.append(Function({ **func, "name": funcs_key }, self.__environment))

    def __set_imports(self, key: str) -> None:
        if key == GLOBAL_IMPORT_DEF:
            import_path = self.__content[key]

            if type(import_path) != str:
                raise_type_error("Import path", str, get_type(import_path))
            
            internal_parser = Parser(import_path)
            
            self.__environment.merge(internal_parser.__environment)
    
    def __set_meta(self, key: str) -> None:
        if key == GLOBAL_NAME_DEF:
            self.__meta.add(key, self.__content[key])
        if key == GLOBAL_DESC_DEF:
            self.__meta.add(key, self.__content[key])

    def __set_env(self, key: str):
        if key == 'environment':
            env_obj = self.__content[key]

            if type(env_obj) != dict:
                raise_type_error("Environment object", "Object", get_type(env_obj))

            for env_key in env_obj:
                env_val = env_obj[env_key]

                if type(env_val) != str:
                    raise_type_error("Environment value", "String", get_type(env_val))

                self.__environment.add(env_key, env_val)

    def build(self):
        Production = self.__factory.produce(
            environment=self.__environment,
            meta=self.__meta,
            constructor=self.__construct,
            functions=self.__functions
        )
        
        return Production
