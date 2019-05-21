from sea_perm import *
import numpy as np

# fitness
def merito():
	def merito_(indiv):
		return evaluate(indiv)
	return merito_

#[9,3,5,4,1,6,7,2,8] (por exemplo)
def evaluate(solution):
	viola = 0
	matrix = []
	for i in range(len(solution)):
		row = []
		for j in range(len(solution)):
			if solution[i]-1 == j:
				row.append(1)
			else:
				row.append(0)
		matrix.append(row) 

	#Buscar todas as diagonais da matriz
	matrix = np.array(matrix)
	diags = [matrix[::-1,:].diagonal(i) for i in range(-matrix.shape[0]+1,matrix.shape[1])]
	diags.extend(matrix.diagonal(i) for i in range(matrix.shape[1]-1,-matrix.shape[0],-1))
	
	diagonals = [n.tolist() for n in diags]

	#Contar violações
	for i in range (len(diagonals)):
		count = 0
		for j in range(len(diagonals[i])):
			if diagonals[i][j] == 1:
				count += 1

		if count > 1:
			viola +=  (count * (count-1))

	return viola

if __name__ == '__main__':
	pass