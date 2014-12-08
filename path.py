import time
from collections import deque

from path_node import PathNode

class Path:
	def __init__(self, grid, init_pos, end_pos, method=0):
		methods = ["Graph Search", "Bidirectional Graph Search"]
		self.method = methods[method]
		start_time = time.clock()
		if method == 0:
			end_node = self.__get_node_path(grid, init_pos, end_pos)
			self.path_positions = self.__get_path_positions(end_node) if end_node is not None else None
		elif method == 1:
			end_nodes = self.__get_node_path_bidirectional(grid, init_pos, end_pos)
			self.path_positions = self.__get_path_positions_bidirectional(end_nodes[0], end_nodes[1]) if end_nodes is not None else None
		self.time_taken = time.clock() - start_time
	def __get_node_path(self, grid, init_pos, end_pos):
		past_nodes = set()
		init_node = PathNode(init_pos)
		frontier = deque([init_node])
		while len(frontier) > 0:
			cur_node = frontier.popleft()
			if cur_node.pos == end_pos: return cur_node
			past_nodes.add(cur_node)
			for pos in grid.get_adjacent_positions(cur_node.pos):
				adjacent_node = PathNode(pos, cur_node)
				if adjacent_node not in past_nodes and adjacent_node not in frontier:
					frontier.append(adjacent_node)
		return None
	def __get_path_positions(self, end_node):
		temp_positions = []
		cur_node = end_node
		while cur_node.parent is not None:
			temp_positions.append(cur_node.pos)
			cur_node = cur_node.parent
		temp_positions.append(cur_node.pos)
		return tuple(reversed(temp_positions))
	def __get_node_path_bidirectional(self, grid, init_pos, end_pos):
		"""Bidirectionally searches for a path."""
		past_a_nodes = set()
		past_b_nodes = set()
		init_a_node = PathNode(init_pos)
		init_b_node = PathNode(end_pos)
		frontier_a = deque([init_a_node])
		frontier_b = deque([init_b_node])
		while len(frontier_a) > 0 or len(frontier_b) > 0:
			cur_a_node = frontier_a.popleft()
			cur_b_node = frontier_b.popleft()
			past_a_nodes.add(cur_a_node)
			past_b_nodes.add(cur_b_node)
			if cur_b_node in past_a_nodes: 
				for elem in past_a_nodes:
					if elem.pos == cur_b_node.pos:
						return (elem, cur_b_node)
			elif cur_a_node in past_b_nodes:
				for elem in past_b_nodes:
					if elem.pos == cur_a_node.pos:
						return (cur_a_node, elem)
			for pos in grid.get_adjacent_positions(cur_a_node.pos):
				adjacent_node = PathNode(pos, cur_a_node)
				if adjacent_node not in past_a_nodes and adjacent_node not in frontier_a:
					frontier_a.append(adjacent_node)
			for pos in grid.get_adjacent_positions(cur_b_node.pos):
				adjacent_node = PathNode(pos, cur_b_node)
				if adjacent_node not in past_b_nodes and adjacent_node not in frontier_b:
					frontier_b.append(adjacent_node)
		return None
	def __get_path_positions_bidirectional(self, node1, node2):
		node2_nodes = []
		cur_node = node2
		while cur_node.parent is not None:
			cur_node = cur_node.parent
			node2_nodes.append(cur_node.pos)
		cur_parent = node1
		for pos in node2_nodes:
			node1 = PathNode(pos, cur_parent)
			cur_parent = node1
		return self.__get_path_positions(node1)
	def __str__(self):
		return ', '.join(['({}, {})'.format(x, y) for x, y in self.path_positions]) + ' (Cost: {})'.format(len(self.path_positions))
	def is_complete(self):
		"""Returns if the Path is complete. If a route couldn't be found between the two points on initialization, returns False. Otherwise returns True."""
		return self.path_positions is not None
