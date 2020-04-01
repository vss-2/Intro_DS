import os
import numpy as np
import matplotlib.pyplot as mp
import csv

pais  = []
total = []

def qualMaior(pais, total):
        maior = 0
        posicao = 0
        contador = 0
        for valor in total:
                if(valor > maior):
                        maior = valor
                        posicao = contador
                contador = contador + 1
        
        oPais = pais[posicao]
        oTotal = total[posicao]
        pais.remove(pais[posicao])
        total.remove(total[posicao])
        return (oPais, oTotal)


def montarGrafico():
        with open(os.getcwd()+'src/ImpSuco.csv') as csvfile:
                lerArquivo = csv.reader(csvfile, delimiter = ';')
                for row in lerArquivo:
                        somatorio = 0
                        # Calcula o valor de cada país
                        for valor in row:
                                if(type(valor) == type('a')):
                                        pais.append(valor)
                                        continue
                                else:
                                        somatorio = somatorio + valor
                        total.append(somatorio)

                        os5maiores = ('', 0)
                        paises = []
                        for x in range(0,5):
                                os5maiores = qualMaior(pais, total)
                                paises.append(os5maiores)
                csvfile.close()
                return

if __name__ == "__main__":
        montarGrafico()