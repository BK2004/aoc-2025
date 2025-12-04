from utils.grid import *
from utils.sorts import *
from utils.jaggedgrid import *
from utils.graph import *
from utils.linkedlist import *

def part1(filename: str):
	sum = 0
	with open(filename) as f:
		ids = f.read().split(",")
		for rng in ids:
			nums = rng.split("-")
			l, r = int(nums[0]), int(nums[1])

			for x in range(l, r+1):
				str_x = str(x)
				if len(str_x) % 2 == 1:
					continue

				if str_x[:len(str_x)//2] == str_x[len(str_x)//2:]:
					sum += x
	return sum

def part2(filename: str):
	sum = 0
	with open(filename) as f:
		ids = f.read().split(",")
		for rng in ids:
			nums = rng.split("-")
			l, r = int(nums[0]), int(nums[1])

			for x in range(l, r+1):
				y = str(x)
				for window_size in range(1, len(y)):
					if y == y[:window_size] * (len(y) // window_size):
						sum += x
						break
	return sum
