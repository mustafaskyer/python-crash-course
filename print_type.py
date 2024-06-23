def printtype(param):
    paramType = type(param)
    if isinstance(param, str):
        return "String"
    elif isinstance(param, int):
        return "Int";
    elif isinstance(param, float):
        return "Float"
    else:
        return "Unknown"
print(printtype(1.1))