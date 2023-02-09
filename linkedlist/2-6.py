import math
from linked import produceSequenceFromArray
def isPalindrome (sequence):
	p1 = sequence
	p2 = sequence
	temp = sequence
	size = 0
	
	# Identify the size
	while temp.next != None:
		size+=1
		temp = temp.next

	midpoint = math.floor(size/2) 
	while midpoint >= 0:
		p2 = p2.next
		midpoint-=1

	while p1 != None and p2!=None:
		if p1.data != p2.data:
			return False
		p1 = p1.next
		p2 = p2.next
	
	return True
	
sequence = produceSequenceFromArray(list("aaabaaa"))
print(isPalindrome(sequence)) 
