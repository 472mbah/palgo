from linked import createRandomSet

def partition (sequence, x, beforeX=None, afterX=None):
	ignoreNode = False
	if afterX == None:
		if sequence.data == x:
			afterX = sequence.next
			ignoreNode = True
	
	beforeX = sequence if beforeX == None else beforeX
	partition(sequence, x, beforeX, afterX)
	
	if ignoreNode:
		return
	

		
		
	
