import TrabalhoGA as GA

population_size = 50
Generations = 10
saida = []


  
def compara_saida(saida):

    global_minimum = saida[0]

    for i in range(Generations):
        global_minimum <= saida[i]
        global_minimum = saida[i]

    return global_minimum 

for i in range(Generations):
    
    pop = GA.population(population_size)
    fit_inicial = GA.fitness(pop, population_size)
    elit_inicial = GA.elitism(fit_inicial, pop, population_size)
    selec = GA.selection(fit_inicial, pop, population_size)
    cross = GA.crossover(selec, population_size)
    mut = GA.mutation(cross)
    
    pop = mut

    saida.append(elit_inicial)
    
    


    print("------------------ Geracao", i)
    #print("Fitness inicial: ", fit_inicial)
    print("Elite inicial: ", elit_inicial)
    #print("Pop incial: ", pop)
    #print("Selec: ", selec)
    #print("Cross: ",  cross)
    #print("Mut: ", mut)

aux = compara_saida(saida)  

print("Saida final? ", aux)
#print(saida)
#print(saida[0])
#print(saida[1])
#print(saida[2])


    

