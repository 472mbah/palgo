def stringCompress (word):
	counts = [0] * 60
	ranges = [ord('A'), ord('z')]
	midRanges = [ord('Z'), ord('a')]
	for x in word:
		chrIndex = ord(x)
		if chrIndex > midRanges[0] and chrIndex < midRanges[1]:
			continue
		 
		if chrIndex < ranges[0] or chrIndex > ranges[1]:
			continue

		index = chrIndex - ranges[0]
		counts[index]+=1 	
	
	newString = ""
	index = -1
	for count in counts:

		index+=1 
		if count == 0:
			continue
		newString+=(chr(index+ranges[0]) + str(count))
	
	print( newString if len(newString) < len(word) else word  )


stringCompress("heloo world this has been compressed! ia Pience of TEXT yeas!") 

