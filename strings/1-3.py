"""
This is the url problem
"""

def removeWhiteSpaceManager(msg):
	extra = ""
	for x in msg:
		if x == ' ':
			extra += "  "
	txt = list(msg+extra)
	return (txt, len(txt))

def shiftValuesByN (valuesArr, n, startFrom=0):
	placeholders = [" "] * n
	currIndex = 0
	
	tracker = startFrom
	size = len(valuesArr)
	placeholderSize = len(placeholders)	

	while tracker < size:
		temp = placeholders[currIndex]
		placeholders[currIndex] = valuesArr[tracker]
		valuesArr[tracker] = temp
		
		currIndex = (currIndex+1) % placeholderSize
		tracker+=1
	return valuesArr	

def removeWhiteSpace (data):
	(msg, count) = data
	size = len(msg)
	for x in range(size):
		current = msg[x]
		if current==' ':
			startFrom = x+1
			shiftValuesByN(msg, 2, startFrom)
			msg[x] = '%'
			msg[x+1] = '2'
			msg[x+2] = '0'
	
	return ''.join(msg)	

arrayText = removeWhiteSpaceManager("urlify function doing something interesting converting text")
print(removeWhiteSpace(arrayText))	
