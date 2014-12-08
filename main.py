import sys

from grid import Grid, RandomGrid
from path import Path

PRINT_GRID = True

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print "Filename for Grid must be supplied."
		print "Example: python main.py test_grid.txt"
		sys.exit(1)

	try:
		grid = Grid(sys.argv[1])
	except IOError as e:
		print "Error reading {}: {}".format(sys.argv[1], e.strerror)
		sys.exit(1)
	except Exception as e:
		print e
	rand_grid = RandomGrid(10,10,4,4)
	print "Random grid created. Starting searches...\n"
	while 1:
		start_pos = rand_grid.get_random_position()
		end_pos = rand_grid.get_random_position()
		graph_search_path = Path(rand_grid, start_pos, end_pos, 0)
		while not graph_search_path.is_complete():
			print "No path found for {} to {}".format(start_pos, end_pos)
			start_pos = rand_grid.get_random_position()
			end_pos = rand_grid.get_random_position()
			graph_search_path = Path(rand_grid, start_pos, end_pos)
		bidirectional_path = Path(rand_grid, start_pos, end_pos, 1)
		iterative_deepening_path = Path(rand_grid, start_pos, end_pos, 2)
		if PRINT_GRID:
			rand_grid.display_path(graph_search_path)
			print
			rand_grid.display_path(bidirectional_path)
			rand_grid.display_path(iterative_deepening_path)
		else:
			print "Path found from {} to {}".format(start_pos, end_pos)
			print "Graph search path length: {}; time taken: {}s".format(len(graph_search_path.path_positions) - 1, graph_search_path.time_taken)
			print "Bidirectional path length: {}; time taken: {}s".format(len(bidirectional_path.path_positions) - 1, bidirectional_path.time_taken)
			print "Iterative deepening path length: {}; time taken: {}s".format(len(iterative_deepening_path.path_positions) - 1, iterative_deepening_path.time_taken)
		raw_input()
