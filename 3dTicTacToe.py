#Kairavi Chahal
#kchahal@andrew.cmu.edu

def hasWinner(board):
	n = len(board)
	if checkLayersXY(board, n) or checkLayersYZ(board, n) or checkLayersZX(board, n) or check3dDiag1(board, n) or check3dDiag2(board, n) or check3dDiag3(board, n) or check3dDiag4(board, n):
		return True
	return False
	
def check3dDiag1(board, n):
	won = True
	for x in xrange(n):
		y = x
		z = x
		if (board[x][y][z] == "-"):
			return False
		elif (board[0][0][0] != board[x][y][z]):
			won = False
	return won
	
def check3dDiag2(board, n):
	won = True
	for x in xrange(n):
		y = x
		z = (n-1)-x
		if (board[x][y][z] == "-"):
			return False
		elif (board[0][0][2] != board[x][y][z]):
			won = False
	return won
	
def check3dDiag3(board, n):
	won = True
	for y in xrange(n):
		z = y
		x = (n-1)-y
		if (board[x][y][z] == "-"):
			return False
		elif (board[0][2][2] != board[x][y][z]):
			won = False
	return won
	
def check3dDiag4(board, n):
	won = True
	for x in xrange(n):
		y = (n-1)-x
		z = x
		if (board[x][y][z] == "-"):
			return False
		elif (board[0][2][0] != board[x][y][z]):
			won = False
	return won
	
def checkLayersXY(board, n):
	for layer in xrange(n):
		if checkPlane(board[layer], n):
			return True
	return False
	
def checkLayersYZ(board, n):
	for col in xrange(n):
		layerYZ = []
		for layer in xrange(n):
			layerYZ.append(board[layer][col])
		if checkPlane(layerYZ, n):
			return True
	return False
	
def checkLayersZX(board, n):
	for row in xrange(n):
		layerZX = []
		for layer in xrange(n):
			layerZX.append(board[layer][row])
		if checkPlane(layerZX, n):
			return True
	return False
	
def checkPlane(plane, n):
	for row in xrange(n):
		if checkRow(plane[row], n):
			return True
	for col in xrange(n):
		newCol = []
		for row in xrange(n):
			newCol.append(plane[row][col])
		if checkCol(newCol, n):
			return True
	if checkDiag1(plane, n):
		return True
	elif checkDiag2(plane, n):
		return True
	return False
	
def checkRow(row, n):
	won = True
	for col in xrange(n):
		if (row[col] == "-"):
			won = False
		elif (row[0] != row[col]):
			won = False
	return won
	
def checkCol(col, n):
	won = True
	for row in xrange(n):
		if (col[row] == "-"):
			won = False
		elif (col[0] != col[row]):
			won = False
	return won
	
def checkDiag1(plane, n):
	won = True
	for row in xrange(n):
		col = row
		if (plane[row][col] == "-"):
			return False
		elif (plane[0][0] != plane[row][col]):
			won = False
	return won
	
def checkDiag2(plane, n):
	won = True
	for row in xrange(n):
		col = (n-1)-row
		if (plane[row][col] == "-"):
			return False
		elif (plane[n-1][n-1] != plane[row][col]):
			won = False
	return won
