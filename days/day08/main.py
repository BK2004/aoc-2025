from utils.grid import *
from utils.sorts import *
from utils.jaggedgrid import *
from utils.graph import *
from utils.linkedlist import *

def MakeSet(x):
	x.parent = x
	x.v = x.idx
	x.rank   = 0
	x.size   = 1

def Union(x, y):
	xRoot = Find(x)
	yRoot = Find(y)
	if xRoot.rank > yRoot.rank:
		yRoot.parent = xRoot
		xRoot.size += yRoot.size
	elif xRoot.rank < yRoot.rank:
		xRoot.parent = yRoot
		yRoot.size += xRoot.size
	elif xRoot != yRoot: # Unless x and y are already in same set, merge them
		yRoot.parent = xRoot
		xRoot.rank = xRoot.rank + 1
		xRoot.size += yRoot.size

def Find(x):
     if x.parent == x:
        return x
     else:
        x.parent = Find(x.parent)
        return x.parent
	 
def dist(p1, p2):
	return (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2 + (p2[2] - p1[2]) ** 2

class Node:
	def __init__(self, idx):
		self.idx = idx

def part1(filename: str):
	NUM_PAIRS = 1000
	NUM_MULTIPLICANDS = 3
	points = []
	with open(filename) as f:
		for l in f.readlines():
			l = l.strip()
			[x, y, z] = l.split(",")
			points.append((int(x), int(y), (int(z))))

	nodes = [Node(i) for i in range(len(points))]
	[MakeSet(node) for node in nodes]

	# Get distances between pairs
	dists = []
	for i in range(len(points)):
		for j in range(i+1, len(points)):
			dists.append((dist(points[i], points[j]), i, j))
	dists = sorted(dists)

	for d in range(NUM_PAIRS):
		_, i, j = dists[d]
		if Find(nodes[i]) == Find(nodes[j]):
			continue
		else:
			# Combine
			Union(nodes[i], nodes[j])
	sets = [Find(x) for x in nodes]
	ordered_sets = [(i, sets[i]) for i in range(len(points))]
	ordered_sets = sorted(ordered_sets, key=lambda x:x[1].size, reverse=True)
	res = 1
	used = set()
	m = 0
	while len(used) < NUM_MULTIPLICANDS:
		if Find(nodes[ordered_sets[m][0]]).v in used:
			m += 1
			continue
		res *= ordered_sets[m][1].size
		used.add(Find(nodes[ordered_sets[m][0]]).v)
		m += 1
	return res


def part2(filename: str):
	points = []
	with open(filename) as f:
		for l in f.readlines():
			l = l.strip()
			[x, y, z] = l.split(",")
			points.append((int(x), int(y), (int(z))))

	nodes = [Node(i) for i in range(len(points))]
	[MakeSet(node) for node in nodes]

	# Get distances between pairs
	dists = []
	for i in range(len(points)):
		for j in range(i+1, len(points)):
			dists.append((dist(points[i], points[j]), i, j))
	dists = sorted(dists)

	s = len(nodes)
	for d in range(len(dists)):
		_, i, j = dists[d]
		if Find(nodes[i]) == Find(nodes[j]):
			continue
		else:
			# Combine
			Union(nodes[i], nodes[j])
			s -= 1
			if s == 1:
				return points[i][0] * points[j][0]
