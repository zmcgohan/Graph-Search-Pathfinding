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
