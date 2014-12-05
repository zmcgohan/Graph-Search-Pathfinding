class PathNode:
	"""Represents a node for the tree used to find a path on a Grid."""
	def __init__(self, pos, parent=None):
		self.pos = pos
		self.parent = parent
		if parent is not None:
			self.path_cost = self.parent.path_cost + 1
		else:
			self.path_cost = 0
	def __str__(self):
		if self.parent is not None:
			return "({},{})<-({},{})".format(
					str(self.parent.pos[0]), str(self.parent.pos[1]), str(self.pos[0]), str(self.pos[1]))
		else:
			return "None<-({},{})".format(self.pos[0], self.pos[1])
	def get_initial(self):
		initial_node = self
		while initial_node.parent != None:
			initial_node = initial_node.parent
		return initial_node
	def hashcode(self):
		return "{},{}".format(*self.pos)
