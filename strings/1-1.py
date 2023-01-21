"""
This assumes that you are working with an ascii data set
This eans we have 128 unique characters at most
So we can create an array for this and when the arr[index] has already been set because it was previously found
then we can return false.

If there is no character constraint, we can use hashmap approach

"""
def isUnique (msg):

	if len(msg) > 128:
		return False	

	uniques = [True]*128
	for x in msg:
		position = ord(x)-32
		if not uniques[position]:
			print(False)
			return False
		else:
			uniques[position] = False

	print(True)

"""
Bit vector follows a similar idea, except we use the bits as the array and the size is further reduced
from 128 bits to just the 25, but we can store this information in a single number of 32 bits.
"""

def bitChecker (msg):
	checker = 0
	for x in msg:
		index = ord(x) - ord('a')
		bitRepresentation = 1 << index
		if bitRepresentation & checker:
			print(False)
			return False
		checker |= bitRepresentation
	
	print(True)
	return True


bitChecker("uniqs") 
