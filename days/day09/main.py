from utils.grid import *
from utils.sorts import *
from utils.jaggedgrid import *
from utils.graph import *
from utils.linkedlist import *
import math

def part1(filename: str):
	points = []
	with open(filename) as f:
		for line in f.readlines():
			line = line.strip()
			[x, y] = line.split(",")
			points.append((int(x), int(y)))

	max_size = 0
	for i in range(len(points)):
		for j in range(1, len(points)):
			sqr = (points[j][0] - points[i][0] + 1) * (points[j][1] - points[i][1] + 1)
			if sqr > max_size:
				max_size = sqr
	return max_size

def vec(e):
	return (e['x2'] - e['x1'], e['y2'] - e['y1'])

def vert_in_poly(x, y, edges):
	# If on boundary, yes
	for edge in edges:
		v = vec(edge)
		if v[0] == 0 and (edge['y1'] <= y <= edge['y2'] or edge['y2'] <= y <= edge['y1']) and x == edge['x1']:
			return True
		if v[1] == 0 and (edge['x1'] <= x <= edge['x2'] or edge['x2'] <= x <= edge['x1']) and y == edge['y1']:
			return True
	# Even-odd
	cnt = 0
	for edge in edges:
		v = vec(edge)
		if v[0] != 0:
			# can't intersect, continue
			continue
		elif (edge['y1'] < y <= edge['y2'] or edge['y2'] < y <= edge['y1']) and x < edge['x1']:
			cnt += 1
	return cnt % 2 == 1

def intersect(e1, e2):
	# If both are vertical or both are horizontal, they are collinear, so return False
	v1, v2 = vec(e1), vec(e2)
	if (v1[0] == 0 and v2[0] == 0) or (v1[1] == 0 and v2[1] == 0):
		return False
	
	# Make e1 vertical and e2 horizontal
	if v1[1] == 0:
		return intersect(e2, e1)
	
	return (min(e2['x1'], e2['x2']) < e1['x1'] < max(e2['x1'], e2['x2']) and min(e1['y1'], e1['y2']) <= e2['y1'] <= max(e1['y1'], e1['y2'])) or (min(e2['x1'], e2['x2']) <= e1['x1'] <= max(e2['x1'], e2['x2']) and min(e1['y1'], e1['y2']) < e2['y1'] < max(e1['y1'], e1['y2']))

def boundary_in_bounds(x1, y1, x2, y2, edges):
	edge = {
		'x1': x1,
		'x2': x2,
		'y1': y1,
		'y2': y2 
	}

	for e in edges:
		if intersect(edge, e):
			return False
	return True

def in_poly(p1, p2, edges, points):
	# x/y1: top left, x/y2: top right, x/y3: bottom left, x/y4: bottom right
	x1, y1 = p1
	x4, y4 = p2
	x2, y2 = x4, y1
	x3, y3 = x1, y4

	x5, y5 = (x1 + x2) / 2, y1
	x6, y6 = x2, (y1 + y3) / 2
	x7, y7 = x5, y4
	x8, y8 = x1, y6

	# Check for red squares in square
	for p in points:
		if x1 < p[0] < x2 and y1 < p[1] < y2:
			return False

	# return vert_in_poly(x1, y1, edges) and vert_in_poly(x2, y2, edges) and vert_in_poly(x3, y3, edges) and vert_in_poly(x4, y4, edges) and vert_in_poly(x5, y5, edges) and vert_in_poly(x6, y6, edges) and vert_in_poly(x7, y7, edges) and vert_in_poly(x8, y8, edges)

	return vert_in_poly(x1, y1, edges) and vert_in_poly(x4, y4, edges) and boundary_in_bounds(x1, y1, x2, y2, edges) and boundary_in_bounds(x2, y2, x3, y3, edges) and boundary_in_bounds(x3, y3, x4, y4, edges) and boundary_in_bounds(x4, y4, x1, y1, edges)

def part2(filename: str):
	points = []
	with open(filename) as f:
		for line in f.readlines():
			line = line.strip()
			[x, y] = line.split(",")
			points.append((int(x), int(y)))

	edges = []
	for i in range(len(points)):
		p1, p2 = points[i], points[(i + 1) % len(points)]
		edges.append({
			'x1': p1[0],
			'y1': p1[1],
			'x2': p2[0],
			'y2': p2[1]
		})

	max_size = 0
	for i in range(len(points)):
		for j in range(1, len(points)):
			sqr = abs(points[j][0] - points[i][0] + 1) * abs(points[j][1] - points[i][1] + 1)
			if sqr > max_size and in_poly(points[i], points[j], edges, points):
				max_size = sqr
		print(f'Finished point {i+1}/{len(points)}')
	return max_size
