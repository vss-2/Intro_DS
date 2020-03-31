import os
import numpy as np
import matplotlib.pyplot as mp
import csv

pais   = []
quant  = []
preco  = []
ano = 2018

# O CSV da Embrapa está no formato:
# NUM | PAIS | QUANT(ANO X) | VALOR(ANO X) | QUANT(ANO X+1) | VALOR(ANO X+1) ...
# Portato, analisarei apenas a partir da coluna 2 e 3 de cada ano

def minerarDados():
        with open(os.getcwd()+'/src/ImpSuco.csv') as csvfile:
                lerArquivo = csv.reader(csvfile, delimiter = ';')
                for row in lerArquivo:
                        # Pular as duas primeiras linhas
                        if(row[0] == ''):
                                continue
                        else:
                                if(float(row[(ano-1970)*2]) > 0):
                                        pais.append(row[1])
                                        quant.append(int(row[(ano-1970)*2]))
                                        preco.append(int(row[(ano-1970)*2+1]))
                return


def plotarGrafico():
        def mostrarValorCol(colunas):
                for coluna in colunas:
                        altura = coluna.get_height()
                        ax.text(coluna.get_x() + coluna.get_width()/2, altura, int(altura), ha = 'center', va = 'bottom')

        quantPais = np.arange(len(pais))
        espacoEntreCol = 0.3

        # Para desenhar figuras
        figura, ax = mp.subplots()

        colunaQuant = ax.bar(quantPais, quant, espacoEntreCol, color = 'b', align = 'center')
        colunaPreco = ax.bar(quantPais+espacoEntreCol, preco, espacoEntreCol, color = 'g', align = 'center')

        ax.set_ylabel('Valor')
        ax.set_title('Embrapa: Importação de Suco de Uva: de 1970 a '+ str(ano))
        ax.set_xticks(quantPais + espacoEntreCol / 2)
        ax.set_xticklabels(pais)
        ax.legend((colunaQuant, colunaPreco), ('Quantidade', 'Preço'))
        mostrarValorCol(colunaQuant)
        mostrarValorCol(colunaPreco)
        mp.show()


if __name__ == "__main__":
    minerarDados()
    plotarGrafico()