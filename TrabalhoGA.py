import math
import random


def fitness(population, tam):
    fitness = []
    for i in range(tam):
        aux = modal_function(population[i])
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
