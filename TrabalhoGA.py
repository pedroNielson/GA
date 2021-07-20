import math
import random


def fitness(pop, tam):
    fitness = []
    for i in range(tam):
        aux = modal_function(pop[i])
        fitness.append(aux)
    return fitness


def modal_function(individual):
    x1 = individual[0]
    x2 = individual[1]

    for i in range(1,5):
        f_modal = (i*math.cos((i+1)*x1 + i))*(i*math.cos((i+1)*x2 + i))
    
    return f_modal



def individual():
    individual = []
    for i in range(2):
        aux = random.uniform(-10,10)
        individual.append(round(aux,4))
    
    return individual


def population(tam):
    population = []

    for i in range(tam):
        aux = individual()
        population.append(aux)
    
    return population


def selection(fitness, pop, tam):
    selection = []
    for i in range(tam):
        x1 = random.randint(0,tam)
        x2 = random.randint(0,tam)

        if fitness[x1] > fitness[x2]:
            selection.append(pop[x1])
        elif fitness[x2] > fitness[x1]:
            selection.append(pop[x2])
        elif fitness[x1] == fitness[x2]:
            selection.append(pop[x1])
    
    return crossover(selection, tam)


def crossover(pop, tam):
    x=0


pop = population(5)

print(pop)

print(fitness(pop,5))
