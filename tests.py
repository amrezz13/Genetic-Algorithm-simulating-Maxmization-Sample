import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import random
import seaborn as sns
import csv


population = np.random.randint(0, 1000, 1000)
description={}
total_populations=[]
crroses=[]
size_of_population=[]
for x in range(100000):

    n1 = random.randint(0, len(population)-1)
    dad = population[n1]
    population = np.delete(population, n1)
    n2 = random.randint(0, len(population)-1)
    mom = population[n2]
    population = np.delete(population, n2)
    integer_dad=dad
    integer_mom=mom

    def binary(dad, mom):
        dad_chromosome = [int(x) for x in list('{0:0b}'.format(dad))]
        mom_chromosome = [int(x) for x in list('{0:0b}'.format(mom))]
        if (len(dad_chromosome) > len(mom_chromosome)):
            while( len( mom_chromosome ) < len(dad_chromosome)):
                mom_chromosome.insert(0,0)
        elif(len(dad_chromosome)< len(mom_chromosome)):
            while(len(dad_chromosome)<len(mom_chromosome)):
                dad_chromosome.insert(0,0)
        else:
            pass

        return dad_chromosome, mom_chromosome


    dad, mom= np.asarray(binary(dad,mom))

    def swapping(dad, mom):
        n1 = random.randint(0, len(dad)-1)
        n2 = random.randint(0, len(mom)-1)
        dad_cross=dad[n1]
        mom_cross=mom[n2]
        mom[n2]=dad_cross
        dad[n1]=mom_cross
        return dad, mom

    brother, sister =swapping(dad, mom)
    def convert_to_decimal(brother, sister):
        size = len(brother) - 1
        integer_brother = 0
        integer_sister=0
        for x in range(size + 1):
            integer_brother = integer_brother + (brother[x] * (2 ** (size - x)))

        for x in range(size + 1):
            integer_sister = integer_sister + (sister[x] * (2 ** (size - x)))
        return integer_brother, integer_sister

    brother, sister = convert_to_decimal( brother, sister)

    if ((brother >= integer_mom) or (brother >= integer_dad)):
        population=np.insert(population,random.randint(0, (len(population)-1)), brother)

    if ((sister >= integer_mom) or (sister >= integer_dad)):
        population=np.insert(population,random.randint(0, (len(population)-1)), sister)


    fittness_of_population=np.average(population)
    total_populations.append(fittness_of_population)
    crroses.append(x)
    size_of_population.append(len(population))


mydata = {
    'Fitness of population':total_populations,
    'Size of population':size_of_population,
    'Number of crosses':crroses
}
print(total_populations)
df=pd.DataFrame(mydata)


plt.subplot(211)
plt.plot('Number of crosses','Fitness of population',data=df,label='fitness line')
plt.xlabel('Numbers Of Crosess')
plt.ylabel('Fitness of population')

plt.subplot(212)
plt.plot('Number of crosses','Size of population',data=df, linestyle='dashed',label='size of population')
plt.xlabel('Number of Crosess')
plt.ylabel('Size of the Population')
plt.legend()
plt.show()