from tsp import *
import time
#from stats import *

if __name__ == '__main__':
    numb_generations = 2
    size_pop = 70
    prob_mut = 0.05
    prob_cross = 0.75
    k_tour = 3
    k_elite = 0.1
    sel_parents = tour_sel(k_tour)
    recombination = order_cross
    mutation = muta_swap
    sel_survivors = sel_survivors_elite(k_elite)
    #metric = hamming_distance

    numb_runs = 1

    coord = le_coordenadas_tsp('berlin52.tsp')
    dicio = dicio_cidades(coord)
    meu_merito = merito(dicio)
    fitness_func = meu_merito
    size_cromo = len(dicio)

    boa, average_best = run(numb_runs,numb_generations-1,size_pop,size_cromo,prob_mut,prob_cross,sel_parents,recombination,mutation,sel_survivors,fitness_func)

    print (boa,average_best)