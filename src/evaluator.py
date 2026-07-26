from .parser import parse
from typing import Any

# evaluate()
#       │
#       ├── parser.parse()
#       │
#       ├── lookup fact
#       │
#       ├── convert datatype
#       │
#       ├── execute operator
#       │
#       └── return True/False
# facts = {
#     "marks": 62
# }

def lookup_fact(facts:dict,variable:str) -> Any:
    """
    Retrieves the value associated with a variable from the facts dictionary.

    Parameters:
        facts (dict):
            The dictionary containing all available facts.

        variable (str):
            The variable name to look up.

    Returns:
        Any:
            The value associated with the variable.
    """
    return facts[variable] 

def convert_user_value(user_value:Any,comparison_value:Any) -> Any:
    datatype_of_value = type(user_value)

    if datatype_of_value == int:
        return int(comparison_value)
    elif datatype_of_value == float:
        return float(comparison_value)
    elif datatype_of_value == bool:
        if comparison_value.lower() == "true":
            return True
        elif comparison_value.lower() == "false":
            return False
    elif datatype_of_value == str:
        return str(comparison_value)

    return comparison_value

def compare_values(user_value:Any,curr_op:str,check_value:Any) -> bool:
    if curr_op == "<=":
        return user_value <= check_value
    elif curr_op == ">=":
        return user_value >= check_value
    elif curr_op == "==":
        return user_value == check_value
    elif curr_op == "!=":
        return user_value != check_value
    elif curr_op == "<":
        return user_value < check_value
    elif curr_op == ">":
        return user_value > check_value 

# evaluate("marks>=40", facts)

def evaluate(condition:str,facts:dict) -> bool:
    parsed = parse(condition)
    user_value = lookup_fact(facts,parsed.variable)
    check_value = convert_user_value(user_value , parsed.value) 
    return compare_values(user_value,parsed.operator,check_value)
    