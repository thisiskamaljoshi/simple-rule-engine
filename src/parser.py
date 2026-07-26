from dataclasses import dataclass
from typing import Optional
from .operators import OPERATORS

@dataclass
class ParsedCondition:
    variable: str
    operator: str
    value: str

# parse()

#     │
#     ├── validate_input()
#     │
#     ├── find_operator()
#     │
#     ├── split_condition()
#     │
#     ├── clean_tokens()
#     │
#     ├── validate_variable()
#     │
#     ├── validate_value()
#     │
#     └── return ParsedCondition

def parse(condition:str) -> Optional[ParsedCondition]:
    """
    Parses a single rule condition.

    Example:
        Input:
            "marks>=40"

        Output:
            ParsedCondition(
                variable="marks",
                operator=">=",
                value="40"
            )
    """

    if not validate_input(condition):
        return None

    operator = find_operator(condition)

    variable, value = split_condition(condition, operator)

    variable, value = clean_tokens(variable, value)

    return ParsedCondition(variable, operator, value)



def validate_input(condition: str) -> bool:
    """
    Validates the input condition before parsing.

    This function checks that the supplied condition is suitable
    for parsing. Typical validations include:

    - The condition is not None.
    - The condition is a string.
    - The condition is not empty.
    - The condition is not composed solely of whitespace.

    Parameters:
        condition (str):
            The rule condition to validate.

    Returns:
        bool:
            True if the input passes validation,
            otherwise False.

    """

    if isinstance(condition, str) and condition.strip():
        return True
    else:
        return False

def find_operator(condition: str) -> Optional[str]:
    """
    Finds the comparison operator in a rule condition.

    The function searches the condition for one of the supported
    comparison operators and returns the first matching operator.

    Parameters:
        condition (str):
            The condition to search.

    Returns:
        str | None:
            The detected operator if one exists;
            otherwise None.
    """

    for operator in OPERATORS:
        if operator in condition:
            return operator

    return None

def split_condition(condition:str , operator:str) -> tuple[str,str]:
    """
    Splits a rule condition into its variable and value components.

    The function separates the condition using the supplied comparison
    operator and returns the left-hand side (variable) and right-hand
    side (comparison value).

    Parameters:
        condition (str):
            The rule condition to split.

        operator (str):
            The comparison operator found in the condition.

    Returns:
        tuple[str, str]:
            A tuple containing:
            - variable (str)
            - value (str)

    Example:
        Input:
            condition = "marks>=40"
            operator = ">="

        Output:
            ("marks", "40")
    """
    return condition.split(operator,1)
    # This ensures the string is split only once, even if the value were ever to contain the operator.


def clean_tokens(variable:str ,value:str) -> tuple[str,str]:
    """
    Removes leading and trailing whitespace from the parsed tokens.

    Parameters:
        variable (str):
            The parsed variable name.

        value (str):
            The parsed comparison value.

    Returns:
        tuple[str, str]:
            A tuple containing the cleaned variable and value.
    """
    return variable.strip(), value.strip()

def validate_variable(variable:str) -> str:
    return variable

def validate_value(value:str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in ("'",'"'):
        return value[1:-1]
    return value
