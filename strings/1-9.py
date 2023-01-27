def rotate (str_, n):
	chrs = list(str_);
	size = len(chrs)
	tst = [None]*size
	
	for k in range(size):
		newPos = (k+n) % size
		tst[newPos] = chrs[k]
	
	return ''.join(tst)

"""
This is a method without the isSubstring method
s1 shift n == s2 shift -n
"""
def isRotation (str1, str2):
	
	size1 = len(str1)
	size2 = len(str2)
	if size1 != size2:
		return False
	if str1 == str2:
		return False

	n = 1
	while n < size1:
		if rotate(str1, n) == rotate(str2, -n):
			print("N was", n)
			return True		
		n+=1
	return False

"""
Main approach
- There is some point where we can split s1 and s2 into x and y
s1 = xy
s2 = yx
s3 = xyxy
s2 is a substring of s3
therefore a rotation of s1
"""

def isRotation2 (str1, str2):
	s3 = str1*2
	return str2 in s3

print(isRotation2("waterbottle", rotate("waterbottle", 1000)))
