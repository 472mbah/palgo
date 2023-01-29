from linked import createRandomSet

def findKthToLast (sequence, k):
	if k <= 0:
		k = 1
	pointer = sequence
	size = 0
		
	# Step 1: Identidy size of the linked list	

	while pointer.next != None:
		if pointer.data != None:
			size+=1
			pointer = pointer.next

	# Step 2: Iterate to the kth to last element in the list
	targetIndex = size - k
	pointer = sequence
	if targetIndex < 0:
		return None
	while targetIndex >= 0:
		pointer = pointer.next
		targetIndex-=1
	
	return pointer.data


sequence = createRandomSet()
sequence.printNodes()
print(findKthToLast(sequence, 4))
