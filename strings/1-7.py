# Start with outer end of the array, then move inwards 



def swapOutValues ( s1, s2, e1, e2 ):
	pass	

# Assuming that arr is a nxn matrix
def rotateArray (arr):
	left = top = 0
	n = len(arr)
	right = bottom = n - 1
	
	buffer = arr[0].copy()

	while left < right and top < bottom:
		# Swap the top row with the right row

		# have a buffer that you shift and pop at every iteration
		k = 0
		pointer = top
		while pointer < bottom:
			temp = buffer[k]
			buffer[k] = arr[pointer][right]
			arr[pointer][right] = temp
			pointer+=1
			k+=1

		left = 100
		top = 100
		print(buffer)

		# Swap the what was the right row with the bottom
		# Swap what was the bottom with the left
		# Place what was the left on the right hand side

	print(arr)

arr = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]  ]
rotateArray(arr)
	
"""

01  02   03   04
05  06   07   08
09  10   11   12
13  14   15   16

Becomes

ee ee ee 01
	     02
         03
         04

buffer -> [04, 08, 12, 16]


13  09  05  01
14  10  06  02
15  11  07  03
16  12  08  04

"""	
	

	
