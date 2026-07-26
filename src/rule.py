from dataclasses import dataclass


@dataclass
class Rule:
    """
    Represents a single rule in the rule engine.

    Attributes:
        conditions (list[str]):
            A list of conditions that must all evaluate to True.

        conclusion (str):
            The conclusion (or action) to execute when all
            conditions are satisfied.
    """

    conditions: list[str]
    conclusion: str

    def get_conditions(self) -> list[str]:
        """
        Returns all conditions associated with this rule.

        Returns:
            list[str]:
                The list of rule conditions.
        """
        return self.conditions

    def get_conclusion(self) -> str:
        """
        Returns the rule conclusion.

        Returns:
            str:
                The conclusion associated with this rule.
        """
        return self.conclusion

    def condition_count(self) -> int:
        """
        Returns the number of conditions in the rule.

        Returns:
            int:
                Number of conditions.
        """
        return len(self.conditions)

    def __str__(self) -> str:
        """
        Returns a readable string representation of the rule.
        """
        return (
            f"Rule("
            f"conditions={self.conditions}, "
            f"conclusion='{self.conclusion}')"
        )