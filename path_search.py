from path_node import PathNode

def get_path(grid, init_pos, end_pos):
	"""Returns a Path on grid from init_pos to end_pos."""
	past_positions = set()
	init_node = PathNode(init_pos)
