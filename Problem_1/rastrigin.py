import numpy as np
import math
import matplotlib.pyplot as plt


# Resolve Rastrigin funtion with GA (genetic algorithm)
# Parameters


D = 2
INDIV_SIZE = 10          # DNA length
POP_SIZE = 100           # population size                          
CROSS_RATE = 0.08        # mating probability (DNA crossover)
MUTATION_RATE = 0.005    # mutation probability        # valor mais baixo converge + RAPIDO
N_GENERATIONS = 150
X_BOUND = [-5.12, 5.12]  #upper on lower limits

def F(x):

    return 10*D + sum([(x**2 - 10 * np.cos(2 * math.pi * x))])

 #S = 10*D + ((X[:-1]**2 - 10*np.cos(2*np.pi * X[:-1])) + (X[1:]**2 - 10*np.cos(2*np.pi * X[:-1]))

# find non-zero fitness for selection
def get_fitness(pred): 
        
    return pred - 1e-3 - np.max(pred)

# convert binary DNA to decimal and normalize it to a range(-5, 5)
def translateDNA(pop):
    return pop.dot(2 ** np.arange(INDIV_SIZE)[::-1]) / float(2**INDIV_SIZE-1) * (X_BOUND[1] - X_BOUND[0]) + X_BOUND[0]


def select(pop, fitness):    # nature selection wrt pop's fitness
    idx = np.random.choice(np.arange(POP_SIZE), size=POP_SIZE, replace=True, p=fitness/fitness.sum())
    return pop[idx]

def crossover(parent, pop): # mating process (genes crossover)
        if np.random.rand() < CROSS_RATE:
                i_ = np.random.randint(0, POP_SIZE, size=1)                               # select another individual from pop
                cross_points = np.random.randint(0, 2, size=INDIV_SIZE).astype(np.bool)   # choose crossover points
                parent[cross_points] = pop[i_, cross_points]                              # mating and produce one child
        return parent

def mutate(child):
    for point in range(INDIV_SIZE):
        if np.random.rand() < MUTATION_RATE:
            child[point] = 1 if child[point] == 0 else 0
    return child

pop = np.random.randint(2, size=(POP_SIZE, INDIV_SIZE))   # initialize the pop DNA

plt.ion()       # something about plotting
x = np.linspace(*X_BOUND, 200)
plt.xlabel('x')
plt.ylabel('F(x)')
plt.plot(x, F(x))

for _ in range(N_GENERATIONS):
        F_values = F(translateDNA(pop))    # compute function value by extracting DNA

        if 'sca' in locals():
            sca.remove()
        sca = plt.scatter(translateDNA(pop), F_values, s=200, lw=0, c='red', alpha=0.5)
        plt.pause(0.05)

        # GA part (evolution)
        fitness = get_fitness(F_values)
        print("Fittest solution: ", pop[np.argmax(fitness), :])

        pop = select(pop, fitness)
        pop_copy = pop.copy()

        for parent in pop:
            child = crossover(parent, pop_copy)
            child = mutate(child)
            parent[:] = child  # parent is replaced by its child

plt.ioff()
plt.show()
print('The best individual found is {0}'.format(pop[0]))
print('The optimal solution is x={0} and f(x)={1}'.format(translateDNA(pop[0]), F(translateDNA(pop[0]))))


if __name__ == "__main__":
    main()


