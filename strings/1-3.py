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

def removeWhiteSpace (data):
	(msg, count) = data
	size = len(msg)
	for x in range(size):
		current = msg[x]
		if current==' ':
			bf2 = ' '
			for j in range(x+1, size):
				previousBft = bf2
				bf2 = msg[j]
				print("New bf2", bf2)
				msg[j] = previousBft
			
	return msg	
print(removeWhiteSpace(removeWhiteSpaceManager("hello world")))	


	
	
