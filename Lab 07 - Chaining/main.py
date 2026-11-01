"""Forward and backward chaining over propositional rules."""


RULES = [
    ({"A", "B"}, "C"),
    ({"C"}, "D"),
    ({"D"}, "E"),
]
INITIAL_FACTS = {"A", "B"}


def forward_chain(facts, rules):
    inferred = set(facts)
    changed = True
    while changed:
        changed = False
        for premises, conclusion in rules:
            if premises <= inferred and conclusion not in inferred:
                inferred.add(conclusion)
                print(f"Inferred {conclusion} from {sorted(premises)}")
                changed = True
    return inferred


def backward_chain(goal, facts, rules, proving=None):
    if goal in facts:
        return True
    if proving is None:
        proving = set()
    if goal in proving:
        return False
    proving = proving | {goal}
    for premises, conclusion in rules:
        if conclusion == goal and all(
                backward_chain(premise, facts, rules, proving)
                for premise in premises):
            return True
    return False


def main():
    print("Forward chaining:")
    derived = forward_chain(INITIAL_FACTS, RULES)
    print(f"Known facts after inference: {sorted(derived)}")

    goal = "E"
    proved = backward_chain(goal, INITIAL_FACTS, RULES)
    print(f"Backward chaining: goal {goal} is "
          f"{'proved' if proved else 'not proved'}")


if __name__ == "__main__":
    main()
