from abc import abstractproperty
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

# Método de selecao por torneio, compara dois individuos e escolhe o melhor, no caso o de menor valor

def selection(fitness, pop, tam):
    selection = [] #Lista de individuos selecionados
    
    #Gerando numeros aleatórios de 0 até o tamanho da populacao para a selecao 
    for i in range(tam):
        x1 = random.randint(0,tam) 
        x2 = random.randint(0,tam)

    #Torneio dos individuos, onde o menor é o selecionado para o caso trabalhado
        if fitness[x1] > fitness[x2]:
            selection.append(pop[x2])
        elif fitness[x2] > fitness[x1]:
            selection.append(pop[x1])
        elif fitness[x1] == fitness[x2]:
            selection.append(pop[x1])
            
    
    return crossover(selection, tam)

#Método para calcular o crossover através do método blx-alpha
def BLX_Alpha(p1, p2, pop):
    alpha = 0.5 #Alpha definido normalmente a 0.5
    beta = round(random.uniform(-alpha, 1+alpha),4) #Beta definido como um numero aleatorio de - alpha, até 1+ alpha

    Children = [] # Lista de filhos geradoss pelo crossover

    #Calculo da equacao c para o crossover, onde 0 = x1, e 1 = x2

    Cx1 = pop[p1][0] + (beta*(pop[p2][1] -pop[p1][0]))  
    Cx2 = pop[p2][1] + (beta*(pop[p1][0] -pop[p2][1]))

    #Filtrando o limite superior e inferior dos filhos calculados em Cx1 e Cx2

    if Cx1 > 10:
        Cx1 = 10
    elif Cx1 < -10:
        Cx1 = -10
    
    if Cx2 > 10:
        Cx2 = 10
    elif Cx2 < -10:
        Cx2 = -10
    

    #Inserindo os filhos gerados na lista de filhos

    Children.append(Cx1)
    Children.append(Cx2)

    return Children


def crossover(pop, tam):
    crossover_result = [] #Lista com os individuos resultantes do crossover
    crossover_rate = 0.95 #Taxa de crossover de 95%

    for i in range(tam):
        random_number = random.random(0.0,1.0) #Gerando um numero aleatorio de 0 a 1 e o comparando com a taxa de crossover 
        if random_number > crossover_rate:  #Caso o numero aleatorio seja maior que a taxa de crossover, o individuo não é selecionado 
            aux1 = random.randrange(0, tam)
            aux2 = random.randrange(0, tam)

            p1 = [pop[aux1][0], pop[aux2][1]]
            p2 = [pop[aux2][0], pop[aux1][1]]

            if random.randint(0,1) != 0:
                crossover_result.append(p1)
            else:
                crossover_result.append(p2)
        elif random_number <= crossover_rate:
            aux1 = random.randrange(0, tam)
            aux2 = random.randrange(0, tam)

            crossover_result.append(BLX_Alpha(p1,p2,pop))
    
    return mutation(crossover_result)


def mutation(pop):
    mutation_rate = 0.30





pop = population(5)

print(pop)

print(fitness(pop,5))
