from typing import TypeVar, Generic, Iterable
from .coord import Coord

T = TypeVar("T")

class JaggedList(Generic[T]):
	def __init__(self, elements: Iterable[T]):
		self._data = [x for x in elements]
		self._width = len(self._data)

	@property
	def width(self):
		return self._width
	
	@property
	def data(self):
		return self._data
	
	def in_bounds(self, idx):
		if isinstance(idx, int):
			return 0 <= idx <= self.width
		elif isinstance(idx, slice):
			return True
		else:
			raise TypeError(f"Not implemented for type {idx.__class__}")
		
	def __contains__(self, idx):
		return self.in_bounds(idx)
	
	def __iter__(self):
		for i in range(self.width):
			yield (self.data[i], i)

	def __getitem__(self, idx):
		return self.data[idx]
	
	def __setitem__(self, idx, new_val):
		if self.in_bounds(idx):
			self.data[idx] = new_val
		else:
			raise IndexError(f"{idx} out of bounds or undefined for JaggedList")
		
	def __str__(self):
		return " ".join(str(x) for (x, _) in self)

class JaggedGrid(Generic[T]):
	def __init__(self, lines: list[Iterable[T]]):
		self._data = [JaggedList(line) for line in lines]
		self._height = len(self._data)
	
	@property
	def height(self):
		return self._height

	@property
	def data(self):
		return self._data
	
	def in_bounds(self, idx):
		if isinstance(idx, int):
			return 0 <= idx < self.height
		elif isinstance(idx, Coord):
			return 0 <= idx.x < self.height and 0 <= idx.y < self[idx.x].width
		elif isinstance(idx, slice):
			return True
		elif isinstance(idx, tuple):
			if isinstance(idx[0], int):
				return 0 <= idx < self.height and self.data[idx[0]].in_bounds(idx[1])
			elif isinstance(idx[0], slice):
				return True
			else:
				return TypeError(f"Not implemented for type {idx.__class__}")
		else:
			return TypeError(f"Not implemented for type {idx.__class__}")
	
	def __contains__(self, idx):
		return self.in_bounds(idx)
	
	def __iter__(self):
		for i in range(self.height):
			for (item, j) in self.data[i]:
				yield (item, i, j)
	
	def __getitem__(self, idx):
		if isinstance(idx, int):
			return self.data[idx]
		elif isinstance(idx, tuple):
			if isinstance(idx[0], slice):
				return [x[idx[1]] for x in self.data[idx[0]]]
			return self.data[idx[0]][idx[1]]
		elif isinstance(idx, Coord):
			return self.data[idx.x][idx.y]
		elif isinstance(idx, slice):
			return self.data[idx]
		else:
			return TypeError(f"Not implemented for type {idx.__class__}")
		
	def __setitem__(self, idx, val):
		if isinstance(idx, tuple):
			if self.in_bounds(idx):
				self.data[idx[0]][idx[1]] = val
			else:
				raise IndexError(f"{idx} out of bounds")
		elif isinstance(idx, Coord):
			if self.in_bounds(idx):
				self.data[idx.x][idx.y] = val
			else:
				raise IndexError(f"{idx} out of bounds")
		else:
			raise NotImplementedError
		
	def __str__(self):
		return "\n".join(str(x) for x in self.data)