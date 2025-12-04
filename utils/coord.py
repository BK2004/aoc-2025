from dataclasses import dataclass

@dataclass
class Coord:
	x: int
	y: int

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

	def __add__(self, other):
		x, y = None, None
		if isinstance(other, Coord):
			x = other.x
			y = other.y
		elif isinstance(other, tuple):
			(x, y) = other
		
		if x is None or y is None:
			raise TypeError(f"Can't add {other.__class__} to Coord")
		
		return Coord(self.x + x, self.y + y)
	
	def __sub__(self, other):
		x, y = None, None
		if isinstance(other, Coord):
			x = other.x
			y = other.y
		elif isinstance(other, tuple):
			(x, y) = other
		
		if x is None or y is None:
			raise TypeError(f"Can't subtract {other.__class__} from Coord")
		
		return Coord(self.x - x, self.y - y)
	
	def __mul__(self, other):
		x, y = None, None
		if isinstance(other, Coord):
			x = other.x
			y = other.y
		elif isinstance(other, tuple):
			(x, y) = other
		elif isinstance(other, int):
			x = y = other

		if x is None or y is None:
			raise TypeError(f"Can't multiply {other.__class__} and Coord")
		
		return Coord(self.x * x, self.y * y)
	
	def __truediv__(self, other):
		x, y = None, None
		if isinstance(other, Coord):
			x = other.x
			y = other.y
		elif isinstance(other, tuple):
			(x, y) = other
		elif isinstance(other, int):
			x = y = other

		if x is None or y is None:
			raise TypeError(f"Can't divide Coord by {other.__class__}")
		
		return self.__class__(self.x / x, self.y / y)
	
	def __floordiv__(self, other):
		x, y = None, None
		if isinstance(other, Coord):
			x = other.x
			y = other.y
		elif isinstance(other, tuple):
			(x, y) = other
		elif isinstance(other, int):
			x = y = other

		if x is None or y is None:
			raise TypeError(f"Can't divide Coord by {other.__class__}")
		
		return self.__class__(self.x // x, self.y // y)
	
	def __str__(self):
		return f"({self.x}, {self.y})"