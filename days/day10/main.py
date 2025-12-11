from utils.grid import *
from utils.sorts import *
from utils.jaggedgrid import *
from utils.graph import *
from utils.linkedlist import *
from collections import deque
from scipy.optimize import linprog

def solve(machine: tuple[str, list[int]]):
	goal, buttons = machine[0], machine[1]
	g = int(goal.replace(".", "0").replace("#", "1"), base=2)
	dp = [-1] * (2**len(goal))
	dp[0] = 0

	q = deque([(0, 0)]) # (curr, steps)
	while q:
		(curr, steps) = q.popleft()
		for b in buttons:
			new = curr ^ b
			if dp[new] > -1:
				continue
			else:
				q.append((new, steps + 1))
				dp[new] = steps + 1
				if new == g:
					return dp[new]

def part1(filename: str):
	machines = []
	with open(filename) as f:
		for line in f.readlines():
			line = line.strip()
			segments = line.split(" ")
			goal = segments[0][1:-1][::-1]
			buttons = []
			for b in segments[1:-1]:
				comb_or = 0
				for x in b[1:-1].split(","):
					comb_or = comb_or | (2**int(x))
				buttons.append(comb_or)
			machines.append((goal, buttons))

	return sum(solve(m) for m in machines)

def dot(x, y):
	# x, y are arrays of same length
	res = 0
	for i in range(len(x)):
		res += x[i] * y[i]
	return res

def solve2(m: tuple[list[list[int]], list[int]]):
	buttons, goals = m
	A = [[0 for _ in range(len(buttons))] for _ in range(len(goals))]
	for i in range(len(buttons)):
		for j in range(len(buttons[i])):
			A[buttons[i][j]][i] = 1
	
	bounds = (0, None)

	res = linprog([1] * len(buttons), A_eq=A, b_eq=goals, bounds=bounds, integrality=[1]*len(buttons))
	print(res.fun)
	return res.fun
def part2(filename: str):
	machines = []
	with open(filename) as f:
		for line in f.readlines():
			line = line.strip()
			segments = line.split(" ")
			buttons = []
			for b in segments[1:-1]:
				indexes = [int(x) for x in b[1:-1].split(",")]
				buttons.append(indexes)
			counters = [int(x) for x in segments[-1][1:-1].split(",")]
			machines.append((buttons, counters))

	return sum(solve2(m) for m in machines)
