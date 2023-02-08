from linked import produceSequenceFromArray

# Storing reference of pivot helps in cases where pivot is the parent node of the linked list 
def partition ( sequence, x, pivotParent=None, pivot=None, previousNode=None, startNode=None):
	
	if sequence == None:
		return
	
	if sequence.next == None:
		return
	
	if startNode == None:
		startNode = sequence
	
	print(pivotParent)	

	if pivotParent==None:
	
		if sequence.next.data == x:
		
			if x < sequence.data:
				previousNode.next = sequence.next
				temp = sequence.next.next
				sequence.next.next = sequence
				sequence.next = temp
				pivotParent = previousNode	
			else:
				pivotParent = sequence
	
		partition(startNode, x, pivotParent, sequence, startNode)
		
	else:
		partition(sequence.next, x, pivotParent, sequence, None)	

	"""	
	else:
		expectedNext = sequence.next
		if sequence.data < x:
			pivotParent.next = sequence
			pivotParent.next.next = expectedNext	
		
		partition(expectedNext, x, pivotParent, pivotParent.next, startNode)
	
	pass
	"""

sequence = produceSequenceFromArray([1, 2, 6, 5, 7, 4, 2, 1]) 
sequence.printNodes()
partition(sequence, 5)
sequence.printNodes()
