class Audi:
	def __init__(self):
		self.model = ['Audi q7', 'Audi a6', 'Audi a8', 'Audi a3']

	def putdata(self):
		print('These are the available models for Audi')
		for model in self.model:
			print('\t%s ' % model)
