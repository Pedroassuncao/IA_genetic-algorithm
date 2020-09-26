import numpy as np
import math
import statistics
import sys
import matplotlib.pyplot as mtlb


#Parametros


mu = 0                  # onde a funcao esta centrada
sigma2 = np.sqrt(5)     # Desvio padrao
t = 0                   # Contador
maxits = 100            # 1 dos Criterio de paragem
N = 200                 # numero de pontos dentro da funcao
Ne = 10                 # Numero de elementos de elite
D = 2

epsilon = sys.float_info.epsilon
#arrays utilizados no plot do mu e t
arrayX = []
arrayY = []
#plot
#fig, axs = mtlb.subplots(1, 2)
#axs[0].axvline(x=-5)
#axs[0].axvline(x=5)


# while maxits not exceed and not converged
while (t < maxits  and  sigma2 > epsilon):
    X = np.random.normal(mu, sigma2, N) # funcao de gauss
    #X2 = np.random.normal(mu, sigma2, N) # funcao de gauss
  # funcao de ackkley
    S = 10*D + np.exp(1) - 20 * np.exp(-0.2*np.sqrt((1/D)*(X**2)))
    #X = X1 + X2

    #axs[0].plot(X, S, ".")
    S, X = zip (*sorted(zip(S, X)))

    mu = statistics.mean(X[0:Ne])

    sigma2 = np.sqrt(np.var(X[0:Ne]))

    t = t + 1
    
    arrayY.append(mu)
    arrayX.append(t)
    mtlb.xlabel('nr. de iterações')
    mtlb.ylabel('mu')
    mtlb.plot(arrayX, arrayY, "x-")


print("mu = " + str(mu))
print("S = " + str(S[0]))
mtlb.show()
print("valor medio de mu = " + str(statistics.mean(arrayY)))