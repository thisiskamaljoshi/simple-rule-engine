from dataclasses import dataclass
from typing import Optional
from logical_operators import LOGICAL_OPERATORS

@dataclass
class ParsedLogicalCondition:
    left_expression: str
    operator: str
    right_expression: str

# parse()

#     │
#     ├── validate_logical_input()
#     │
#     ├── find_logical_operator()
#     │
#     ├── split_logical_condition()
#     │
#     ├── clean_logical_tokens()
#     │
#     ├── validate_logical_variable()
#     │
#     └── return ParsedLogicalCondition

def parseLogicalCondition(condition:str) -> Optional[ParsedLogicalCondition]:
    """
    Parses a logical condition.

    Example:
        Input:
            "fever==True AND cough==True"

        Output:
            ParsedLogicalCondition(
                left_expression="fever==True",
                operator="AND",
                right_expression="cough==True"
            )
    """

    if not validate_logical_input(condition):
        return None

    operator = find_logical_operator(condition)

    left_expression, right_expression = split_logical_condition(condition, operator)

    left_expression, operator , right_expression = clean_logical_tokens(left_expression, operator , right_expression)

    return ParsedLogicalCondition(left_expression, operator, right_expression)



def validate_logical_input(condition: str) -> bool:
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

def find_logical_operator(condition: str) -> Optional[str]:
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

    for operator in LOGICAL_OPERATORS:
        if operator in condition:
            return operator

    return None

def split_logical_condition(condition:str , operator:str) -> tuple[str,str]:
    """
    Splits a rule condition into its left_expression and right_expression components.

    The function separates the condition using the supplied comparison
    operator and returns the left-hand side (left_expression) and right-hand
    side (comparison right_expression).

    Parameters:
        condition (str):
            The rule condition to split.

        operator (str):
            The comparison operator found in the condition.

    Returns:
        tuple[str, str]:
            A tuple containing:
            - left_expression (str)
            - right_expression (str)

    Example:
        Input:
            condition = "marks>=40"
            operator = ">="

        Output:
            ("marks", "40")
    """
    return condition.split(operator,1)
    # This ensures the string is split only once, even if the right_expression were ever to contain the operator.


def clean_logical_tokens(left_expression:str ,operator:str, right_expression:str) -> tuple[str,str]:
    """
    Removes leading and trailing whitespace from the parsed tokens.

    Parameters:
        left_expression (str):
            The parsed variable name.

        right_expression (str):
            The parsed comparison right_expression.

    Returns:
        tuple[str, str]:
            A tuple containing the cleaned left_expression and right_expression.
    """
    return left_expression.strip(), operator.strip() , right_expression.strip()

def validate_logical_variable(variable:str) -> str:
    return variable
