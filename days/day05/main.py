from utils.grid import *
from utils.sorts import *
from utils.jaggedgrid import *
from utils.graph import *
from utils.linkedlist import *

def fresh(ranges: list[int], id: int):
	for rang in ranges:
		if rang[0] <= id <= rang[1]:
			return True
	return False

def part1(filename: str):
	ranges = []
	ids = []
	with open(filename) as f:
		for line in f.readlines():
			line = line.strip()
			if line.find("-") > -1:
				# Range
				ranges.append([int(line[:line.find("-")]), int(line[line.find("-") + 1:])])
			elif len(line) == 0:
				continue
			else:
				ids.append(int(line))

	cnt = 0
	for id in ids:
		if fresh(ranges, id):
			cnt += 1

	return cnt

def part2(filename: str):
	ranges = []
	with open(filename) as f:
		for line in f.readlines():
			line = line.strip()
			if line.find("-") > -1:
				# Range
				ranges.append([int(line[:line.find("-")]), int(line[line.find("-") + 1:])])
			else:
				continue

	# run merge intervals, get length
	ranges = sorted(ranges, key=lambda x: x[0])
	curr = [-1, -2]
	out = 0
	for r in ranges:
		if r[0] <= curr[1]:
			curr[1] = max(r[1], curr[1])
		else:
			out += curr[1] - curr[0] + 1
			curr = [r[0], r[1]]

	return out + curr[1] - curr[0] + 1