from typing import Generic, TypeVar

T = TypeVar("T")

def merge_sort(arr: list[T], in_place=True):
	if not in_place:
		arr = [x for x in arr]
	return merge_sort_dfs(arr, 0, len(arr) - 1)
    
def merge_sort_dfs(arr: list[T], l: int, r: int):
	if l >= r: return
	m = (l + r + 1) // 2
	merge_sort_dfs(arr, l, m - 1)
	merge_sort_dfs(arr, m, r)

	# Merge both parts
	l_half = arr[l:m]
	r_half = arr[m:r+1]
	i, j, k = 0, 0, 0
	n, m = len(l_half), len(r_half)
	while i < n or j < m:
		if i >= n:
			arr[l+k] = r_half[j]
			j += 1
		elif j >= m:
			arr[l+k] = l_half[i]
			i += 1
		elif l_half[i] < r_half[j]:
			arr[l+k] = l_half[i]
			i += 1
		else:
			arr[l+k] = r_half[j]
			j += 1
		k += 1

	return arr

def counting_sort(arr, exp1):
	n = len(arr)

	# The output array elements that will have sorted arr
	output = [0] * (n)

	# initialize count array as 0
	count = [0] * (10)

	# Store count of occurrences in count[]
	for i in range(0, n):
		index = arr[i] // exp1
		count[index % 10] += 1

	# Change count[i] so that count[i] now contains actual
	# position of this digit in output array
	for i in range(1, 10):
		count[i] += count[i - 1]

	# Build the output array
	i = n - 1
	while i >= 0:
		index = arr[i] // exp1
		output[count[index % 10] - 1] = arr[i]
		count[index % 10] -= 1
		i -= 1

	# Copying the output array to arr[]
	i = 0
	for i in range(0, len(arr)):
		arr[i] = output[i]

def radix_sort(arr):
	# Find the maximum number to know number of digits
	max1 = max(arr)

	# Do counting sort for every digit. 
	exp = 1
	while max1 / exp >= 1:
		counting_sort(arr, exp)
		exp *= 10