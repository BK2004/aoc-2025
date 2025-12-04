# Creating new day
Create new directory under repo/days with format day{daynum}.  
The daynum must be 1 greater than previous highest.  
e.g. ```day02``` or ```day13```

Create python file in new directory with name main.py.  
Give it 2 functions that take filename as their only args.  
e.g. days/day02/main.py
```
def part1(filename: str):
	with open(filename, 'r') as input:
		for line in input:
			print(line)

def part2(filename: str):
	pass
```

# Adding data files
Create any text file under your day{daynum} folder and pass the name of the file when you run aoc.py  
NOTE: defaults to input.dat

# Usage
py aoc.py &lt;day_num:1-{NUM_DAYS}&gt; [part=0] [datafile=input.dat]  
If no part is provided or part isn't 1 or 2, both parts will be printed for provided day