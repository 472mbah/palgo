import random

class Node:
	
	def __init__ (self, data = None, next_ = None):
		self.data = None if data == None else data
		self.next = None if next_ == None else next_
	
	def addNode (self, data, returnNode=False):
		if self.data == None:
			self.data = value
		elif self.next != None:
			self.next.addNode(data, returnNode)
		else:
			self.next = Node(data)
			if returnNode:
				return self.next
	
	def printNodes (self, showIndex=True, index=0, close=True):
		if self.data != None:
			print(f"{str(index+1)+' - ' if showIndex else ''}{self.data}")
			if self.next != None:
				self.next.printNodes(showIndex, index+1, close)
			elif close:
				print("-------------------")
	
	def removeOnValue (self, value):
		if self.data == value:
			if self.next == None:
				self.data = None
			else:
				self.data = self.next.data
				self.next = self.next.next
				self.removeOnValue(value)
				if self.next != None:
					self.next.removeOnValue(value)
		
		elif self.next != None:
			self.next.removeOnValue(value)
			

class NodeWrapper:
	
	def __init__ (self, data=None, next_=None):
		self.first = Node(data)
		self.last = None
	
	def addNode (self, data):
		if self.last == None:
			self.last = self.first.addNode(data, True)
		else:
			self.last = self.last.addNode(data, True)
		
	def printNodes (self, showIndex=True, index=0, close=True):
		self.first.printNodes(showIndex, index, close)


	def removeOnValue (self, value):
		self.first.removeOnValue(value)

def createRandomSet (size=10, min_=0, max_=9):
	parent = Node(random.randint(min_, max_))
	for k in range(size-1):
		parent.addNode( random.randint( min_, max_  ) )	
		
	return parent
