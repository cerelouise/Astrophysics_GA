#from FitnessCalc import FitnessCalc
from Population import Population
from Algorithm import Algorithm
from time import time
from Individual import Individual
from datetime import datetime, date, time
import math

start = time()

#FitnessCalc.set_solution("100111000100001001110001000010011100010000")

my_pop = Population(50, True)

generation_count = 0
gen_max = 800000
equal_count = 0
equal_max = 1000

old_fitness = 0
while (my_pop.fitness_of_the_fittest() >= 0 and generation_count<gen_max and equal_count < equal_max):
        generation_count += 1
        print("Generation : %s Fittest : %s " % (generation_count, my_pop.fitness_of_the_fittest()))
        my_pop = Algorithm.evolve_population(my_pop)
        if (my_pop.fitness_of_the_fittest() == old_fitness):
                equal_count = equal_count +1
        if (my_pop.fitness_of_the_fittest() != old_fitness):
                equal_count = 0
        old_fitness = my_pop.fitness_of_the_fittest()

my_fittest = my_pop.get_fittest()

AA=0
for i in range(Individual.DefaultGeneLength-29,0,-1):
        j = Individual.DefaultGeneLength-i-29
        AA = AA + my_fittest.genes[i]*(2**j)
AA = AA*100/(2**14-1)
AA = round(AA,2)

BB=0
for i in range(Individual.DefaultGeneLength-15,14,-1):
        j = Individual.DefaultGeneLength-i-15
        BB = BB + my_fittest.genes[i]*(2**j)
BB = BB*100/(2**14-1)
BB = round(BB,2)

CC=0
for i in range(Individual.DefaultGeneLength-1,28,-1):
        j = Individual.DefaultGeneLength-i-1
        CC = CC + my_fittest.genes[i]*(2**j)
CC = CC*100/(2**14-1)
CC = round(CC,2)

goodperiod = float(Population.starperiod)
percenterror = 100*math.fabs(goodperiod-BB)/goodperiod

print("\n\nStar = ", Population.starname, "Expected Period = ",Population.starperiod,"\n")
print("Solution found !\nGeneration : %s  equal_count: %s  Fitness: %s \n  amp, period, phase = " % (generation_count + 1,equal_count, my_pop.fitness_of_the_fittest()),AA, BB, CC,"\n")
print("percent error = ",percenterror)

#print("Genes of the Fittest : %s " % (genes_the_fittest))

d = datetime.today()

goodperiod = float(Population.starperiod)
percenterror = 100*math.fabs(goodperiod-BB)/goodperiod

f = open(Population.starname+'_'+d.strftime("%Y%m%d_%I%M%p")+'.txt','w')
f.write('star: '+Population.starname+'\n')
f.write('period: '+Population.starperiod+' days \n\n')
f.write('settings:'+'\n')
f.write('mutation rate = '+str(Algorithm.Mutation_rate)+'\n')
f.write('uniform rate = '+str(Algorithm.Uniform_rate)+'\n\n')
f.write('Solution found:'+'\n')
f.write('gencount = '+str(generation_count)+' of genmax = '+str(gen_max)+'\n')
f.write('equalcount = '+str(equal_count)+' of equalmax = '+str(equal_max)+'\n\n')
f.write('fitness value = '+str(my_pop.fitness_of_the_fittest())+'\n\n')
f.write('Results:'+'\n')
f.write('amplitude = '+str(AA)+'\n')
f.write('period = '+str(BB)+' days   with percent error= '+str(percenterror)+'\n')
f.write('phase = '+str(CC)+'\n')
f.close()
    
