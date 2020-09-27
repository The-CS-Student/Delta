import numpy as np 

class Tensor:
	def __init__(self,x,y):
		self.dimensions = (x,y)
	def assign(self,value):
		self.value = np.array(value)