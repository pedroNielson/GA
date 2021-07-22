import TrabalhoGA as GA
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


population_size = 50 #Tamanho da populacao
Generations = 150 #Numero de geracoes
saida = [] #Lista de saida
mut = [] #Lista de mutacao
pontos_saida = [] #Lista dos ponts de saida
  
def compara_saida(saida): #Metodo que verifica o menor valor de fitness na lista de saida

    global_minimum = saida[0]

    for i in range(Generations):
        if global_minimum >= saida[i]:
            global_minimum = saida[i]
            

    return global_minimum 

pop = GA.population(population_size) #Gera a populacao inicial
for i in range(Generations): #Roda todas as geracoes
    
    
    fit_inicial = GA.fitness(pop, population_size) #Gera o fitness e armazena na variavel dada
    elit_inicial = GA.elitism(fit_inicial, pop, population_size) #Gera o elitismo
    selec = GA.selection(fit_inicial, pop, population_size) #Gera a selecao 
    cross = GA.crossover(selec, population_size) #Gera o crossover
    mut = GA.mutation(cross, elit_inicial) #Gera a mutacao
    
    pop = mut #Substitui a primeira populacao pela populacao mutada (nova)
    population_size = population_size + 1 #Soma mais um na populacao, devido a adicao do melhor individuo
    pontos_saida.append(elit_inicial) #Armazena os pontos x1 e x2 na lista de pontos
    saida.append(GA.modal_function(elit_inicial)) #Armazena as fitness pontos gerados pelo elismo 

aux = compara_saida(saida) #Metodo pra achar o minimo

print("Minimo global: ", aux) #Print do minimo global 




#Parte de resultados
lista_fitness = []
lista_ponts = []
lista_fitness = saida
lista_ponts = pontos_saida

#Método para calculo dos parametros estatisticos
def resultados():
    media = np.mean(lista_fitness)
    dp = np.std(lista_fitness)
    var = np.var(lista_fitness)
    
    print("Media: ", media)
    print("Variancia: ", var)
    print("Desvio padrao: ", dp)
    
resultados()


#Plot dos gráficos
plt.title("Melhor caso")
plt.xlabel("Gerações")
plt.ylabel("Fitness")
plt.xlim(0,100)
plt.plot(lista_fitness)
plt.show()








    

