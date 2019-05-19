from tsp import *
from n_queens import *
import time
from utils import *
import scipy.stats as stats
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
	mutation = muta_swap

	sel_survivors = sel_survivors_elite(k_elite)

	numb_runs = 30

	'''
	coord = le_coordenadas_tsp('uy734.tsp')
	dicio = dicio_cidades(coord)
	meu_merito = merito(dicio)
	fitness_func = meu_merito
	size_cromo = len(dicio)
	'''
	size_problem = 150

	meu_merito = merito()
	fitness_func = meu_merito
	size_cromo = size_problem


	#filename = str(numb_generations)+'_'+str(size_pop)+'_'+str(prob_mut)+'_'+str(prob_cross)+'_'+str(k_tour)+'_'+str(k_elite)+'swapmutation_nqueens.txt'
	#filename = 'data/'+filename

	#run_for_file(filename,numb_runs,numb_generations-1,size_pop,size_cromo,prob_mut,prob_cross,sel_parents,recombination,mutation,sel_survivors,fitness_func)
	
	swap_tsp = 'data/250_50_0.1_0.8_3_0.1swapmutation.txt'
	swap_nqueens = 'data/250_50_0.1_0.8_3_0.1swapmutation_nqueens.txt'
	inversion_tsp = 'data/250_50_0.1_0.8_3_0.1inversionmutation.txt'
	inversion_nqueens = 'data/250_50_0.1_0.8_3_0.1inversionmutation_nqueens.txt'
	scramble_tsp = 'data/250_50_0.1_0.8_3_0.1scramblemutation.txt'
	scramble_nqueens = 'data/250_50_0.1_0.8_3_0.1scramblemutation_nqueens.txt'
	
	
	swap_tsp_data = read_file(swap_tsp)
	swap_nqueens_data = read_file(swap_nqueens)
	inversion_tsp_data = read_file(inversion_tsp)
	inversion_nqueens_data = read_file(inversion_nqueens)
	scramble_tsp_data = read_file(scramble_tsp)
	scramble_nqueens_data = read_file(scramble_nqueens)
	
	#BOXPLOTS
	box_plt_gr_tsp(swap_tsp_data, inversion_tsp_data, scramble_tsp_data)
	box_plt_gr_nqueens(swap_nqueens_data, inversion_nqueens_data, scramble_nqueens_data)
	
	#HISTOGRAMS
	#histogram(swap_tsp_data, 'Swap Mutation TSP', 'Fitness','')
	#histogram(inversion_tsp_data, 'Inversion Mutation TSP', 'Fitness','')
	#histogram(scramble_tsp_data, 'Scramble Mutation TSP', 'Fitness','')
	#histogram(swap_nqueens_data, 'Swap Mutation Nqueens', 'Fitness','')
	#histogram(inversion_nqueens_data, 'Inversion Mutation Nqueens', 'Fitness','')
	#histogram(scramble_nqueens_data, 'Scramble Mutation Nqueens', 'Fitness','')
	
	#Testar se podemos realizar testes paramétricos
	#Kolgomorov-Smirnov
	print("Teste Paramétrico [KS] para [SWAP-TSP]: ")
	data_test = ks_test(swap_tsp_data)
	print(data_test)
	print("Teste Paramétrico [KS] para [INVERSION-TSP]: ")
	data_test = ks_test(inversion_tsp_data)
	print(data_test)
	print("Teste Paramétrico [KS] para [SCRAMBLE-TSP]: ")
	data_test = ks_test(scramble_tsp_data)
	print(data_test)
	
	print("Teste Paramétrico [KS] para [SWAP-NQUEENS]: ")
	data_test = ks_test(swap_nqueens_data)
	print(data_test)
	print("Teste Paramétrico [KS] para [INVERSION-NQUEENS]: ")
	data_test = ks_test(inversion_nqueens_data)
	print(data_test)
	print("Teste Paramétrico [KS] para [SCRAMBLE-NQUEENS]: ")
	data_test = ks_test(scramble_nqueens_data)
	print(data_test)
	
	#Shapiro-Wilk
	print("Teste Paramétrico [SH] para [SWAP-TSP]: ")
	data_test = sw_test(swap_tsp_data)
	print(data_test)
	print("Teste Paramétrico [SH] para [INVERSION-TSP]: ")
	data_test = sw_test(inversion_tsp_data)
	print(data_test)
	print("Teste Paramétrico [SH] para [SCRAMBLE-TSP]: ")
	data_test = sw_test(scramble_tsp_data)
	print(data_test)
	
	print("Teste Paramétrico [SH] para [SWAP-NQUEENS]: ")
	data_test = sw_test(swap_nqueens_data)
	print(data_test)
	print("Teste Paramétrico [SH] para [INVERSION-NQUEENS]: ")
	data_test = sw_test(inversion_nqueens_data)
	print(data_test)
	print("Teste Paramétrico [SH] para [SCRAMBLE-NQUEENS]: ")
	data_test = sw_test(scramble_nqueens_data)
	print(data_test)
	
	#Levene Teste
	levene_output = levene(swap_tsp_data, inversion_tsp_data, scramble_tsp_data)
	print(levene_output)
	levene_output = levene(swap_nqueens_data, inversion_nqueens_data, scramble_nqueens_data)
	print(levene_output)
	
	#Kruskal-Wallis
	print(stats.kruskal(swap_tsp_data, inversion_tsp_data, scramble_tsp_data))
	
	