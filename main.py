import sys

from grid import Grid
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
	print grid
	path = Path(grid, (4,0), (4,5))
	print path
	grid.display_path(path)
