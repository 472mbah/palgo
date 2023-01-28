from linked import Node 

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

sequence = Node(1)
sequence.addNode(2)
sequence.addNode(2)
sequence.addNode(2)
sequence.addNode(3)
sequence.addNode(2)
sequence.addNode(4)
sequence.printNodes()
print("----------------")
removeDups(sequence) 	
sequence.printNodes()	
