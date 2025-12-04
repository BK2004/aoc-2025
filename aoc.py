import sys
import os
import importlib
import time

MAX_DAYS = len(next(os.walk('./days'))[1])
FLAGS = {
	"test": ["-t", "--test"]
}

def invalid_usage():
	print(f"\033[91mUsage: {sys.argv[0]} <day_num:1-{MAX_DAYS}> [part=0] [datafile=input.dat]")
	print("If no part is provided or part isn't in [1, 2], both parts will be printed.\033[0m")
	sys.exit(1)

def req_int(arg_name: str):
	print(f"\033[91m{arg_name} must be an integer\033[0m")
	sys.exit(1)

def bubble_flags(argv):
	# Move flags to back of array
	l = 0
	for i in range(len(argv)):
		if str(argv[i])[0] != '-':
			argv[l], argv[i] = argv[i], argv[l]
			l += 1
	
	return l

def parse_flags(argv, num_flags):
	seen_flags = set()
	for i in range(num_flags):
		seen_flags.add(argv[-i-1])
	
	parsed = {}
	for key in FLAGS:
		parsed[key] = False
		for id in FLAGS[key]:
			if id in seen_flags:
				parsed[key] = True
	return parsed

def print_runtime(label, start_time, flags):
	if not flags['test']: return
	end_time = time.time()

	print(f"{label} took {int(end_time - start_time) // 60}m, {int(end_time - start_time) % 60}s, and {int((end_time - start_time) % 1 * 1000)}ms")

# Returns (day, part, datafile)
def parse_cli():
	# Sort 
	num_args = bubble_flags(sys.argv)
	num_flags = len(sys.argv) - num_args
	if num_args < 2 or num_args > 4:
		invalid_usage()
	
	# Check for day number as 2nd arg and in bounds
	if not sys.argv[1].isnumeric():
		req_int("Day")
	day = int(sys.argv[1])
	if day < 1 or day > MAX_DAYS:
		print(f"\033[91mDay must be between 1 and {MAX_DAYS}\033[0m")
		sys.exit(1)

	flags = parse_flags(sys.argv, num_flags)

	# Get part and datafile if given
	part = 0
	datafile = "input.dat"
	if num_args > 2:
		if sys.argv[2].isnumeric(): 
			part = int(sys.argv[2])
			if num_args == 4: datafile = sys.argv[3]
		else:
			datafile = sys.argv[2]
			if num_args == 4:
				if sys.argv[3].isnumeric(): part = int(sys.argv[3]) 
				else: req_int("Part")
	if part > 2: part = 0

	return day, part, datafile, flags

def exec():
	day, part, datafile, flags = parse_cli()
	day = str.format("day{:02d}", day)
	datafile = f"days/{day}/{datafile}"

	module = importlib.import_module(f"days.{day}.main")
	start_time = time.time()
	if part <= 1:
		start_time_p1 = time.time()
		print(f"Part 1: {module.part1(datafile)}")
		print_runtime("Part 1", start_time_p1, flags)
	if part % 2 == 0:
		start_time_p2 = time.time()
		print(f"Part 2: {module.part2(datafile)}")
		print_runtime("Part 2", start_time_p2, flags)
	print_runtime("Total", start_time, flags)

exec()