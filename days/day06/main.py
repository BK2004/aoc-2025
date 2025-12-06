from utils.grid import *
from utils.sorts import *
from utils.jaggedgrid import *
from utils.graph import *
from utils.linkedlist import *

def part1(filename: str):
	g = None
	with open(filename) as f:
		lines = [l.strip().split() for l in f.readlines()]
		g = Grid(lines)

	sum = 0
	for c in range(g.width):
		tmp = 0 if g[-1, c] == '+' else 1
		for r in range(g.height - 1):
			tmp = tmp * int(g[r, c]) if g[-1, c] == '*' else tmp + int(g[r, c])
		sum += tmp
	return sum

def part2(filename: str):
	g = None
	with open(filename) as f:
		lines = f.readlines()
		lines = [l[:-1] if l[-1] == '\n' else l for l in lines]
		g = Grid(lines)

	for c in range(g.width):
		if c < g.width - 1 and g[-1, c + 1] in ['*', '+']:
			continue
		for r in range(g.height - 1):
			if g[r, c] == ' ':
				g[r, c] = '.'
	
	# Reset grid
	g = Grid([''.join(g[r]).split() for r in range(g.height)])
	
	# Transpose each column of numbers and do computations
	sum = 0
	for c in range(g.width):
		mult = g[-1, c] == '*'
		nums = g[:-1, c]
		transpose = [[0 for _ in range(len(nums))] for _ in range(len(nums[0]))]
		for row in range(len(nums)):
			for col in range(len(nums[0])):
				transpose[col][row] = nums[row][col]
		
		tmp = 1 if mult else 0
		for row in transpose:
			x = int(''.join(row).replace(".", ""))
			tmp = tmp * x if mult else tmp + x
		sum += tmp
		

	return sum
