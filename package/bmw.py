class Bmw:
	def __init__(self):
		self.model = ['BWM i8', 'BMW x1', 'BMW x5', 'BMW x6']

	def putdata(self):
		print('These are the available models for BMW')
		for model in self.model:
			print('\t%s ' % model)
