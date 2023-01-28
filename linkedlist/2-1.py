from linked import Node, createRandomSet 

"""
Approach: for each data item, check nodes in front to see if data is repeated
Given we have to compare every node,
this is has complexity of n*n(n-1)
"""
def removeDups (sequence):
	
	pointer = sequence
	while pointer.next != None:
		pointer.next.removeOnValue(pointer.data)
		pointer = pointer.next

"""
Bottom method is the same as above without the removeOnValue function
"""
	
def removeDupsStandard (sequence):
	pointer1 = sequence
	pointer2 = sequence.next
	
	while pointer1 != None and pointer2 != None:
		
		while pointer2 != None:
			if pointer2.data == pointer1.data:	
				if pointer2.next != None:
					pointer2.data = pointer2.next.data
					pointer2.next = pointer2.next.next
				else:
					pointer2.data = None
					return
			else:
				
				pointer2 = pointer2.next
		pointer1 = pointer1.next
		pointer2 = None if pointer1==None else pointer1.next

"""
The following method uses hash table, giving us a run time of O(n) but space complexity of O(n) too
"""

def removeDupsBuffer (sequence):
	
	buffer = {}
	pointer = sequence
	
	while pointer.next != None:
		if pointer.data in buffer:
			if pointer.next == None:
				pointer.data = None
				pointer = pointer.next
			else:
				pointer.data = pointer.next.data
				pointer.next = pointer.next.next
		else:
			buffer[pointer.data] = None
			pointer = pointer.next
	
	if pointer.data in buffer:
		pointer.data = None	

sequence = createRandomSet(800)
removeDupsBuffer(sequence) 	
sequence.printNodes()	
