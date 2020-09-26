import numpy as np
import random
from numpy.random import choice
import matplotlib.pyplot as mtlb
#from p15_s import *
#from p15_l import *

# Parameters
SERV = 10                # numero de servidores
TASKS = 10               # numero de tarefas
POPULATION = 100        # Size of Population
CROSS_RATE = 0.003        # CrossOver Chance
MUTATION_RATE = 0.08    # Mutation Rate
N_GENERATIONS = 100     # Number of Generations
arrayX = []
arrayY = []
SCENARIO = 2 # 1 - USING THE CVS FILE; 2 - IF USING RANDOM GENERATOR # Dont forget update SERV and TASK for CVS

# Funcao que calcula o custo da matriz solucao somando todos os elementos
def fitness(elemento, matcusto):
    elemento = np.squeeze(np.asarray(elemento))
    result = elemento * matcusto
    custo_total = np.sum(result)  
    return custo_total

# Funcao que ira escolher quais soluçoes com melhor fitness
def aceitaRejeita(population, tempototal, matcusto):
    end = 0

    while True:

        solucao = []

        solution = population[
            random.randint(0, len(population) - 1)]
        solucao.append(fitness(solution, matcusto))

        maxFit = choice(tempototal)
        
        if (maxFit < solucao):
            return solution
        end = end + 1

        if end > 1000:
            return None

# Funcao que determina o criterio de crossover entre soluções
# Ajustar esta funcao para escolher outro metodo de crossover
def crossover(solution1, solution2):
    corta1 = solution1[:, 0:3]
    print(" seleciona 3 colunas primeira solução", "\n\n", corta1, "\n\n")

    corta2 = solution2[:, 3:10]
    

    print(" seleciona da 4 a 10 coluna da 2º solucao", "\n\n", corta2, "\n\n")
         
    # Junta os cortes das outras matrizes para gerar nova solução
    filho = np.hstack([corta2, corta1])

    print(" Matriz Filho com 3 colunas da solução 1 e 7 colunas da solução 2", "\n\n",
          filho, "\n\n")

    return filho

# Funcao que estrutura a nova matriz gerada
# Explicar melhor esta funcao
def mutacao(novo_filho):
    crianca = np.matrix(novo_filho)
    aux = crianca[:, [1, 3]]
    crianca[:, [1, 3]] = crianca[:, [3, 1]]
    crianca[:, [3, 1]] = aux

    return crianca
'''def mutacao(novo_filho):        # Mutar aleatoriamente um elemento da matriz
    crianca = np.matrix(novo_filho)
    while np.random.rand() < MUTATION_RATE:
        x = np.random.randint(TASKS)
        y = np.random.randint(SERV)
        crianca[x][y] = 1 - crianca[x][y]

    return crianca'''


def main():
    # Criar Matriz com custos

    matcusto = np.random.rand(SERV, TASKS)

    # inicializar populacao

    if SCENARIO == 2:
        population = []
        for w in range(POPULATION):
            elemento = np.zeros((SERV, TASKS), dtype=np.int)
            for i in range(TASKS):
                elemento[random.randint(0, SERV - 1)][i] = 1
            population.append(elemento)
    elif SCENARIO == 1:
        population = []
        matcusto = np.loadtxt(open("p15_s.csv", "rb"), dtype="int", delimiter=",", skiprows=0)
           

    # avalia o fitness

    tempototal = []
    for j in range(POPULATION):
        tempototal.append(fitness(population[j], matcusto))

    best_solution = []
    best_fitness = 0
    gen_count = 0
    crossover_count = 0
    mutation_count = 0
    for g in range(N_GENERATIONS):

        gen_count += 1

        solution1 = aceitaRejeita(population, tempototal, matcusto)
        solution2 = aceitaRejeita(population, tempototal, matcusto)

        print(" Solução 1", "\n\n", solution1, "\n\n", "Solução 2", "\n\n", solution2, "\n\n")

        # crossover

        novo_filho = []

        for _ in range(POPULATION):
            novo_filho.append(crossover(solution1, solution2))
            crossover_count += 1

        # mutacao

        crianca = []

        for _ in range(POPULATION):
            if np.random.rand() < MUTATION_RATE:
                crianca.append(mutacao(novo_filho[_]))
                mutation_count += 1
            else:
                crianca.append(novo_filho[_])

        # vereficar se a solucao e boa

        population = crianca

        for f in range(POPULATION):
            fitcrianca = fitness(population[f], matcusto)
            if best_fitness < fitcrianca:
                best_fitness = fitcrianca
                best_solution = population[f]
        arrayY.append(best_fitness)             #array para o plot
        arrayX.append(gen_count)                    #array para o plot

    print("\n\n", "Número de Gerações:", gen_count, "\n\n", "Número de Crossovers:", crossover_count, "\n\n",
          "Número de Mutações:", mutation_count, "\n\n", "MELHOR SOLUCAO:", "\n\n", best_solution)

    # cria um grafico para o melhor fitness x geracoes

    #media_tempototal = sum(tempototal) / N_GENERATIONS
    mtlb.title('variação da fitness')
    mtlb.xlabel('nr. de geracoes')
    mtlb.ylabel('fitness')
    mtlb.plot(tempototal)
    mtlb.show()
   
    

    #print(arrayX)
    #print(arrayY)
    mtlb.title('variação da best fitness')   
    mtlb.xlabel('nr. de geracoes')
    mtlb.ylabel('fitness')
    mtlb.plot(arrayX, arrayY, "x-")

    mtlb.show()


if __name__ == '__main__':
    main()
