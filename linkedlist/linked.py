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
	
	def printNodes (self, showIndex=True, index=0):
		if self.data != None:
			print(f"{str(index+1)+' - ' if showIndex else ''}{self.data}")
			if self.next != None:
				self.next.printNodes(showIndex, index+1)
	
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
		
	def printNodes (self, showIndex=True, index=0):
		self.first.printNodes(showIndex, index)


	def removeOnValue (self, value):
		self.first.removeOnValue(value)

#first = NodeWrapper("hello")
#first.addNode("world")
#first.addNode("how")
#first.addNode("is")
#first.addNode("it")
#first.addNode("hello")
#first.addNode("going")
#first.addNode("this")
#first.addNode("is")
#first.addNode("funny!")
#first.printNodes()
#print("---------------------")
#first.removeOnValue("hello")
#first.removeOnValue("is")
#first.printNodes()
