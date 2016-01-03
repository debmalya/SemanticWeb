# This is to create simple graph containing subject, property, object.
class SimpleGraph:
	'''
	cross indexing the subject, predicate (property) and object.
	'''
	def __init__(self):
		self.spo = {}
		self.pos = {}
		self.osp = {}


