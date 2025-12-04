from utils.grid import *
from utils.sorts import *
from utils.jaggedgrid import *
from utils.graph import *
from utils.linkedlist import *

def max_joltage(bank: str):
	# Store leftwise-max in arrany and rightwise-max (non-inclusive) in arrays
	l = [0 for _ in range(len(bank))]
	r = [0 for _ in range(len(bank))]
	if len(bank) <= 1:
		return 0
	
	l[0] = int(bank[0])
	r[-1] = int(bank[-1])
	for i in range(1, len(bank)):
		l[i] = max(l[i-1], ord(bank[i]) - ord('0'))
	for i in range(len(bank) - 2, 0, -1):
		r[i] = max(r[i+1], ord(bank[i]) - ord('0'))
	
	# Compute maximum joltage
	res = 0
	for i in range(len(bank)-1):
		res = max(res, l[i] * 10 + r[i+1])
	return res

def max_joltage_2(bank: str, remaining_digits=12):
	if remaining_digits == 0:
		return 0
	
	# Repeat for remaining_digits = (12, 11, ..., 1): pick the largest digit in positions [0,...,len(bank) - remaining_digits - 1] and recurse on [len(bank) - remaining_digits:]
	max_idx = 0
	for i in range(1, len(bank) - remaining_digits + 1):
		if ord(bank[i]) - ord('0') > ord(bank[max_idx]) - ord('0'):
			max_idx = i
	return (ord(bank[max_idx]) - ord('0')) * (10**(remaining_digits - 1)) + max_joltage_2(bank[max_idx+1:], remaining_digits=remaining_digits-1)

def part1(filename: str):
	out = 0
	with open(filename) as f:
		for bank in f.readlines():
			bank = bank.strip()
			out += max_joltage_2(bank, remaining_digits=2)
	return out
			

def part2(filename: str):
	out = 0
	with open(filename) as f:
		for bank in f.readlines():
			bank = bank.strip()
			out += max_joltage_2(bank)
	return out
