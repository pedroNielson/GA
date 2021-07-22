from abc import abstractproperty
import math
import random




#Metodo para adicionar os valores de calculados na modal na lista de fitness
def fitness(pop, tam):
    fitness = []
    for i in range(tam):
        aux = modal_function(pop[i])
        fitness.append(round(aux, 4))
    return fitness

#Metodo para calcular as modais, com os individuos gerados aleatoriamente
def modal_function(individual):
    x1 = individual[0]
    x2 = individual[1]

    aux1 = 0
    aux2 = 0
    i = 0

    while i < 6:
        aux1 = aux1 + (i*math.cos((i+1)*x1 + i))
        aux2 = aux2 + (i*math.cos((i+1)*x2 + i))
        i = i+1

    f_modal = aux1*aux2
    

    return f_modal

#Metodo para criacao dos individuos
def individual():
    individual = []
    for i in range(2):
        aux = random.uniform(-10, 10) #Cria um numero aleatorio de -10 a 10 e adiciona ele com 4 casas decimais aos individuos (x1 e x2)
        individual.append(round(aux, 4))

    return individual

#Metodo para criacao da populacao, depende do tamanho selecionado na main
def population(tam):
    population = []

    for i in range(tam):
        aux = individual()
        population.append(aux)

    return population

# Método de selecao por torneio, compara dois individuos e escolhe o melhor, no caso o de menor valor
def selection(fitness, pop, tam):
    selection = []  # Lista de individuos selecionados

    # Gerando numeros aleatórios de 0 até o tamanho da populacao para a selecao
    for i in range(tam):
        aux1 = random.randrange(0, tam)
        aux2 = random.randrange(0, tam)

    # Torneio dos individuos, onde o menor é o selecionado para o caso trabalhado
        if fitness[aux1] > fitness[aux2]:
            selection.append(pop[aux2])
        elif fitness[aux1] < fitness[aux2]:
            selection.append(pop[aux1])
        elif fitness[aux1] == fitness[aux2]:
            selection.append(pop[aux1])

    return selection

# Método para calcular o crossover através do método blx-alpha


def BLX_Alpha(p1, p2, pop):
    alpha = 0.5  # Alpha definido normalmente a 0.5
    # Beta definido como um numero aleatorio de - alpha, até 1+ alpha
    beta = round(random.uniform(-alpha, 1+alpha), 4)

    Children = []  # Lista de filhos geradoss pelo crossover

    # Calculo da equacao c para o crossover, onde 0 = x1, e 1 = x2

    Cx1 = pop[p1][0] + (beta*(pop[p2][1] - pop[p1][0]))
    Cx2 = pop[p2][1] + (beta*(pop[p1][0] - pop[p2][1]))

    # Filtrando o limite superior e inferior dos filhos calculados em Cx1 e Cx2

    if Cx1 > 10:
        Cx1 = 10
    elif Cx1 < -10:
        Cx1 = -10

    if Cx2 > 10:
        Cx2 = 10
    elif Cx2 < -10:
        Cx2 = -10

    # Inserindo os filhos gerados na lista de filhos

    Children.append(round(Cx1, 4))
    Children.append(round(Cx2, 4))

    return Children


def crossover(pop, tam):
    crossover_result = []  # Lista com os individuos resultantes do crossover
    crossover_rate = 0.95  # Taxa de crossover de 95%

    for i in range(tam):
        # Gerando um numero aleatorio de 0 a 1 e o comparando com a taxa de crossover
        random_number = random.uniform(0.0, 1.0)
        if random_number > crossover_rate:  # Caso o numero aleatorio seja maior que a taxa de crossover, o individuo não é selecionado
            # Gerando dois numeros aleatorios
            aux1 = random.randint(0, tam-1)
            aux2 = random.randint(0, tam-1)
            # Individuos que nao foram selecionados para o crossover sao adicionados na populacao final, mas sem passar pela operacao
            p1 = [round(pop[aux1][0], 4), round(pop[aux2][1], 4)]
            crossover_result.append(p1)

        elif random_number <= crossover_rate:  # Caso o numero aleatorio seja menor que a taxa de crossover, ou seja, dentro do range, o individuo é selecionado para tal operacao
            # Gerando dois numeros aleatorios para os pais
            aux1 = random.randint(0, tam-1)
            aux2 = random.randint(0, tam-1)

            # Aplicando o método BLX-Alpha para o calculo do crossover dos individuos
            result = BLX_Alpha(aux1, aux2, pop)

            # Inclusao dos individuos na lista de individuos resultantes do crossover
            crossover_result.append(result)

    return crossover_result


def mutation(aux_pop, elit):
    mutation_result = []  # Lista com os individuos resultantes da mutacao
    mutation_rate = 0.30  # Taxa de mutacao de 30%

    pop_length = len(aux_pop)

    for i in range(pop_length):
        mutation_temp = []  # Lista temporaria para armazenar os novos individuos
        # Gerando um numero aleatorio de 0 a 1.5 e o comparando com a taxa de mutacao
        random_number = random.uniform(0.0, 1.0)
        if random_number > mutation_rate:  # Caso o numero aleatorio seja maior que a taxa de mutacao, o individuo não é selecionado
            
            mutation_temp = aux_pop[i]

        elif random_number <= mutation_rate:  # Caso o numero aleatorio seja menor ou igual a taxa de mutacao, o individuo é selecionado para tal
            # Valor do intervalo de mutacao, randomizado de 0.95 a 1.05
            mutation_interval = random.uniform(0.95, 1.05)
            # Aplicando o intervalo de mutação a populacao para gerar os novos individuos
            mutation_x1 = aux_pop[i][0]*mutation_interval
            mutation_x2 = aux_pop[i][1]*mutation_interval

            # Filtrando individuos acima dos limites superior e inferior, e os corrigindo para dentro destes limites
            if mutation_x1 > 10:
                mutation_x1 = 10
            elif mutation_x1 < -10:
                mutation_x1 = -10

            if mutation_x2 > 10:
                mutation_x2 = 10
            elif mutation_x2 < -10:
                mutation_x2 = -10

            # Inserindo os individuos mutados na lista temporaria
            mutation_temp.append(round(mutation_x1, 4))
            mutation_temp.append(round(mutation_x2, 4))
            

        # Apendando todos os individuos na lista resultado da mutacao
        mutation_result.append(mutation_temp)

    mutation_result.append(elit)
    return mutation_result


def elitism(fitness, pop, tam):  # metodo que escolhe o melhor fitness da geracao
    rand = random.randint(1, 10)  # Valor randomico de 0 a 10
    # Inicia a variavel de melhor resultado com algum valor alatorio da fitness
    top_result = fitness[0]
    flag = 0  # Variavel para marcar o indice que obteve sucesso

    for i in range(tam):  # For rodando pela lista de fitness
        # Caso a fitness seja menor ou igual que o melhor resultado
        if top_result >= fitness[i]:
            # A fitness é atribuida ao melhor resultado, pois estamos procurando o mínimo
            top_result = fitness[i]
            flag = i  # O indice da melhor fitness é marcado

    
    
    # São retornados os pontos x1 e x2 referentes a melhor fitness da geracao
    return pop[flag]

