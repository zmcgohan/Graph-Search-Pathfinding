from collections import deque

from path_node import PathNode

class Path:
	def __init__(self, grid, init_pos, end_pos):
		end_node = self.__get_node_path(grid, init_pos, end_pos)
		self.path_positions = self.__get_path_positions(end_node) if end_node is not None else None
	def __get_node_path(self, grid, init_pos, end_pos):
		past_positions = set(init_pos)
		init_node = PathNode(init_pos)
		frontier = deque(PathNode(pos, init_node) for pos in grid.get_adjacent_positions(init_pos))
		for node in frontier:
			past_positions.add(node.pos)
		while len(frontier) > 0:
			cur_node = frontier.popleft()
			if cur_node.pos == end_pos: return cur_node
			for pos in grid.get_adjacent_positions(cur_node.pos):
				if pos not in past_positions:
					past_positions.add(pos)
					frontier.append(PathNode(pos,cur_node))
			#[frontier.append(PathNode(pos,cur_node)) for pos in grid.get_adjacent_positions(cur_node.pos) if pos not in past_positions]
		return None
	def __get_path_positions(self, end_node):
		temp_positions = []
		cur_node = end_node
		while cur_node.parent is not None:
			temp_positions.append(cur_node.pos)
			cur_node = cur_node.parent
		temp_positions.append(cur_node.pos)
		return tuple(reversed(temp_positions))
	def __str__(self):
		return ', '.join(['({}, {})'.format(x, y) for x, y in self.path_positions]) + ' (Cost: {})'.format(len(self.path_positions))
	def is_complete(self):
		"""Returns if the Path is complete. If a route couldn't be found between the two points on initialization, returns False. Otherwise returns True."""
		return self.path_positions is not None
