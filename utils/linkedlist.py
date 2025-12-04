from typing import Generic, TypeVar

T = TypeVar("T")

class LinkedListNode(Generic[T]):
		def __init__(self, val: T):
			self.val = val
			self.next = None
			self.prev = None

class LinkedList(Generic[T]):
	def __init__(self):
		self.head = LinkedListNode(None)
		self.tail = LinkedListNode(None)
		self.head.next = self.tail
		self.tail.prev = self.head
		self.size = 0
	
	def get_node(self, idx: int):
		curr = self.head.next
		i = 0
		while i < idx and curr:
			curr = curr.next
		return curr

	def insert(self, node: LinkedListNode[T], idx: int):
		curr = self.get_node(idx)
		if curr is None: return None
		p = curr.prev
		p.next = node
		node.prev = p
		node.next = curr
		curr.prev = node
		self.size += 1
		return node
	
	def insert_after(self, node: LinkedListNode[T], after: LinkedListNode[T]):
		n = after.next
		after.next = node
		node.prev = after
		node.next = n
		n.prev = node
		self.size += 1
		return node
	
	def delete_node(self, node: LinkedListNode[T]):
		p = node.prev
		n = node.next

		p.next = n
		n.prev = p
		node.next = None
		node.prev = None
		self.size -= 1
		return node
	
	def delete_at(self, idx: int):
		curr = self.head.next
		i = 0
		while curr.next and curr.next.val is not None and i < idx:
			curr = curr.next
			i += 1
		if curr == self.tail: return None
		return self.delete_node(curr)