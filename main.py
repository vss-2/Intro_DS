# Importamos a biblioteca numpy como np para calculos
import numpy as np

# Podemos tambem usar apenas um pedaco da biblioteca
From numpy import array

# Vamos criar duas listas
altura = [1.72, 1.55, 1.45, 1.65, 1.78]
peso = [85.5, 48.0, 78.5, 88.2, 65.7]

# Criando array de alturas, para nao usar listas:

# Para caso de import numpy as np
npAltura  = np.array(altura)

# Para caso de From numpy import array
npAltura2 = array(altura)

npPeso = np.array(peso)
npPeso2 = array(peso)

# Se colocamos para printar ele fara todos, como se houvesse um for 

IMC = npPeso / npAltura ** 2
print(IMC)
