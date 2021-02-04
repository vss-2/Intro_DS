import os
import numpy as np
import matplotlib.pyplot as mp

# Definindo os eixos
# Y o matplot que vai moldar
# X eu quero que contenha apenas 5 ranges
y = [] 
x = [1,2,3,4,5]

altura, peso, forca = np.loadtxt(os.getcwd()+'/dados.csv', delimiter = ';', unpack = True, dtype = 'float')

imc = peso / altura ** 2

y.append(np.median(np.percentile(imc, q=range(0,20)))
y.append(np.median(np.percentile(imc, q=range(21,40)))
y.append(np.median(np.percentile(imc, q=range(41,60)))
y.append(np.median(np.percentile(imc, q=range(61,80)))
y.append(np.median(np.percentile(imc, q=range(81,100)))