
# Importando duas bibliotecas, de variacao uniforme
# e biblioteca de random inteiro

from random import uniform
from random import randint


# Importando biblioteca de diretorio atual

import os

texto = []


# Gerador de 100 valores de altura e peso
# A altura varia de 1.5 a 2.2
# O peso varia de 50 a 120
# Temos um inteiro aleatorio de 0 a 10

def obterTexto():
      for x in range[1,100]:
            texto.append(str(uniform(1.50, 2.20)) + ';' +  
            str(inform(50, 120)) + ';' + str(randint(0, 10)) + '\n')


# Pegamos o diretorio
# Damos a entrada a o lugar de gravar, permissoes, e codificacao
# O codigo de diretorio foi corrigido para aceitar Windows, Mac e Linux

def gerarArquivo():
      diretorio = r'%s' % os.getcwd().replace('\\','/')
      entrada = open(diretorio, 'w+', encoding = 'UTF-8')
      obterTexto()
      entrada.writelines(texto)
      entrada.close()

if __name__ == '__main__':
      gerarArquivos()
