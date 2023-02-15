# Regex
from re import findall

# Utils
from ..utils import (
    index_dict
)

# OS
from os import (
    popen
)

# Requests
from requests import (
    request
)

# Constants
from ..constants import (
    VARIABLE_FINDER_REGEX,
    VARIABLE_OPEN_TOKEN,
    VARIABLE_CLOSE_TOKEN,
    GLOBAL_ENV_DEF,
    GLOBAL_CONSTRUCT_DEF,
    FUNCTION_ARGS_DEF
)

# Utils
from ..utils import (
    parse_args,
    apply_args
)

# Error handling
from ..errors import (
    raise_invalid_variable,
    raise_missing_argument
)

class FunctionBase:
    config: dict = {}
    environment = None
    args = None

    def __init__(self, config: dict, args: list, environment):
        self.config = config
        self.args = args
        self.environment = environment

    def parse_arguments(self, class_instance, args, kwargs):
        parsed_args = parse_args(self.args, args, kwargs)

        arg_source = {}
        arg_source[FUNCTION_ARGS_DEF] = parsed_args
        arg_source[GLOBAL_ENV_DEF] = self.environment
        arg_source[GLOBAL_CONSTRUCT_DEF] = class_instance.__dict__

        for key, value in self.config.items():
            self.config[key] = apply_args(arg_source, value)

    def define(self):
        pass

class CLIFunctionBase(FunctionBase):
    def define(self):
        def executor(instance, *args, **kwargs):
            self.parse_arguments(instance, args, kwargs)
            
            return popen(**self.config).read()

        return executor

class RequestFunctionBase(FunctionBase):
    def define(self):
        def executor(instance, *args, **kwargs):
            self.parse_arguments(instance, args, kwargs)

            return request(**self.config)

        return executor
