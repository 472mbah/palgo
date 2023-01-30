import math
from linked import createRandomSet

def removeMiddleNode (sequence, global_={'size':0, 'backtrackIndex':None, 'deleteDone':False}):
	if sequence.next != None:
		global_['size'] += 1
		removeChild = removeMiddleNode(sequence.next, global_)
		if global_['deleteDone']:
			return None
		if removeChild:
			sequence.next = sequence.next.next
			global_['deleteDone'] = True
			return None
		else:		
			global_['backtrackIndex']-=1
			computed = global_['backtrackIndex']== math.floor(global_['size'] / 2)
			return computed
	else:
		global_['backtrackIndex'] = global_['size']
		return math.floor(global_['backtrackIndex']) == global_['size'] / 2

sequence = createRandomSet(11)
sequence.printNodes()
removeMiddleNode(sequence)
sequence.printNodes()
