from tkinter import *
from functools import reduce
from time import sleep

# Tamanho de cada quadrado
qdd_larg = 10 
qdd_alt = 10

# Tamanho do grid que contém os quadrados
grid_alt = 10
grid_larg = 10

objetivo = []
posinicial = []

def criarQuadrado(janela, cor, linha, coluna):
	quadrado = Canvas(janela, width=qdd_larg, height=qdd_alt, background=cor)
	quadrado.grid(row=linha, column=coluna)
	return

def estaNoGrid(x, y):
	if(x > -1 and x < grid_larg and y > -1 and y < grid_alt):
		print('Está dentro do grid: ', x, y)
		return True
	else:
		print('Não está dentro do grid: ', x, y)
		return False

def menorDistancia(x, y, objetivo):
	return ((objetivo[0] - a)**2 + (objetivo[1] - b)**2)**(1/2)

def custoUniforme(x, y, objetivo, lista_MD, lista, janela):
	for a in range(x-1, x+2):
		for b in range(y-1, y+2):
			lista_MD.append(menorDistancia(a, b, objetivo))
			lista.append([a,b])
			if(a == objetivo[0] and b == objetivo[1]):
				print('Achei o objetivo')
				return
			else:
				menor = reduce(lambda i, j: min(i, j), lista_MD)
				parXY = lista[lista_MD.index(menor)]
		
	custoUniforme(parXY[0], parXY[1], objetivo, lista_MD, lista, janela)
	return
				
			

def dfs(x, y, objetivo, pilha, visitados, janela):
	print('Centro: ', x, y)
	criarQuadrado(janela, 'yellow', x, y)
	for a in range(x-1, x+2):
		for b in range(y-1, y+2):
			if (estaNoGrid(a,b) and ([a,b] not in visitados)):
				pilha.append([a,b])
				if(a == objetivo[0] and b == objetivo[1]):
					print('Achei o objetivo')
					return
	parXY = pilha.pop()
	dfs(parXY[0], parXY[1], objetivo, pilha, visitados, janela)
	return

def bfs(x, y, objetivo, fila, janela):
	print('Centro: ', x, y)
	for a in range(x-1, x+2):
		for b in range(y-1, y+2):
			if(estaNoGrid(a,b)):
				criarQuadrado(janela, 'yellow', a, b)
				if [a,b] not in fila:
					fila.append([a,b])
				if (a == objetivo[0] and b == objetivo[1]):
					print('Achei o objetivo')
					return
				print(fila)
				# sleep(3)
				# janela.mainloop()
		
	if(len(fila) > 0):
		#bfs(fila[0], fila[1], objetivo, fila, janela)
		parXY = fila.pop(0)
		bfs(parXY[0], parXY[1], objetivo, fila, janela)

def main():
	objetivo = [int(i) for i in input('Defina o objetivo (verde) x e y: \n').split(' ')]
	posinicial = [int(i) for i in input('Defina a posição inicial (azul) x e y: \n').split(' ')]
	base = Tk()
	for i in range(0,grid_larg):
		for j in range(0,grid_alt):
			criarQuadrado(base, 'red', i, j)
	criarQuadrado(base, 'green', objetivo[0], objetivo[1])
	criarQuadrado(base, 'blue', posinicial[0], posinicial[0])
	fila, pilha, visitados = []
	bfs(posinicial[0], posinicial[1], objetivo, fila, base)
	dfs(posinicial[0], posinicial[1], objetivo, pilha, visitados, base)
	custoUniforme(posinicial[0], posinicial[1], objetivo, [], [], janela)
	base.mainloop()

main()
