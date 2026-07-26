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