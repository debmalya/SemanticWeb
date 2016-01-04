# This is to create simple graph containing subject, property, object.
class SimpleGraph:
	'''
	cross indexing the subject, predicate (property) and object.
	'''
	def __init__(self):
		self.spo = {}
		self.pos = {}
		self.osp = {}

	'''
	Adding to index
	'''
	def _addToIndex(self,index,a,b,c):
		if a not in index: index[a] = {b:set([c])}
		else:
			if b not in index[a]: index[a][b] = set([c])
			else: 
				index[a][b].add(c)
