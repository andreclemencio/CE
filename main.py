from tsp import *
import time
from utils import *
#from stats import *

if __name__ == '__main__':
	numb_generations = 250
	size_pop = 50
	prob_mut = 0.1
	prob_cross = 0.8
	k_tour = 3
	k_elite = 0.1
	sel_parents = tour_sel(k_tour)
	recombination = order_cross
	mutation = muta_swap
	sel_survivors = sel_survivors_elite(k_elite)

	numb_runs = 1

	coord = le_coordenadas_tsp('uy734.tsp')
	dicio = dicio_cidades(coord)
	meu_merito = merito(dicio)
	fitness_func = meu_merito
	size_cromo = len(dicio)

	start = time.time()
	boa,average_best = run(numb_runs,numb_generations-1,size_pop,size_cromo,prob_mut,prob_cross,sel_parents,recombination,mutation,sel_survivors,fitness_func)
	end = time.time()


	print (end - start)
	display_stat_n(boa,average_best)