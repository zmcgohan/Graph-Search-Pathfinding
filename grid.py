class Grid:
	"""Represents a grid map stored in a tuple of tuples."""
	def __init__(self, filename):
		grid_li = []
		with open(filename, 'r') as f:
			for line in f:
				temp = []
				for c in line:
					if c == ' ':
						temp.append(None) # blank space
					elif c == '0':
						temp.append(0) # 0s are regular terrain
					elif c == '1':
						temp.append(1) # 1s are objects
				grid_li.append(temp)
		max_row_length = max([len(row) for row in grid_li])
		for row in grid_li:
			if len(row) < max_row_length:
				row.append(None * (max_row_length - len(row)))
		self.grid = tuple(tuple(row) for row in grid_li)
	def __str__(self):
		return '\n'.join([''.join([' ' if x is None else str(x) for x in row]) for row in self.grid])
	def get_adjacent_positions(self, pos):
		adjacent_positions = []
		if pos[0]-1 >= 0 and self.grid[pos[0]-1][pos[1]] == 0:
			adjacent_positions.append((pos[0]-1,pos[1]))
		if pos[0]+1 < len(self.grid) and self.grid[pos[0]+1][pos[1]] == 0:
			adjacent_positions.append((pos[0]+1,pos[1]))
		if pos[1]-1 >= 0 and self.grid[pos[0]][pos[1]-1] == 0:
			adjacent_positions.append((pos[0], pos[1]-1))
		if pos[1]+1 < len(self.grid[0]) and self.grid[pos[0]][pos[1]+1] == 0:
			adjacent_positions.append((pos[0], pos[1]+1))
		return adjacent_positions
	def display_path(self, path):
		"""Prints the grid with a path displayed with 8's."""
		path_positions = set(path.path_positions)
		display_str = ''
		for row in xrange(len(self.grid)):
			for col in xrange(len(self.grid[row])):
				if (row, col) in path_positions: display_str += '8'
				elif self.grid[row][col] is None: display_str += ' '
				elif self.grid[row][col] == 1: display_str += '1'
				elif self.grid[row][col] == 0: display_str += '0'
			display_str += '\n'
		print display_str
