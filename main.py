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
	#Change variables mutation here
	mutation = muta_inversion

	sel_survivors = sel_survivors_elite(k_elite)

	numb_runs = 30

	coord = le_coordenadas_tsp('uy734.tsp')
	dicio = dicio_cidades(coord)
	meu_merito = merito(dicio)
	fitness_func = meu_merito
	size_cromo = len(dicio)


	filename = str(numb_generations)+'_'+str(size_pop)+'_'+str(prob_mut)+'_'+str(prob_cross)+'_'+str(k_tour)+'_'+str(k_elite)+'inversionmutation.txt'
	filename = 'data/'+filename

	run_for_file(filename,numb_runs,numb_generations-1,size_pop,size_cromo,prob_mut,prob_cross,sel_parents,recombination,mutation,sel_survivors,fitness_func)