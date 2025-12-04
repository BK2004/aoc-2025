# Creating container directory
day=$(printf "%02d" $1)
dir="days/day${day}"
mkdir $dir

# Populate with files
echo -n "" >> $dir/sample.dat
echo -n "" >> $dir/input.dat

echo -e "from utils.grid import *
from utils.sorts import *
from utils.jaggedgrid import *
from utils.graph import *
from utils.linkedlist import *

def part1(filename: str):
\tpass

def part2(filename: str):
\tpass" >> $dir/main.py
code $dir/main.py
code $dir/sample.dat
code $dir/input.dat