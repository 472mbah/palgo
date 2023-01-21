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
	
		# If character is in range a - z
		if ord_ < ranges[0] and ord_ > ranges[1]:
			continue
		
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

