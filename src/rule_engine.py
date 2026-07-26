from rule import Rule
from evaluator import evaluate

rules = [
    Rule(
        conditions=[
            "fever==True",
            "temperature>38"
        ],
        conclusion="High Fever"
    ),
    Rule(
        conditions=[
            "age>=18"
        ],
        conclusion="Adult"
    )
]

facts = {
    "fever": True,
    "temperature": 39,
    "cough": True,
    "age": 25
}

def evaluate_rule(rule:Rule,facts:dict) -> bool:
    results = []
    for condition in rule.get_conditions():
       results.append(evaluate(condition,facts))
    return all(results)

def evaluate_rules(rules:list[Rule],facts:dict) -> None:
    for rule in rules:
        result = evaluate_rule(rule,facts)
        fire_rule(rule,result)

def fire_rule(rule:Rule,evaluation:bool) -> None:
    if evaluation:
        print(rule.get_conclusion())

def run(rules:list[Rule],facts:dict) -> None:
    evaluate_rules(rules,facts)

run(rules,facts)