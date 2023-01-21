# Examples -> abc === cba, aaaaxccccc 
"""
Main ideas are that they should have the same count for every character
- Populate the hashmap and then check the other to ensure it is consistent
- order both strings, make sure they are the same
"""

# Hashmap approach
def isPermutation (str1, str2):
	
	if len(str1) != len(str2):
		return False
	
	uniqueCounts = {}
	for x in str1:
		if x in uniqueCounts:
			uniqueCounts[x]+=1
		else:
			uniqueCounts[x]=1

	for x in str2:
		if x in uniqueCounts:
			uniqueCounts[x]-=1
			if uniqueCounts[x] == 0:
				del uniqueCounts[x]
		else:
			return False
	
	return not len(uniqueCounts.keys())


# Sorting approach
def isPermutationSorting (str1, str2):
		
	if len(str1) != len(str2):
		return False
	
	return sorted(str1)==sorted(str2)
	
print(isPermutationSorting("pde", "del"))
