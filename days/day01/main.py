from utils.grid import *
from utils.sorts import *
from utils.jaggedgrid import *
from utils.graph import *
from utils.linkedlist import *

def part1(filename: str):
	with open(filename, 'r') as f:
		data = f.read().strip().splitlines()
	
	x = 50
	out = 0
	for line in data:
		if line[0] == 'L':
			# left
			x = x - int(line[1:])
			if x < 0: x = (100 + (x % 100)) % 100
		else:
			# right
			x = (x + int(line[1:])) % 100
		if x == 0:
			out += 1
	
	return out

def part2(filename: str):
	with open(filename, 'r') as f:
		data = f.read().strip().splitlines()
	
	x = 50
	out = 0
	for line in data:
		# print("----\nbefore:", line, x, out)
		prev = x
		diff = int(line[1:])
		if line[0] == 'L':
			# left
			if diff >= prev and prev != 0:
				out += 1
				diff -= prev
				x = 0
			out += abs(diff) // 100
			diff = diff % 100
			x = x - diff
			if x < 0: x = (100 + (x % 100)) % 100
		else:
			# right
			if diff >= 100 - prev:
				out += 1
				diff -= (100 - prev)
				x = 0
			out += diff // 100
			diff = diff % 100
			x = (x + diff) % 100
		# print("after:", x, out)
	
	return out
