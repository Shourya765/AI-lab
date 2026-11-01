# Lab 07: Forward Chaining and Backward Chaining

## Aim
Implement forward and backward chaining to perform logical reasoning from facts and rules.

## Objectives
- Understand rule-based reasoning.
- Implement forward chaining using facts and inference rules.
- Implement backward chaining to prove a goal.
- Compare data-driven and goal-driven inference.

## Algorithm / steps
1. Store each rule as a set of premise facts and one conclusion.
2. **Forward chaining:** repeatedly find rules whose premises are known, add their conclusions, and stop when no new facts can be inferred.
3. **Backward chaining:** start with the goal; succeed if it is a fact, otherwise recursively try to prove the premises of a rule that concludes the goal.
4. Track goals currently being proved to avoid infinite recursion in cyclic rules.
5. Print derived facts and whether the target goal can be proved.

## Source code
See [`main.py`](./main.py), which uses the example rules and facts from the lab instructions.

## Run and output
Run `python main.py`. Forward chaining derives `C`, `D`, and `E`; backward chaining reports whether `E` is provable from the initial facts and rules.

## Result and conclusion
Forward chaining is data-driven and derives consequences from known facts. Backward chaining is goal-driven and searches for supporting facts and rules. Both reach the same conclusion for this example.

## Output screenshots
Save a screenshot of the program's actual terminal output in this folder's `screenshots` directory before submission.
