class Especie:

	def __init__(self, gen, fit):
		self.geracao = int(gen)
		self.val_fit = int(fit)

	def getInfo(self):
		return (self.geracao, self.val_fit)

