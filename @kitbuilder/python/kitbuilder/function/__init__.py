# Environment
from ..environment import Environment

# Bases
from ..bases import (
    CLIFunctionBase,
    RequestFunctionBase
)

# Constants
from ..constants import (
    FUNCTION_REQUEST_TYPE,
    FUNCTION_CLI_TYPE,
    FUNCTION_TYPE_DEF,
    FUNCTION_ARGS_DEF,
    FUNCTION_CONFIG_DEF,
    FUNCTION_NAME_WHITELIST,
    FUNCTION_NAME_DEF,
    VARIABLE_FINDER_REGEX,
    FUNCTION_NAME_INVALID_TOKEN
)

# Regex
from re import search

# Utils
from ..utils import (
    get_type
)

# Error handling
from ..errors import (
    raise_type_error,
    raise_required_error,
    raise_invalid_name
)

class Function:
    __input: dict = {}

    __type: str = None
    __args: list = []
    __config: dict = {}
    __name: str = None
    __environment = {}

    def __init__(self, func, env):
        self.__environment = env.list_all()
        self.__parse(func)

    def get(self):
        func = {}
        
        func[FUNCTION_NAME_DEF] = self.__name
        func[FUNCTION_ARGS_DEF] = self.__args
        func[FUNCTION_CONFIG_DEF] = self.__config
        func[FUNCTION_TYPE_DEF] = self.__type

        return func

    def __parse(self, func: dict)->None:
        self.__input = func
        for key in func:
            self.__validate_required(key)
            self.__validate_type(key)
            self.__parse_args(key)
            self.__parse_config(key)
            self.__parse_name(key)

    def __parse_name(self, key: str) -> None:
        if key == FUNCTION_NAME_DEF:
            func_name = self.__input[key]
        
            if func_name in FUNCTION_NAME_WHITELIST or func_name.startswith(FUNCTION_NAME_INVALID_TOKEN):
                raise_invalid_name(func_name)

            self.__name = func_name

    def __parse_config(self, key: str) -> None:
        if key == FUNCTION_CONFIG_DEF:
            config_obj = self.__input[key]

            if type(config_obj) != dict:
                raise_type_error("Configuration", "Object", get_type(config_obj))

            self.__config = config_obj

    def __parse_args(self, key: str) -> None:
        if key == FUNCTION_ARGS_DEF:
            args_list = self.__input[key]

            if type(args_list) != list:
                raise_type_error("Argument list", "List/Array", get_type(args_list))

            self.__args = args_list

    def __validate_required(self, key: str) -> None:
        if key not in [FUNCTION_ARGS_DEF, FUNCTION_TYPE_DEF, FUNCTION_NAME_DEF, FUNCTION_CONFIG_DEF]:
            raise_required_error("function")

    def __validate_type(self, key: str) -> None:
        if key == FUNCTION_TYPE_DEF:
            function_type = self.__input[key].lower()

            if type(function_type) != str or function_type not in [FUNCTION_CLI_TYPE, FUNCTION_REQUEST_TYPE]:
                raise_type_error("Function type", "String", get_type(function_type))

            self.__type = function_type

    def build(self):
        f_base = None
    
        if self.__type == FUNCTION_CLI_TYPE:
            f_base = CLIFunctionBase(self.__config, self.__args, self.__environment)
        
        if self.__type == FUNCTION_REQUEST_TYPE:
            f_base = RequestFunctionBase(self.__config, self.__args, self.__environment)
        
        return f_base.define()
