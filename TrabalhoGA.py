from abc import abstractproperty
import math
import random


def fitness(pop, tam):
    fitness = []
    for i in range(tam):
        aux = modal_function(pop[i])
        fitness.append(round(aux,4))
    return fitness


def modal_function(individual):
    x1 = individual[0]
    x2 = individual[1]

    aux1 = 0
    aux2 = 0
    i=0

    while i<6:
        aux1 = aux1 + (i*math.cos((i+1)*x1 + i))
        aux2 = aux2 + (i*math.cos((i+1)*x2 + i))
        
        print("Iteracao ", i)
        print("Primeira parte: ", "X1 = ", x1, "X2 = ", x2, "resultado: ", aux1)
        print("Segunda parte: ", "X1 = ", x1, "X2 = ", x2, "resultado: ", aux2)
        i = i+1

    f_modal = aux1*aux2
    print("Aux1: ", aux1, "Aux2: ", aux2)
    print("Modal final: ",f_modal)


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
        aux1 = random.randrange(0,tam) 
        aux2 = random.randrange(0,tam)

    #Torneio dos individuos, onde o menor é o selecionado para o caso trabalhado
        if fitness[aux1] > fitness[aux2]:
            print("Random: ", aux1, " ", aux2, "Entrou em: ", fitness[aux1], ">", fitness[aux2])
            selection.append(pop[aux2])
        elif fitness[aux1] < fitness[aux2]:
            print("Random: ", aux1, " ", aux2,"Entrou em: ", fitness[aux1], "<", fitness[aux2])
            selection.append(pop[aux1])
           
            
        elif fitness[aux1] == fitness[aux2]:
            print("Random: ", aux1, " ", aux2,"Entrou em: ", fitness[aux1], "=", fitness[aux2])
            selection.append(pop[aux1])
            
    
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

    Children.append(round(Cx1,4))
    Children.append(round(Cx2,4))

    return Children


def crossover(pop, tam):
    crossover_result = [] #Lista com os individuos resultantes do crossover
    crossover_rate = 0.95 #Taxa de crossover de 95%

    for i in range(tam):
        random_number = random.uniform(0.0,1.0) #Gerando um numero aleatorio de 0 a 1 e o comparando com a taxa de crossover 
        if random_number > crossover_rate:  #Caso o numero aleatorio seja maior que a taxa de crossover, o individuo não é selecionado 
            #Gerando dois numeros aleatorios
            aux1 = random.randint(0, tam-1)
            aux2 = random.randint(0, tam-1)

            #
            p1 = [round(pop[aux1][0],4), round(pop[aux2][1],4)]
            #p2 = [round(pop[aux2][0],4), round(pop[aux1][1],4)]

            #if random.randint(0,1) != 0:
            crossover_result.append(p1)
            #else:
                #crossover_result.append(p2)
                
        elif random_number <= crossover_rate: #Caso o numero aleatorio seja menor que a taxa de crossover, ou seja, dentro do range, o individuo é selecionado para tal operacao
            #Gerando dois numeros aleatorios para os pais 
            aux1 = random.randint(0, tam-1)
            aux2 = random.randint(0, tam-1)

            #Aplicando o método BLX-Alpha para o calculo do crossover dos individuos 
            result = BLX_Alpha(aux1,aux2,pop)

            #Inclusao dos individuos na lista de individuos resultantes do crossover
            crossover_result.append(result)
    
    return crossover_result


def creep_mutation():
    teste = 0



def mutation(pop, tam):
    mutation_result = [] #Lista com os individuos resultantes da mutacao
    mutation_rate = 0.30 #Taxa de mutacao de 30%

    for i in range(tam):
        random_number = random.uniform(0.0,1.5) #Gerando um numero aleatorio de 0 a 1.5 e o comparando com a taxa de mutacao   
        if random_number > mutation_rate: #Caso o numero aleatorio seja maior que a taxa de mutacao, o individuo não é selecionado
            aux = pop[i]
            mutation_result.append(aux)

        elif random_number <= mutation_rate: #Caso o numero aleatorio seja menor ou igual a taxa de mutacao, o individuo é selecionado para tal  
            for j in range(tam):
                mutation_interval = random.uniform(0.95, 1.05) #Valor do intervalo de mutacao, randomizado de 0.95 a 1.05
                mutation = tam[i][j]*mutation_interval #Aplicando o intervalo de mutação a populacao para gerar os novos individuos

                #Filtrando individuos acima dos limites superior e inferior, e os corrigindo para dentro destes limites
                if mutation > 10:
                    mutation = 10
                elif mutation < -10:
                    mutation = -10
                
                aux = mutation
                mutation_result.append(aux)

    return mutation_result

tam = 10

pop = population(tam)
fit = fitness(pop,tam)
selec = selection(fit, pop, tam)
mut = mutation(pop,tam)

print("Populacao inicial: " , pop)
print("Fitness inicial: " , fit)
print("Crossover: ", selec)
print("Mutacao: ", mut)