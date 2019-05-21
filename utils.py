"""
Utilities for visualization
Ernesto Costa, February 2016
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# auxiliary 
def display(indiv, phenotype):
    print('Chromo: %s\nFitness: %s' % (phenotype(indiv[0]),indiv[1]))
    
def display_stat_1(best,average):
    generations = list(range(len(best)))
    plt.title('Performance over generations')
    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.plot(generations, best, label='Best')
    plt.plot(generations,average,label='Average')
    plt.legend(loc='best')
    plt.show()
    
def display_stat_n(boa,average_best):
    generations = list(range(len(boa)))
    plt.title('Performance over runs')
    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.plot(generations, boa, label='Best of All')
    plt.plot(generations,average_best,label='Average of Bests')
    plt.legend(loc='best')
    plt.show()
    
#Method to Read Files
def read_file(filename):
    f = open(filename, 'r')
    x = f.readlines()
    f.close()
    data = []
    for i in range(0,len(x)-1):
        data.append(float(x[i]))
    return data


#Make Boxplots
def box_plt_gr_tsp(swap_data, inversion_data, scramble_data):
    data_analyse = [swap_data, inversion_data, scramble_data]
    fig = plt.figure(1)
    ax = fig.add_subplot(111)
    ax.boxplot(data_analyse)
    ax.set_xticklabels(['SWAP', 'INV','SCRA'])
    plt.ylabel('TSP Benchmark')
    ax.set_yticks(np.arange(200000, 290000, 10000))
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    plt.show()   
    
def box_plt_gr_nqueens(swap_data, inversion_data, scramble_data):
    data_analyse = [swap_data, inversion_data, scramble_data]
    fig = plt.figure(2)
    ax = fig.add_subplot(111)
    ax.boxplot(data_analyse)
    ax.set_xticklabels(['SWAP', 'INV','SCRA'])
    plt.ylabel('NQUEENS Benchmark')
    ax.set_yticks(np.arange(30, 90, 10))
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    plt.show() 

#Just to check data (if follow normal distribution)
def histogram(data_analyse, title, x, y, bins = 30):
    fig = plt.figure(3)
    #fit =  stats.norm.pdf(data_analyse, np.mean(data_analyse), np.std(data_analyse))
    #plt.plot(data_analyse,fit,'-o')
    plt.hist(data_analyse, bins=bins)
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.show()
    
#Kolgomorov-Smirnov
def ks_test(data_analyse):
    norm_data = (data_analyse - np.mean(data_analyse))/(np.std(data_analyse)/np.sqrt(len(data_analyse)))
    return stats.kstest(norm_data, 'norm')    

#Shapiro-Wilk
def sw_test(data_analyse):
    norm_data = (data_analyse - np.mean(data_analyse))/(np.std(data_analyse)/np.sqrt(len(data_analyse)))
    return stats.shapiro(norm_data)

#Levene
def levene(swap, inversion, scramble):
    output = stats.levene(swap, inversion, scramble, center='mean')
    return output
    
#Kruskal-Wallis
def kruskalwallis(swap, inversion, scramble):
    output = stats.kruskal(swap,inversion,scramble)

#Mann Whitney
def mann_whitney(data1, data2):
    return stats.mannwhitneyu(data1, data2)

    
if __name__ == '__main__':
    pass