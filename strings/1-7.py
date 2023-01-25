# Start with outer end of the array, then move inwards, replacing rows with columns
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
		
		while pointer <= bottom:
			temp = buffer[k]
			buffer[k] = arr[pointer][right]
			arr[pointer][right] = temp
			pointer+=1
			k+=1
		
		
		lastItem = buffer[len(buffer)-1]
		# Swap the what was the right row with the bottom
		k = 0
		pointer = right
		while pointer >= left:
			temp = buffer[k]
			buffer[k] = arr[bottom][pointer]
			arr[bottom][pointer] = temp
			pointer-=1
			k+=1 
		buffer[0] = lastItem
		# Swap what was the bottom with the left
			
		lastItem = buffer[len(buffer)-1]
		k = 0
		pointer = bottom
		while pointer >= top:
			temp = buffer[k]
			buffer[k] = arr[pointer][left]
			arr[pointer][left] = temp
			pointer-=1
			k+=1
		buffer[0] = lastItem 
	
		k = 0
		pointer = left
		while pointer < right:
			arr[top][pointer] = buffer[k]
			k+=1
			pointer+=1

		# Place what was the left on the top hand side
		
		buffer = arr[top+1][left+1:right].copy()
		top+=1
		left+=1
		right-=1
		bottom-=1
		
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
