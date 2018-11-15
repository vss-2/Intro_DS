# Importando biblioteca e diretorio atual

import numpy as np
import os


# Caracterizando os valores que serao colocados

def tabela(valIMC):
      if (valIMC < 16):
            return str(valIMC) + ': Magreza grave'
      elif (valIMC < 17):
            return str(valIMC) + ': Magreza moderada'
      elif (valIMC < 18.5):
            return str(valIMC) + ': Magreza leve'
      elif (valIMC < 25):
            return str(valIMC) + ': Saudavel'
      elif (valIMC < 30):
            return str(valIMC) + ': Sobrepeso'
      elif (valIMC < 35):
            return str(valIMC) + ': Obesidade Grau I'
      elif (valIMC < 40):
            return str(valIMC) + ': Obesidade Grau II (Severa)'
      else :
            return str(valIMC) + ': Obesidade Grau III (Morbida)'


# Os parametros sao:
# Local do arquivo
# Delimitador usado la no gerador
# Se houver mais de uma variavel para devemos "desempacotalas", e ha, entao True
# Tipo de dado

altura, peso, forca = np.loadtext(os.getcwd()+'\\peso.csv', delimiter=';', unpack = True, dtype = 'float')

# Se pedirmos para printar, observer que saira tudo organizado
print(altura)
