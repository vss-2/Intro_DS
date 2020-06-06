from random import randint

class Especie:

        def __init__(self, gen, fit):
                self.geracao = int(gen)
                self.val_fit = int(fit)

        def getInfo(self):
                return (self.geracao, self.val_fit)

class Populacao:

	def __init__(self, qtd):
		self.esp_pop   = [None]*qtd
		self.atual_gen = 0
		for k in range(0, qtd):
			self.esp_pop[k] = Especie(str(0), randint(0,100))

	def selecionar(self, grupo, fit_min):
		# Elimina quem o fitness for menor que o esperado
		novoG = [None]*len(grupo)
		for i in range(0, len(grupo)):
			if(grupo[i].fit >= fit_min):
				novoG.append(grupo[i])
		# Reproduzir até o tamanho do novo grupo ser igual ao anterior
		reproduzir(len(grupo), novoG)
		return novoG

	def reproduzir(self, qtd, grupo):
		# Geração atual do grupo é incrementada
		# Reprodução é uma média dos pais aleatórios
		grupo.atual_gen += 1
		while(len(grupo) < qtd):
			valrand1, valrand2 = randint(0, len(grupo)), randint(0, len(grupo))
			grupo.append(Especie(grupo.atual_gen, grupo[valrand1] + grupo[valrand2])/2)

		return grupo
