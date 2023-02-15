import keyword

# Definitions
FUNCTION_TYPE_DEF = "type"
FUNCTION_ARGS_DEF = "args"
FUNCTION_CONFIG_DEF = "config"
FUNCTION_NAME_DEF = "name"
GLOBAL_NAME_DEF = "name"
GLOBAL_DESC_DEF = "description"
GLOBAL_ENV_DEF = "environment"
GLOBAL_FUNC_DEF = "functions"
GLOBAL_IMPORT_DEF = "import"
GLOBAL_CONSTRUCT_DEF = "construct"

# Function name whitelist
FUNCTION_NAME_WHITELIST = keyword.kwlist

# Function types
FUNCTION_CLI_TYPE = "cli"
FUNCTION_REQUEST_TYPE = "request"

# Special tokens
VARIABLE_OPEN_TOKEN = "%{{"
VARIABLE_CLOSE_TOKEN = "}}%"
FUNCTION_NAME_INVALID_TOKEN = "__"

# Regex definitions
VARIABLE_FINDER_REGEX = f"(?<=\\{VARIABLE_OPEN_TOKEN})(.*?)(?={VARIABLE_CLOSE_TOKEN})"
