# Interactive Live-Coding Workshop Facilitator Guide: Building a Rule Engine AST Parser
**Project:** SimpleRuleEngine (`simple-rule-engine`)  
**Workshop Title:** *Zero to Parser: Build an AST-Driven Rule Engine in 60 Minutes*  
**Audience:** Python Developers, Backend Engineers, CS Students  
**Duration:** 60-Minute Masterclass + Three 30-Minute Deep-Dive Labs  

---

## 1. Attendee Prerequisites & Setup

### Environment Requirements
- Python 3.10+ (requires modern type union syntax `int | float` and `dataclasses`)
- Modern terminal (PowerShell, Bash, or Zsh)
- Text Editor / IDE (VS Code, PyCharm, or Neovim)

### 5-Minute Pre-Workshop Terminal Setup
Attendees run the following commands in their terminal before the session begins:

```bash
# 1. Clone the repository
git clone https://github.com/thisiskamaljoshi/simple-rule-engine.git
cd simple-rule-engine

# 2. Create and activate a clean virtual environment
python -m venv .venv

# Windows (PowerShell)
.venv\Scripts\Activate.ps1
# Linux / macOS
source .venv/bin/activate

# 3. Install testing and linting tools
pip install pytest pytest-cov ruff mypy

# 4. Verify installation
python -c "import pytest; print('Environment Ready!')"
```

### Starter Repository Layout
Attendees should start with a clean package structure under `src/simple_rule_engine/`:

```text
simple-rule-engine/
├── pyproject.toml
├── src/
│   └── simple_rule_engine/
│       ├── __init__.py
│       ├── tokens.py        <-- Milestone 1
│       ├── lexer.py         <-- Milestone 1
│       ├── ast_nodes.py     <-- Milestone 2
│       ├── parser.py        <-- Milestones 2 & 3
│       ├── evaluator.py     <-- Milestone 4
│       ├── engine.py        <-- Milestone 4
│       └── exceptions.py    <-- Shared
└── tests/
    └── test_rule_engine.py
```

---

## 2. Masterclass Code-Along Blueprint (60 Minutes)

```mermaid
timeline
    title 60-Minute Masterclass Roadmap
    00:00 - 00:15 : Milestone 1 : Lexing & Tokenization
    00:15 - 00:30 : Milestone 2 : AST Nodes & Relational Parser
    00:30 - 00:45 : Milestone 3 : Precedence Climbing & Parentheses
    00:45 - 01:00 : Milestone 4 : Evaluator, Type Coercion & Engine
```

---

### Milestone 1 (00:00–00:15): Lexing & Tokenization

#### Core Concept
Transforming raw text strings into an unambiguous stream of strongly typed tokens. Handling whitespace stripping, string literals with quotes, multi-character comparison operators (`>=`, `<=`, `==`, `!=`), and boolean/keyword detection.

#### Exact Classes & Functions to Code Live
1. `TokenType` Enum and `Token` Dataclass in `tokens.py`.
2. `Lexer` class with `tokenize()`, `_read_string()`, `_read_number()`, and `_match_comparison_operator()` in `lexer.py`.

#### Live Code Walkthrough
```python
# src/simple_rule_engine/tokens.py
from enum import Enum, auto
from dataclasses import dataclass
from typing import Any

class TokenType(Enum):
    IDENTIFIER = auto()
    NUMBER = auto()
    STRING = auto()
    BOOLEAN = auto()
    COMPARISON_OP = auto()
    LOGICAL_OP = auto()
    LPAREN = auto()
    RPAREN = auto()
    EOF = auto()

@dataclass(frozen=True)
class Token:
    type: TokenType
    value: Any
    position: int
```

#### Interactive Checkpoint #1 (Run in REPL)
Attendees execute the following command to verify their Lexer:

```python
from simple_rule_engine.lexer import Lexer
from simple_rule_engine.tokens import TokenType

tokens = Lexer("marks >= 40 AND passed == True").tokenize()
assert len(tokens) == 8
assert tokens[0].type == TokenType.IDENTIFIER and tokens[0].value == "marks"
assert tokens[1].type == TokenType.COMPARISON_OP and tokens[1].value == ">="
assert tokens[2].type == TokenType.NUMBER and tokens[2].value == 40
assert tokens[3].type == TokenType.LOGICAL_OP and tokens[3].value == "AND"
assert tokens[4].type == TokenType.IDENTIFIER and tokens[4].value == "passed"
assert tokens[5].type == TokenType.COMPARISON_OP and tokens[5].value == "=="
assert tokens[6].type == TokenType.BOOLEAN and tokens[6].value is True
assert tokens[7].type == TokenType.EOF
print(" Milestone 1 Verified: Lexer works perfectly!")
```

---

### Milestone 2 (00:15–00:30): AST Nodes & Relational Comparison Parsing

#### Core Concept
Moving beyond flat regexes to hierarchical tree data structures. Designing immutable AST nodes and implementing a single-clause comparison parser.

#### Exact Classes & Functions to Code Live
1. `ASTNode`, `LiteralNode`, `ComparisonNode` in `ast_nodes.py`.
2. `Parser` skeleton with `_consume()`, `_match()`, and `_parse_comparison_or_grouped()` in `parser.py`.

#### Live Code Walkthrough
```python
# src/simple_rule_engine/ast_nodes.py
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

class ASTNode(ABC):
    pass

@dataclass(frozen=True)
class LiteralNode(ASTNode):
    value: Any

@dataclass(frozen=True)
class ComparisonNode(ASTNode):
    variable: str
    operator: str
    target_value: LiteralNode
```

#### Interactive Checkpoint #2 (Run in REPL)
Attendees execute the following command to verify their Comparison Parser:

```python
from simple_rule_engine.parser import Parser
from simple_rule_engine.ast_nodes import ComparisonNode, LiteralNode

ast = Parser.from_text("temperature > 37.5")
assert isinstance(ast, ComparisonNode)
assert ast.variable == "temperature"
assert ast.operator == ">"
assert ast.target_value == LiteralNode(37.5)
print(" Milestone 2 Verified: Comparison Parsing and AST Nodes functioning!")
```

---

### Milestone 3 (00:30–00:45): Precedence Climbing & Parenthesized Expressions

#### Core Concept
Implementing Recursive Descent to parse nested boolean logic (`AND`, `OR`) while enforcing standard operator precedence (`()` binds tighter than relational ops, which bind tighter than `AND`, which binds tighter than `OR`).

#### Exact Classes & Functions to Code Live
1. `LogicalNode` in `ast_nodes.py`.
2. `_parse_logical_or()` and `_parse_logical_and()` in `parser.py`.

#### Live Code Walkthrough
```python
# src/simple_rule_engine/ast_nodes.py (add LogicalNode)
@dataclass(frozen=True)
class LogicalNode(ASTNode):
    operator: str
    left: ASTNode
    right: ASTNode

# src/simple_rule_engine/parser.py
def _parse_logical_or(self) -> ASTNode:
    left = self._parse_logical_and()
    while self._current().type == TokenType.LOGICAL_OP and self._current().value == "OR":
        self.pos += 1
        right = self._parse_logical_and()
        left = LogicalNode(operator="OR", left=left, right=right)
    return left

def _parse_logical_and(self) -> ASTNode:
    left = self._parse_comparison_or_grouped()
    while self._current().type == TokenType.LOGICAL_OP and self._current().value == "AND":
        self.pos += 1
        right = self._parse_comparison_or_grouped()
        left = LogicalNode(operator="AND", left=left, right=right)
    return left
```

#### Interactive Checkpoint #3 (Run in REPL)
Attendees execute the following command to verify precedence and parentheses:

```python
from simple_rule_engine.parser import Parser
from simple_rule_engine.ast_nodes import LogicalNode, ComparisonNode

# Test: Parentheses override default precedence
expr = "(age >= 18 AND citizen == True) OR visa == True"
ast = Parser.from_text(expr)

assert isinstance(ast, LogicalNode)
assert ast.operator == "OR"
assert isinstance(ast.left, LogicalNode)
assert ast.left.operator == "AND"
assert ast.right.variable == "visa"
print(" Milestone 3 Verified: Recursive Descent & Precedence works!")
```

---

### Milestone 4 (00:45–01:00): Evaluator, Type Coercion & Rule Engine

#### Core Concept
Walking the AST against a runtime facts dictionary. Performing dynamic type coercion (`int`, `float`, `bool`, `str`), short-circuit evaluation, and assembling the high-level `RuleEngine`.

#### Exact Classes & Functions to Code Live
1. `Evaluator` class with `_eval_comparison()`, `_eval_logical()`, `_coerce_type()` in `evaluator.py`.
2. `Rule` and `RuleEngine` classes in `engine.py`.

#### Live Code Walkthrough
```python
# src/simple_rule_engine/evaluator.py
class Evaluator:
    def __init__(self, facts: dict):
        self.facts = facts

    def evaluate(self, node: ASTNode) -> bool:
        if isinstance(node, ComparisonNode):
            actual = self.facts[node.variable]
            expected = self._coerce_type(actual, node.target_value.value)
            return self._compare(actual, node.operator, expected)
        if isinstance(node, LogicalNode):
            if node.operator == "AND":
                return self.evaluate(node.left) and self.evaluate(node.right)
            if node.operator == "OR":
                return self.evaluate(node.left) or self.evaluate(node.right)
        return False
```

#### Interactive Checkpoint #4 (Final Masterclass Challenge)
Attendees run the end-to-end medical expert system test:

```python
from simple_rule_engine.engine import Rule, RuleEngine

# Define Business Rules
rules = [
    Rule(
        name="Influenza Rule",
        conditions=["fever == True AND temperature >= 38.5", "cough == True OR sore_throat == True"],
        conclusion="Diagnosis: Influenza"
    ),
    Rule(
        name="Common Cold",
        conditions=["fever == False", "cough == True"],
        conclusion="Diagnosis: Common Cold"
    )
]

# Create Runtime Facts
patient_facts = {
    "fever": True,
    "temperature": 39.2,
    "cough": False,
    "sore_throat": True
}

# Run Engine
engine = RuleEngine(rules)
report = engine.execute(patient_facts)

assert report.fired_rules_count == 1
assert report.passed_conclusions == ["Diagnosis: Influenza"]
print(" 🎉 MASTERCLASS COMPLETE: Full Rule Engine successfully executed!")
```

---

## 3. Specialized Code-Along Labs (30 Minutes Each)

### Lab 1: The Resilient Type Coercion & Operator Evaluation Pipeline (30 min)
- **Objective:** Deep-dive into edge-case data types: handling string quotes, boolean variations (`"true"`, `"1"`, `"yes"`), floating-point epsilon comparisons, and missing fact keys.
- **Hands-On Exercise:** Implement a strict vs. lenient `FactContext` class that returns fallback defaults or raises custom `MissingFactError`.
- **Assertion Challenge:**
  ```python
  ctx = FactContext({"country": "India"}, strict=False)
  assert ctx.get("missing_var") is None
  ```

### Lab 2: Parsing Nested Parentheses & Multi-Clause Expressions (30 min)
- **Objective:** Extend the grammar to support arbitrary parenthetical nesting depth (e.g. `(((a == 1) AND b == 2) OR (c == 3 AND (d == 4 OR e == 5)))`).
- **Hands-On Exercise:** Add character column tracking to syntax errors so attendees see exact ASCII arrows pointing to missing parentheses.
- **Assertion Challenge:**
  ```python
  try:
      Parser.from_text("a == 1 AND (b == 2")
  except ParserError as err:
      assert "Expected closing ')'" in str(err)
  ```

### Lab 3: Production Hardening: Custom Diagnostics & Pytest Matrix (30 min)
- **Objective:** Build an industrial test suite using `pytest.mark.parametrize` covering 100% of operators (`<`, `<=`, `>`, `>=`, `==`, `!=`), data types, and syntax violations.
- **Hands-On Exercise:** Write a 20-row parameterized test matrix verifying edge cases and benchmark throughput against 10,000 facts.
- **Assertion Challenge:** Run `pytest --cov=simple_rule_engine` and achieve 100% test coverage.

---

## 4. Facilitator Troubleshooting Playbook

| Symptom / Error | Root Cause | Live Debugging Hint (Terminal / REPL) | Immediate Resolution Code |
| :--- | :--- | :--- | :--- |
| **`TypeError: '<' not supported between instances of 'str' and 'int'`** | Comparison value was not coerced into fact's type before evaluation. | Run: `type(actual), type(expected)` inside `_eval_comparison` | Wrap in `_coerce_type(actual, target)`: `if isinstance(actual, int): expected = int(expected)` |
| **`AttributeError: 'NoneType' object has no attribute 'variable'`** | Parser returned `None` on syntax failure instead of raising an explicit `ParserError`. | Check return type of `Parser.parse()` | Replace `return None` with `raise ParserError("Invalid syntax")` |
| **`AssertionError: "'Female'" != "Female"` (String quotes bug)** | Lexer did not strip enclosing `'` or `"` characters during string token creation. | Run: `token.value` on a string token to check for quotes | In `Lexer._read_string`: increment `self.pos` past opening and closing quote characters. |
| **`IndexError: string index out of range` in Lexer** | Lookahead `_peek()` accessed `self.pos + 1` without checking `pos + 1 < length`. | Check length guard before inspecting `self.text[self.pos + 1]` | Add guard: `if self.pos + 1 < self.length and self.text[self.pos + 1] == ...` |
| **`AND` evaluated with lower priority than `OR`** | Parser grammar flipped `logical_or` and `logical_and` method calls. | Trace: `_parse_logical_or` must call `_parse_logical_and`, not vice versa | Grammar hierarchy: `_parse_logical_or` calls `_parse_logical_and` which calls `_parse_comparison_or_grouped`. |
| **`KeyError: 'marks'` during evaluation** | Fact dictionary missing key referenced in condition. | Print `self.facts.keys()` inside `_eval_comparison` | Guard fact lookup: `if node.variable not in self.facts: raise MissingFactError(...)` |
| **`RecursionError: maximum recursion depth exceeded`** | Grammar method called itself without consuming any tokens (infinite loop). | Check `self.pos` inside the `while` loop | Ensure `self.pos += 1` or `self._consume()` advances the token index before recursing. |
