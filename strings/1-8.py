def setRowColsToZero (arr, i, j, M, N):
	
	# set row to zero
	pointer = 0
	
	while pointer < N:
		arr[i][pointer] = 0
		pointer+=1
	
	# set col to 0
	pointer = 0
	while pointer < M:
		arr[pointer][j] = 0
		#print(arr[pointer][j])
		pointer+=1
	


def zeroMatrix (arr):

	M = len(arr)
	if M <= 0:
		return

	N = len(arr[0])
	columnsCompleted = {}
	rowsCompleted = {}
	
	# a strore will enable us to prevent re-doing operations

	for i in range(M):
		for j in range(N):
			if i in rowsCompleted or j in columnsCompleted:
				continue
			if arr[i][j] == 0:
				setRowColsToZero(arr, i, j, M, N)
				columnsCompleted[j] = None
				rowsCompleted[i] = None
	return arr

vector = zeroMatrix([ [1, 2, 3], [4, 0, 6], [7, 8, 9], [11, 12, 13]  ])
[print(row) for row in vector]	
