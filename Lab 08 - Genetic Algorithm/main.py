"""Genetic algorithm maximizing the number of one-bits in a chromosome."""

import random


CHROMOSOME_LENGTH = 20
POPULATION_SIZE = 40
MAX_GENERATIONS = 200
MUTATION_RATE = 0.02


def fitness(chromosome):
    return sum(chromosome)


def tournament_selection(population, rng, tournament_size=3):
    contestants = rng.sample(population, tournament_size)
    return max(contestants, key=fitness)


def crossover(parent_a, parent_b, rng):
    point = rng.randint(1, CHROMOSOME_LENGTH - 1)
    return parent_a[:point] + parent_b[point:], parent_b[:point] + parent_a[point:]


def mutate(chromosome, rng):
    return [
        1 - bit if rng.random() < MUTATION_RATE else bit
        for bit in chromosome
    ]


def main():
    rng = random.Random(7)
    population = [
        [rng.randint(0, 1) for _ in range(CHROMOSOME_LENGTH)]
        for _ in range(POPULATION_SIZE)
    ]

    for generation in range(MAX_GENERATIONS + 1):
        best = max(population, key=fitness)
        if generation % 10 == 0 or fitness(best) == CHROMOSOME_LENGTH:
            print(f"Generation {generation}: best fitness "
                  f"{fitness(best)}/{CHROMOSOME_LENGTH}")
        if fitness(best) == CHROMOSOME_LENGTH or generation == MAX_GENERATIONS:
            break

        next_population = [best.copy()]
        while len(next_population) < POPULATION_SIZE:
            parent_a = tournament_selection(population, rng)
            parent_b = tournament_selection(population, rng)
            child_a, child_b = crossover(parent_a, parent_b, rng)
            next_population.append(mutate(child_a, rng))
            if len(next_population) < POPULATION_SIZE:
                next_population.append(mutate(child_b, rng))
        population = next_population

    print(f"Best chromosome: {''.join(map(str, best))}")
    print(f"Best fitness: {fitness(best)}/{CHROMOSOME_LENGTH}")


if __name__ == "__main__":
    main()
