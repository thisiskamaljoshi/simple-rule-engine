from rule import Rule
from evaluator import evaluate
from evaluator import evaluate_logical_expression

# rules = [
#     Rule(
#         conditions=[
#             "fever==True",
#             "temperature>38"
#         ],
#         conclusion="High Fever"
#     ),
#     Rule(
#         conditions=[
#             "age>=18"
#         ],
#         conclusion="Adult"
#     )
# ]

logical_rules = [
    Rule(
        conditions=[
            "fever==True AND temperature>=38",
            "body_weakness==True AND spots==False"
        ],
        conclusion="Viral Fever"
    ),
    Rule(
        conditions=[
            "gender=='Female' AND age>=18"
        ],
        conclusion="Girl"
    )
]

# facts = {
#     "fever": True,
#     "temperature": 39,
#     "cough": True,
#     "age": 25
# }

logical_facts = {
    "fever": True,
    "temperature": 39,
    "body_weakness": True,
    "cough": True,
    "spots": False,
    "gender": 'Female',
    "age": 25
}

def evaluate_rule(rule:Rule,facts:dict) -> bool:
    results = []
    for condition in rule.get_conditions():
       results.append(evaluate(condition,facts))
    return all(results)

def evaluate_logical_rule(rule:Rule,logical_facts:dict) -> bool:
    results = []
    for logical_condition in rule.get_conditions():
        results.append(evaluate_logical_expression(logical_condition,logical_facts))
    print(results)
    return all(results)

def fire_rule(rule:Rule,evaluation:bool) -> None:
    if evaluation:
        print(rule.get_conclusion())

def evaluate_rules(rules:list[Rule],facts:dict) -> None:
    for rule in rules:
        result = evaluate_rule(rule,facts)
        fire_rule(rule,result)

def evaluate_logical_rules(rules:list[Rule],facts:dict) -> None:
    for rule in rules:
        result = evaluate_logical_rule(rule,facts)
        fire_rule(rule,result)

def run(rules:list[Rule],facts:dict) -> None:
    evaluate_rules(rules,facts)

def run_logical_exp(rules:str,facts:dict) -> None:
    evaluate_logical_rules(rules,facts)

# run(rules,facts)
run_logical_exp(logical_rules,logical_facts)