# Lab 08: Genetic Algorithm

## Aim
Implement a genetic algorithm in Python to find an optimal solution using selection, crossover, and mutation.

## Objectives
- Represent candidate solutions as chromosomes.
- Initialize a population and calculate fitness.
- Select parents, perform crossover, and mutate offspring.
- Preserve and report the best solution across generations.

## Algorithm / steps
1. Create a seeded random population of 20-bit chromosomes.
2. Define fitness as the number of `1` bits; the optimum is the all-ones chromosome.
3. Select parents with a three-member tournament.
4. Apply one-point crossover and bit-flip mutation.
5. Preserve the best chromosome (elitism), repeat for each generation, and stop when the target is reached or the generation limit is met.

## Source code
See [`main.py`](./main.py). The fixed random seed makes the demonstration reproducible.

## Run and output
Run `python main.py`. The program prints the best fitness during the run and the best chromosome found.

## Result and conclusion
The genetic algorithm improves candidate solutions by applying selection and genetic operators over generations. It finds the maximum-fitness chromosome for this small demonstration; in general, stochastic search does not guarantee an optimum for every problem or parameter setting.

## Output screenshots
Save a screenshot of the program's actual terminal output in this folder's `screenshots` directory before submission.
