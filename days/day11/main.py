from utils.grid import *
from utils.sorts import *
from utils.jaggedgrid import *
from utils.graph import *
from utils.linkedlist import *
from collections import deque

def count(curr, visited, edges):
	rec = 0
	for adj in edges[curr]:
		if adj == "out":
			rec += 1
		elif adj in visited:
			continue
		else:
			visited.add(adj)
			rec += count(adj, visited, edges)
			visited.remove(adj)
	return rec

def count2(src, edges, dest):
	if dest not in edges:
		edges[dest] = set()
	if src not in edges:
		edges[src] = set()
	# Topo-sort
	indeg = {}
	for k in edges:
		indeg[k] = 0
	indeg[dest], indeg[src] = 0, 0

	for k in edges:
		for trg in edges[k]:
			indeg[trg] += 1

	q = deque()
	for k in indeg:
		if indeg[k] == 0:
			q.append(k)
	
	topoOrder = []
	while q:
		node = q.popleft()
		topoOrder.append(node)

		for neighbor in edges[node]:
			indeg[neighbor] -= 1
			if indeg[neighbor] == 0:
				q.append(neighbor)
	
	# Ways to reach each node from src
	ways = {k: 0 for k in edges}
	ways[src] = 1
	ways[dest] = 0

	for node in topoOrder:
		for neighbor in edges[node]:
			ways[neighbor] += ways[node]
	return ways[dest]

def part1(filename: str):
	edges = {}
	with open(filename) as f:
		for line in f.readlines():
			line = line.strip()
			src = line[:line.find(":")]
			edges[src] = set()
			for to in line[line.find(":") + 2:].split(" "):
				edges[src].add(to)
	
	return count2("you", edges, "out")
	

def part2(filename: str):
	edges = {}
	with open(filename) as f:
		for line in f.readlines():
			line = line.strip()
			src = line[:line.find(":")]
			edges[src] = set()
			for to in line[line.find(":") + 2:].split(" "):
				edges[src].add(to)
				# Ensure all destination nodes exist in the dict
				if to not in edges:
					edges[to] = set()
	
	return count2("svr", edges, "fft") * count2("fft", edges, "dac") * count2("dac", edges, "out") + count2("svr", edges, "dac") * count2("dac", edges, "fft") * count2("fft", edges, "out")
