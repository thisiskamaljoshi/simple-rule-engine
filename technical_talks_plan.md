# Conference & Meetup Technical Talks Plan: Rule Engines & AST Compilers
**Project:** SimpleRuleEngine (`simple-rule-engine`)  
**Speaker Profile:** Principal Software Engineer / Systems Architect / Technical Educator  
**Target Venues:** PyCon, EuroPython, Python Web Conf, DevSecOps Days, Architecture Meetups  

---

## Portfolio Overview

| Talk Type | Title | Duration | Target Venue / Audience | Core Theme |
| :--- | :--- | :---: | :--- | :--- |
| **Flagship Keynote / Masterclass** | *Demystifying Interpreters: Building a Production-Grade Rule Engine & AST Parser in Pure Python* | 45–60 min | PyCon Keynote / Architecture Summit / All Levels | End-to-End Compiler Pipeline & Expert System Architecture |
| **Track Talk 1 (Algorithms & Compilers)** | *Writing a Recursive Descent Parser from Scratch: Precedence, Parentheses, and Zero-RegEx Tokenization* | 25–30 min | PyData / Deep-Dive Technical Track | EBNF Grammars, Lexing, and AST Construction |
| **Track Talk 2 (Security & System Design)** | *Zero-Eval: Secure Dynamic Rule Evaluation Without Remote Code Execution* | 20–25 min | DevSecOps / Enterprise Backend Track | Sandboxing, DSL Security, and RCE Prevention |
| **Track Talk 3 (Software Craftsmanship)** | *Polymorphic Type Coercion & Visitor Evaluators: Bridging Dynamic Facts to String DSLs* | 20–25 min | Python User Groups (PUGs) / Code Quality Track | Dynamic Typing, Visitor Pattern, and Clean Refactoring |

---

## 1. Flagship Masterclass (45–60 min)

### Title
**Demystifying Interpreters: Building a Production-Grade Rule Engine & AST Parser in Pure Python**

### Format & Event Fit
- **Format:** 45-minute presentation + 15-minute live coding demo & Q&A.
- **Audience:** Senior Software Engineers, Backend Architects, and Tech Leads.
- **Event Fit:** PyCon, EuroPython, Regional Python Conferences, Engineering Masterclasses.

### Opening Narrative Hook & Problem Statement
> *"Every growing business application eventually reaches a crossroads: product managers demand configurable business logic, while engineers dread deploying new code for every minor threshold change. The hasty solution? Storing Python condition strings in a database and running `eval()`. The result? A security time-bomb and fragile architectures that break on the first typo.*
> 
> *In this masterclass, we will demystify how compilers and interpreters work by building an industrial-strength Rule Engine from scratch in 100% standard library Python—complete with a Lexer, Recursive Descent Parser, and AST-walking Evaluator."*

### Repository Files Projected & Walked Through
1. `README.md` — The Expert System problem statement and constraints.
2. `src/simple_rule_engine/tokens.py` — Defining the lexical token grammar.
3. `src/simple_rule_engine/lexer.py` — Building the single-pass tokenizer.
4. `src/simple_rule_engine/ast_nodes.py` — The AST node class hierarchy.
5. `src/simple_rule_engine/parser.py` — The Recursive Descent parser with precedence climbing.
6. `src/simple_rule_engine/evaluator.py` — The tree-walking evaluator with short-circuiting.
7. `src/simple_rule_engine/engine.py` — The high-level `Rule` and `RuleEngine` orchestration API.

### Live Terminal & REPL Demo Script

```bash
# Step 1: Launch interactive Python session
python -q

# Step 2: Import the engine components
>>> from simple_rule_engine.lexer import Lexer
>>> from simple_rule_engine.parser import Parser
>>> from simple_rule_engine.evaluator import Evaluator
>>> from simple_rule_engine.engine import Rule, RuleEngine

# Step 3: Demonstrate Tokenizer
>>> expr = "temperature >= 38.5 AND (cough == True OR soreThroat == True)"
>>> tokens = Lexer(expr).tokenize()
>>> for t in tokens: print(t)
# Output: Token stream with positions

# Step 4: Demonstrate AST Generation
>>> ast = Parser.from_text(expr)
>>> print(ast)
# Output: ((temperature >= Literal(38.5)) AND ((cough == Literal(True)) OR (soreThroat == Literal(True))))

# Step 5: Evaluate against Facts
>>> facts = {"temperature": 39.2, "cough": False, "soreThroat": True}
>>> evaluator = Evaluator(facts)
>>> evaluator.evaluate(ast)
# Output: True

# Step 6: Full Expert System Execution
>>> engine = RuleEngine([
...     Rule(name="Fever Alert", conditions=["temperature >= 38.0"], conclusion="Prescribe Antipyretic"),
...     Rule(name="Flu Diagnosis", conditions=[expr], conclusion="Isolate for Influenza")
... ])
>>> report = engine.execute(facts)
>>> print(f"Fired Rules: {report.passed_conclusions}")
# Output: Fired Rules: ['Prescribe Antipyretic', 'Isolate for Influenza']
```

### Key Audience Takeaways
1. How compiler pipelines work: Lexing $\to$ Parsing $\to$ AST Generation $\to$ Evaluation.
2. Why writing a dedicated recursive descent parser is faster, safer, and cleaner than regular expressions.
3. How to build secure domain-specific languages (DSLs) in Python without third-party dependencies.

---

## 2. Specialized Track Talk 1: Algorithms & Compilers (25–30 min)

### Title
**Writing a Recursive Descent Parser from Scratch: Precedence, Parentheses, and Zero-RegEx Tokenization**

### Format & Event Fit
- **Format:** 25-minute focused technical track talk.
- **Audience:** Intermediate-to-Senior Engineers interested in data structures, algorithms, and domain-specific languages.
- **Event Fit:** PyData, Algorithm Deep-Dive Meetups, Computer Science Seminars.

### Opening Narrative Hook & Problem Statement
> *"Why does `str.split('AND')` fail the moment you have 3 conditions or parentheses? Because formal languages cannot be parsed with flat string splitting or regular expressions. In this talk, we explore how to turn an EBNF grammar into recursive Python methods that build an Abstract Syntax Tree in $O(N)$ linear time."*

### Repository Files Projected & Walked Through
1. `src/parser.py` vs `src/logical_parser.py` (Deconstructing why the legacy flat-splitting approach fails).
2. `src/simple_rule_engine/tokens.py` & `src/simple_rule_engine/lexer.py` (Handling quoted literals and operator tokenization).
3. `src/simple_rule_engine/parser.py` (Walking through `_parse_logical_or`, `_parse_logical_and`, `_parse_comparison_or_grouped`).

### Live Terminal & REPL Demo Script

```python
# Demonstrate the flaw of flat splitting vs AST recursion
>>> from simple_rule_engine.parser import Parser

# Compound multi-clause condition with operator precedence
>>> complex_rule = "age >= 18 AND citizen == True OR visa == 'Valid'"
>>> ast = Parser.from_text(complex_rule)
>>> print("AST Representation:", ast)
# Shows: (((age >= Literal(18)) AND (citizen == Literal(True))) OR (visa == Literal('Valid')))

# Parenthesized condition changing precedence
>>> grouped_rule = "age >= 18 AND (citizen == True OR visa == 'Valid')"
>>> ast_grouped = Parser.from_text(grouped_rule)
>>> print("Grouped AST:", ast_grouped)
# Shows: ((age >= Literal(18)) AND ((citizen == Literal(True)) OR (visa == Literal('Valid'))))
```

### Key Audience Takeaways
1. Understanding Extended Backus-Naur Form (EBNF) grammars.
2. How to implement operator precedence climbing without complex parsing libraries.
3. How to produce clear syntax error diagnostics with exact column numbers.

---

## 3. Specialized Track Talk 2: Security & System Architecture (20–25 min)

### Title
**Zero-Eval: Secure Dynamic Rule Evaluation Without Remote Code Execution**

### Format & Event Fit
- **Format:** 20-minute lightning architecture / security track talk.
- **Audience:** Security Engineers, Backend Architects, DevSecOps Practitioners.
- **Event Fit:** DevSecOps Conferences, PyCon Security Tracks, Enterprise Python Summits.

### Opening Narrative Hook & Problem Statement
> *"Think you can safely sandbox Python's `eval()` with `eval(code, {'__builtins__': {}})`? Think again. In Python, bytecode introspection and object traversal can escape almost any custom sandbox. The only true way to run untrusted dynamic conditions safely is to eliminate `eval()` entirely. Let's see how our AST rule parser provides mathematically guaranteed execution safety."*

### Repository Files Projected & Walked Through
1. `README.md` (Zero-`eval` constraint analysis).
2. `src/evaluator.py` & `src/simple_rule_engine/evaluator.py` (Safe AST traversal without arbitrary code execution).
3. `tests/test_invalid_conditions.py` (Malicious input rejection tests).

### Live Terminal & REPL Demo Script

```python
# Attempting standard Python sandbox escape vs our Zero-Eval Engine
>>> from simple_rule_engine.parser import Parser
>>> from simple_rule_engine.evaluator import Evaluator
>>> from simple_rule_engine.exceptions import LexerError, ParserError

# Malicious payload designed to execute OS commands
>>> malicious_payload = "__import__('os').system('whoami') == 0"

# Attempting to feed malicious payload into SimpleRuleEngine:
>>> try:
...     ast = Parser.from_text(malicious_payload)
... except (LexerError, ParserError) as err:
...     print(f"🛡️ BLOCKED AT PARSE TIME: {err}")
# Output: 🛡️ BLOCKED AT PARSE TIME: Expected comparison operator. Found LPAREN ('(')

# Untrusted user input can NEVER reach Python's bytecode executor!
```

### Key Audience Takeaways
1. Why Python's `eval()` cannot be securely sandboxed against adversarial code.
2. How AST whitelisting provides complete isolation by design.
3. How to implement security boundaries between user-provided logic and runtime environments.

---

## 4. Specialized Track Talk 3: Software Craftsmanship & Refactoring (20–25 min)

### Title
**Polymorphic Type Coercion & Visitor Evaluators: Bridging Dynamic Facts to String DSLs**

### Format & Event Fit
- **Format:** 20-minute live refactoring presentation.
- **Audience:** Python Developers, Clean Code Advocates, Junior-to-Mid Backend Engineers.
- **Event Fit:** Local Python User Groups (PUGs), Tech Meetups, Internal Engineering Lunch & Learns.

### Opening Narrative Hook & Problem Statement
> *"In Python, `True == 1` is `True`, but `'Female' == \"'Female'\"` is `False`. During our code audit, we found a bug where uncalled quote-stripping functions silently caused a production rule to fail without throwing an error! Let's explore how dynamic type coercion works under the hood and how to refactor anemic classes into clean, test-backed domain models."*

### Repository Files Projected & Walked Through
1. `src/parser.py:161-164` & `src/evaluator.py:49-51` (The uncalled quote-stripper bug).
2. `src/rule.py` (Refactoring Java-style getters into idiomatic dataclasses).
3. `src/simple_rule_engine/evaluator.py` (The `_coerce_type` method and operator dispatch table).

### Live Terminal & REPL Demo Script

```python
# Demonstrating the subtle string quote bug and how the refactored engine fixes it
>>> from simple_rule_engine.parser import Parser
>>> from simple_rule_engine.evaluator import Evaluator

# Condition with single-quoted string literal
>>> rule_cond = "gender == 'Female' AND age >= 18"
>>> facts = {"gender": "Female", "age": 25}

>>> ast = Parser.from_text(rule_cond)
>>> print("Parsed Comparison Target:", ast.left.target_value.value)
# Shows clean string: 'Female' (quotes stripped by Lexer)

>>> evaluator = Evaluator(facts)
>>> print("Evaluation Result:", evaluator.evaluate(ast))
# Output: Evaluation Result: True
```

### Key Audience Takeaways
1. How to avoid silent data-type mismatch bugs in dynamically typed languages.
2. Refactoring "Kingdom of Nouns" anemic classes into clean Pythonic models.
3. Writing comprehensive unit test matrices using `pytest.mark.parametrize`.
