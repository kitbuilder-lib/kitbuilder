def raise_type_error(entity: str, expected_type: str, received_type: str):
    raise TypeError(f"{entity} defintion type is invalid. Expected {expected_type}, received {received_type}")

def raise_required_error(entity: str):
    raise Exception(f"Missing required {entity} key")

def raise_invalid_variable(var: str):
    raise Exception(f"Variable: {var} not found.")

def raise_missing_argument(key: str):
    raise TypeError(f"Expected {key} argument")

def raise_invalid_name(key: str):
    raise Exception(f"Invalid function name: {key}")

def raise_invalid_argument(key: str):
    raise Exception(f"Invalid argument found: {key}")
