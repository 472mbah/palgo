from linked import produceSequenceFromArray

def partition ( sequence, x, pivotParent=None, previousNode=None, startNode=None):
	
	if sequence == None:
		return
	
	if sequence.next == None:
		return
	
	if startNode == None:
		startNode = sequence

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
	
		partition(sequence.next, x, pivotParent, sequence, startNode)
	
	else:
		expectedNext = sequence.next
		if sequence.data < x:
			pivotParent.next = sequence
			pivotParent.next.next = expectedNext	
		
		partition(expectedNext, x, pivotParent, pivotParent.next, startNode)
	
	pass

sequence = produceSequenceFromArray([1, 2, 6, 5, 7, 4, 2, 1]) 
sequence.printNodes()
partition(sequence, 5)
sequence.printNodes()
