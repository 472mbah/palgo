from linked import createRandomSet

def partition (sequence, x, parentOfX=None, itemX=None, biggerThanX=None):
	"""
	Are we in mode 1
	We can still look for items greater than x but positioned before x
	parentsOfX and itemX get defined together
	"""
	if sequence.next == None:
		return
	
	if parentOfX == None: 
		
		if biggerThanX == None:
			sequence.data > x:
				biggerThanX = sequence
		
		if sequence.next.data == x:
			parentOfX = sequence
			itemX = parentOfX.next
			if biggerThanX != None: # this would could be an edge case where biggerThanX == sequence(current)
				
							

	

	# mode 2 - we just keep iterating and appending to the parent of x 
	# the values which are smaller than x
	