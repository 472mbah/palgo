"""
Align both items together
Start from the back because this makes knowing whether there was an insertion or
deletetion much easier
If there is, you know to shift the pointer of the longer string by one backwards
Other case can only be replacements
If there are changes/differences > 1, then return false
"""


def oneAway (str1, str2):
	str1size = len(str1)
	str2size = len(str2)

	if abs(str1size - str2size) > 1:
		return False

	pointer1 = str1size-1
	pointer2 = str2size-1
	differences = 0
	dropIn = None
	if pointer1 > pointer2:
		differences = 1
		dropIn = 2
	elif pointer2 > pointer1:
		differences = 1
		dropIn = 1
	

	#print('start', pointer1, pointer2, dropIn)
	
	
	while pointer1 >= 0 or pointer2 >= 0:
		ch1 = str1[pointer1]
		ch2 = str2[pointer2]
		consideringDrop = False

		#print("Came in here", ch1, ch2, pointer1, pointer2)
		if ch1 != ch2:
			if dropIn!=None:
		
				consideringDrop = True
				if dropIn == 1:
					pointer2 -= 1
				else:
					pointer1 -= 1
				dropIn = None
			else:
				differences+=1
			if differences >= 2:
				return False
		if not consideringDrop:
			pointer1-=1
			pointer2-=1
	
	return True

print(oneAway("bake", "pale"))	

