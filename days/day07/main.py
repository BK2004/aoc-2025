from utils.grid import *
from utils.sorts import *
from utils.jaggedgrid import *
from utils.graph import *
from utils.linkedlist import *
import functools

g= None

def explore(g, v, row, col):
	if (row, col) not in g:
		return 0
	
	if (row, col) in v:
		return 0
	
	v.add((row, col))
	
	if g[row, col] == '^':
		return 1 + explore(g, v, row, col-1) + explore(g, v, row, col+1)
	else:
		return explore(g, v, row+1, col)


def part1(filename: str):
	g = None
	with open(filename) as f:
		g = Grid([l.strip() for l in f.readlines()])

	# Find start
	for c in range(g.width):
		if g[0, c] == 'S':
			break

	return explore(g, set([(0, c)]), 1, c)

@functools.lru_cache(maxsize=None)
def explore2(row, col):
	global g
	if row == g.height - 1:
		return 1
	
	if (row, col) not in g:
		return 0
	
	if g[row, col] == '^':
		return explore2(row, col-1) + explore2(row, col+1)
	else:
		return explore2(row+1, col)
	

def part2(filename: str):
	global g
	with open(filename) as f:
		g = Grid([l.strip() for l in f.readlines()])

	# Find start
	for c in range(g.width):
		if g[0, c] == 'S':
			break

	return explore2(1, c)
