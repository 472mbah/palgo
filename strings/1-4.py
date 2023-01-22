"""
Permutation of strings problem
Approach: Take count of all values & ensure that
- at most one character with odd count
- all others must be even

Casing can be ignored
Non-letter characters can be ignored too 
"""

def isPermPalindrome (word):

	characters = {}
	word =  word.lower()
	ranges = [ ord('a'), ord('z') ]
	for x in word:
		ord_ = ord(x)
	
		if ord_ < ranges[0] and ord_ > ranges[1]:
			continue
		
		# If character is in range a - z
		if x in characters:
			characters[x] += 1
		else:
			characters[x] = 1
	
	oddCount = 0

	for key in characters:
		# if character is odd
		if characters[key] % 2 != 0:
			oddCount+=1
	
	return oddCount <= 1		

"""
Second approach stems from the fact that we can have at most one character with an odd count.
We can map alphabet (lowercase) from 0 - 25.
Since we are not concerned about words with even count, their bits after toggling
will return to 0.
The others will return to 1.
Works like a light switch

Then we can use bit manipulation to check if only one bit is set.
When (n-1) & n == 0, this means only one bit is set, which therefore means 
at most one character with an odd count
"""

def toggleBit ( index,  bitVector ):
	mask = 1 << index
	return bitVector ^ mask

def isPermPalindromeBitMethod (phrase):
	
	min_ = ord('a')
	ranges = [min_, ord('z')]
	bitVector = 0
	for char in phrase:
		charCode = ord(char)
		if charCode < ranges[0] or charCode > ranges[1]:
			continue
		
		index = charCode - min_	
		bitVector = toggleBit(index, bitVector)		
	
	return bitVector & (bitVector - 1) == 0


print(isPermPalindrome("reviver"))

