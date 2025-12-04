from utils.grid import *
from utils.sorts import *
from utils.jaggedgrid import *
from utils.graph import *
from utils.linkedlist import *

def get_neighbors(g, r, c):
	dirs = [-1, 0, 1]
	for x in dirs:
		for y in dirs:
			if x == y == 0:
				continue
			neighbor = (x + r,y + c)
			if g.in_bounds(neighbor):
				yield neighbor

def can_access(g, r, c):
	cnt = 0
	for n in get_neighbors(g, r, c):
		if g[n] == '@':
			cnt += 1
	return cnt < 4

def remove(g):
	'''
	Remove as many toilet paper rolls as possible.
	Return # removed
	'''
	to_remove = []
	for (char, r, c) in g:
		if char == '@' and can_access(g, r, c):
			to_remove.append((r, c))
	for (r, c) in to_remove:
		g[r, c] = '.'
	
	return len(to_remove)

def part1(filename: str):
	g = None
	with open(filename, 'r') as f:
		lines = f.readlines()
		lines = [l.strip() for l in lines]
		g = Grid(lines)

	res = 0
	for (char, r, c) in g:
		if char == '@' and can_access(g, r, c):
			res += 1
	return res
	

def part2(filename: str):
	g = None
	with open(filename, 'r') as f:
		lines = f.readlines()
		lines = [l.strip() for l in lines]
		g = Grid(lines)

	res = 0
	removed = remove(g)
	while removed > 0:
		res += removed
		removed = remove(g)

	return res
