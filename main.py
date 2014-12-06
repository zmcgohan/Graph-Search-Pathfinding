import sys

from grid import Grid, RandomGrid
from path import Path

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
	rand_grid = RandomGrid(150,20,4,4)
	while 1:
		start_pos = rand_grid.get_random_position()
		end_pos = rand_grid.get_random_position()
		path = Path(rand_grid, start_pos, end_pos)
		while not path.is_complete():
			print "No path found for {} to {}".format(start_pos, end_pos)
			start_pos = rand_grid.get_random_position()
			end_pos = rand_grid.get_random_position()
			path = Path(rand_grid, start_pos, end_pos)
		#print "Path found from {} to {}, length {}".format(start_pos, end_pos, len(path.path_positions))
		rand_grid.display_path(path)
		raw_input()
