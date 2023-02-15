# Regex
from re import findall

# Literal eval
from ast import literal_eval

# Errors
from ..errors import (
    raise_missing_argument,
    raise_invalid_variable
)

# Constants
from ..constants import (
    VARIABLE_FINDER_REGEX,
    VARIABLE_OPEN_TOKEN,
    VARIABLE_CLOSE_TOKEN
)
def index_dict(obj: dict, index: str):
    list_ = findall(r'\["*(.*?)"*\]', index)

    for k in list_:
        if k.isdigit() and isinstance(obj, list):
            obj = obj[int(k)]
        else:
            obj = obj.get(k)
        if obj is None:
            break
        
    return obj

def get_type(obj):
    return str(type(obj).__name__).capitalize()

def parse_args(__args, args, kwargs):    
    if len(args) != len(__args):
        for key in __args:
            if key not in kwargs:
                raise_missing_argument(key)
        
        return kwargs

    parsed_args = {}

    for key in __args:
        for arg_key in args:
            parsed_args[key] = arg_key

    return parsed_args

def apply_args(arg_source: dict, obj):
    string = str(obj)

    matches = findall(VARIABLE_FINDER_REGEX, string)

    if matches:
        for index, match in enumerate(matches):
            full_variable = VARIABLE_OPEN_TOKEN + match + VARIABLE_CLOSE_TOKEN

            results = index_dict(arg_source, match)

            if not results:
                raise_invalid_variable(full_variable)
            
            string = string.replace(full_variable, str(results))

    if type(obj) == list or type(obj) == dict:
        obj = literal_eval(string)
    else:
        obj = string
    
    return obj
