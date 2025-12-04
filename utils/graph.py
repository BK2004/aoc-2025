from typing import Generic, Iterable, TypeVar
from .coord import Coord
from .jaggedgrid import JaggedGrid
from .grid import Grid
from dataclasses import dataclass

T = TypeVar("T")

Relations = {
	"ADJACENCY_LIST": 0,
	"EDGE_MATRIX": 1
}

@dataclass
class Node(Generic[T]):
	val: T

	def __eq__(self, other):
		return isinstance(other, Node) and other.val == self.val
	
class Graph(Generic[T]):
	def __init__(self, nodes: Iterable[T] = [], edges: Iterable[tuple] = [], relation_type = Relations["ADJACENCY_LIST"]):
		self._nodes = [Node(x) for x in nodes]
		self._links = {}
		self._num_edges = 0
		self._relation = relation_type

		for i in range(self.num_verts):
			self._links[nodes[i]] = i

		if self._relation == Relations["ADJACENCY_LIST"]:
			self._edge_links = [{} for _ in range(self.num_verts)]
		elif self._relation == Relations["EDGE_MATRIX"]:
			self._edge_links = Grid([[0] * self.num_verts] * self.num_verts)

		for edge in edges:
			self.add_edge(edge[0], edge[1])
	
	@property
	def num_verts(self):
		return len(self._nodes)
	
	@property
	def num_edges(self):
		return self._num_edges
	
	def add_edge(self, vert_1: T, vert_2: T):
		if self._relation == Relations["ADJACENCY_LIST"]:
			self._edge_links[self._links[vert_1]][self._links[vert_2]] = 1
		elif self._relation == Relations["EDGE_MATRIX"]:
			self._edge_links[(self._links[vert_1], self._links[vert_2])] = 1

	def __str__(self):
		lines = []
		for i in range(self.num_verts):
			if self._relation == Relations["ADJACENCY_LIST"]:
				lines.append(" ".join(str(self._nodes[x].val) for x in self._edge_links[i]))
			elif self._relation == Relations["EDGE_MATRIX"]:
				tmp = []
				for j in range(self._edge_links.width):
					if self._edge_links[(i, j)] > 0: tmp.append(self._nodes[j].val)
				lines.append(" ".join(str(x) for x in tmp))
		return "\n".join(f"{self._nodes[i].val}: {lines[i]}" for i in range(self.num_verts))