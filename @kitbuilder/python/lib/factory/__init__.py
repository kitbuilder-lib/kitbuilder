# Constants
from ..constants import (
    FUNCTION_NAME_DEF,
    FUNCTION_CLI_TYPE,
    FUNCTION_TYPE_DEF,
    GLOBAL_DESC_DEF,
    GLOBAL_NAME_DEF
)

# Meta
from ..meta import Meta

# Environment
from ..environment import Environment

# Utils
from ..utils import (
    parse_args
)

class Factory:
    __environment: Environment = {}

    def __define_functions(self, functions: list):
        defined = {}

        for function in functions:
            definition = function.get()

            defined[definition[FUNCTION_NAME_DEF]] = function.build()

        return defined

    def produce(self, functions: list, meta: Meta, environment: Environment, constructor: list):
        self.__environment = environment

        metadata = meta.get()

        definitions = self.__define_functions(functions)

        def __init__(self, *args, **kwargs):
            arguments = parse_args(constructor, args, kwargs)

            for arg in arguments:
                setattr(self, arg, arguments[arg])

        Production = type(
            metadata[GLOBAL_NAME_DEF],
            (object,),
            {
                "__init__": __init__,
                "__doc__": metadata[GLOBAL_DESC_DEF],
                **definitions
            }
        )

        return Production
