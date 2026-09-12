# Problem 3 — Build a Rule Condition Parser

## Problem Statement

Build a parser that evaluates rule conditions written as strings against a collection of facts. Your parser should behave like the condition evaluation part of a simple rule-based expert system.

Instead of writing hardcoded Python conditions such as:

```python
if facts["marks"] >= 40:
    print("Pass")
```

your program should be able to interpret a condition stored as a string:

```text
marks>=40
```

and determine whether the condition is **True** or **False** by looking up the corresponding value in the `facts` dictionary.

Your parser must support numeric, string, and boolean comparisons while automatically converting the value from the condition into the correct data type before performing the comparison.

---

## Input

A dictionary containing facts.

Example:

```python
facts = {
    "marks": 62
}
```

A condition represented as a string.

```python
condition = "marks>=40"
```

---

## Expected Output

```text
True
```

---

## Another Example

### Input

```python
facts = {
    "marks": 35
}

condition = "marks>=40"
```

### Output

```text
False
```

---

## Functional Requirements

Your parser must:

1. Read the condition string.
2. Identify the variable name.
3. Identify the comparison operator.
4. Identify the comparison value.
5. Retrieve the variable's value from the `facts` dictionary.
6. Convert the comparison value to the same data type as the corresponding fact.
7. Evaluate the condition.
8. Return `True` or `False`.

---

## Supported Comparison Operators

Your parser must support the following operators:

- `>`
- `>=`
- `<`
- `<=`
- `==`
- `!=`

---

## Supported Data Types

Your parser must correctly evaluate conditions involving:

- Integers
- Floating-point numbers
- Strings
- Boolean values

---

## Example Test Cases

### Integer Comparison

```python
facts = {
    "marks": 62
}

condition = "marks>=40"
```

**Output**

```text
True
```

---

```python
facts = {
    "marks": 35
}

condition = "marks>=40"
```

**Output**

```text
False
```

---

### Floating Point Comparison

```python
facts = {
    "temperature": 37.5
}

condition = "temperature>=36.5"
```

**Output**

```text
True
```

---

```python
facts = {
    "temperature": 35.8
}

condition = "temperature>36.5"
```

**Output**

```text
False
```

---

### String Comparison

```python
facts = {
    "country": "India"
}

condition = 'country=="India"'
```

**Output**

```text
True
```

---

```python
facts = {
    "country": "Japan"
}

condition = 'country!="India"'
```

**Output**

```text
True
```

---

### Boolean Comparison

```python
facts = {
    "fever": True
}

condition = "fever==True"
```

**Output**

```text
True
```

---

```python
facts = {
    "cough": False
}

condition = "cough==True"
```

**Output**

```text
False
```

---

## Constraints

- Every condition contains exactly one comparison operator.
- Variable names are guaranteed to exist in the `facts` dictionary.
- Spaces around operators may or may not be present.
- All conditions are syntactically valid.
- The parser must **not** use Python's `eval()` function.
- The parser should determine the appropriate data type using the value stored in the `facts` dictionary rather than hardcoding conversions.

---

## Function Signature

```python
def evaluate(condition, facts):
    pass
```

The function should return:

```python
True
```

or

```python
False
```

depending on whether the condition evaluates successfully.

---

## Challenge

Implement the parser **without using `eval()` or any third-party parsing libraries**. Parse the condition string manually, identify its components, perform the necessary type conversion, and evaluate the condition yourself.

---
---

# Problem 4 — Support Multiple Conditions

## Goal

Extend the rule engine to support evaluating multiple conditions within a single rule.

Instead of evaluating only one condition:

```python
"marks>=40"
```

your engine should be able to evaluate a list of conditions.

---

## Input

```python
facts = {
    "fever": True,
    "temperature": 39
}

rule = {
    "if": [
        "fever==True",
        "temperature>38"
    ],
    "then": "High Fever"
}
```

---

## Expected Output

```text
High Fever
```

---

## Requirements

Your engine should:

1. Evaluate every condition in the `if` list.
2. Return `True` only if **all** conditions evaluate to `True`.
3. Fire the rule by printing the `then` value when every condition passes.

---

## Example

### Input

```python
facts = {
    "fever": True,
    "temperature": 39
}

rule = {
    "if": [
        "fever==True",
        "temperature>38"
    ],
    "then": "High Fever"
}
```

### Output

```text
High Fever
```

---

### Another Example

```python
facts = {
    "fever": True,
    "temperature": 37
}

rule = {
    "if": [
        "fever==True",
        "temperature>38"
    ],
    "then": "High Fever"
}
```

### Output

```text
Rule not satisfied
```

---

# Problem 5 — Support Logical Operators

## Goal

Extend the parser to support logical operators.

---

## Supported Operators

- `AND`
- `OR`

---

## Examples

```text
fever==True AND cough==True
```

```text
age>=18 OR parentConsent==True
```

---

## Example

### Input

```python
facts = {
    "fever": True,
    "cough": True
}

condition = "fever==True AND cough==True"
```

### Output

```text
True
```

---

# Problem 6 (Yet to implement) — Support Parentheses

## Goal

Support grouping expressions using parentheses.

---

## Example

```text
(age>=18 AND citizen==True) OR visa==True
```

---

## Example

### Input

```python
facts = {
    "age": 17,
    "citizen": False,
    "visa": True
}

condition = "(age>=18 AND citizen==True) OR visa==True"
```

### Output

```text
True
```

---

# Problem 7 — Support Nested Expressions

## Goal

Support nested logical expressions containing multiple levels of parentheses.

---

## Example

```text
(
    fever==True
    AND
    (
        cough==True
        OR soreThroat==True
    )
)
```

---

## Example

### Input

```python
facts = {
    "fever": True,
    "cough": False,
    "soreThroat": True
}
```

Condition

```text
(
    fever==True
    AND
    (
        cough==True
        OR soreThroat==True
    )
)
```

### Output

```text
True
```

---

# Suggested Function

```python
def evaluate(condition: str, facts: dict) -> bool:
    pass
```

---

## Example

```python
evaluate("marks>=40", facts)
```

Returns

```text
True
```

---

# Final Goal

Eventually your rule engine should support complete expert-system rules such as:

```python
facts = {
    "fever": True,
    "temperature": 39,
    "cough": True,
    "age": 25
}

rules = [
    {
        "if": [
            "fever==True",
            "temperature>38",
            "cough==True"
        ],
        "then": "Influenza"
    }
]
```

Your engine should automatically print

```text
Influenza
```

without using any hardcoded `if` statements.

---

# Recommended Learning Progression

Build the project iteratively.

7. Evaluate multiple conditions using `all()`.
8. Support logical operators (`AND`, `OR`).
9. Support parentheses.
10. Build an Abstract Syntax Tree (AST) to evaluate nested expressions.

This progression closely mirrors how many interpreters, compilers, and rule engines evolve. They begin by parsing simple expressions and gradually expand the grammar to support increasingly sophisticated language features.

---

## License & Copyright

- **Code:** Licensed under the [MIT License](LICENSE).
- **Architecture Diagrams & Media:** Copyright © 2026 Kamal Joshi. All rights reserved.