import random

"""
squirrel has 3 survival attributes:
bury acorn?
run from dog?
hide in tree?
each action has a value 0-1, frequency of action

eye color attribute is neutral
eye color on scale 0-1
eye color to observe evolution
"""

# actions, favored or not
# if favored, then fitness = (value) ^ 2
# if not, then fitness = (value - 1) ^ 2

bury_acorn = "favored"
run_from_dog = "favored"
hide_in_tree = "favored"

# set the starting population size
constant_population_size = 1000

# set the mutation rate (0 - 1, 1 being more frequent)
mutation_rate = 0.02

# set number of generations to run
num_generations = 100

population_size = constant_population_size

# generate initial random population of squirrels
population = []
def generate_new_population():
    for squirrel in range(population_size):
        x = []
        for num_attributes in range(3):
            x.append(random.random())
        population.append(x)

# evaluates fitness
fitness = []
def evaluate_fitness():
    global population
    for squirrel in range(population_size):
        if bury_acorn == "favored":
            fit_1 = (population[squirrel][0]) ** 2
        if bury_acorn == "not":
            fit_1 = (population[squirrel][0] - 1) ** 2
        if run_from_dog == "favored":
            fit_2 = (population[squirrel][1]) ** 2
        if run_from_dog == "not":
            fit_2 = (population[squirrel][1] - 1) ** 2
        if hide_in_tree == "favored":
            fit_3 = (population[squirrel][2]) ** 2
        if hide_in_tree == "not":
            fit_3 = (population[squirrel][2] - 1) ** 2
        fitness.append((fit_1 + fit_2 + fit_3) / 3)

# perform crossover
def crossover():
    global population
    global population_size
    new_population = []
    for squirrel in range(population_size):
        if (random.random() < (fitness[squirrel])) == True:
            new_population.append(population[squirrel])
    population = new_population
    if (len(population) > constant_population_size):
        while len(population) > constant_population_size:
            population.pop(-1)
    if len(population) % 2 != 0:
        population.pop(-1)
    for pair in range(0, len(population), 2):
        child = []
        for gene in range(3):
            if (random.random() < .5):
                child.append(population[pair][gene])
            else:
                child.append(population[pair + 1][gene])
        population.append(child)
    population_size = len(population)

# mutation
def mutate():
    for squirrel in range(population_size):
        for gene in range(3):
            if (random.random() < mutation_rate):
                population[squirrel][gene] = population[squirrel][gene] * random.random()

generate_new_population()
for generations in range(num_generations):
    fitness = []
    evaluate_fitness()
    crossover()
    print("finished generations: ", generations)
average_fitness = 0
for fitness_value in range(len(fitness)):
    average_fitness += fitness[fitness_value]
average_fitness = average_fitness / len(fitness)
print("average fitness: ", average_fitness)
