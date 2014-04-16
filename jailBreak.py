#Kairavi Chahal
#kchahal@andrew.cmu.edu

def canEscape(maze, row, col):
	mazeSolution = []
	return findPath(maze, mazeSolution, row, col)
	
def createJailyard(maze):
	import copy
	jailyard = copy.deepcopy(maze)
	firstrow = jailyard[0]
	lastrow = jailyard[len(maze)-1]
	for row in xrange(len(maze)):
		if (jailyard[row][0] == "P"):
			jailyard[row][0] = "E"
		if (jailyard[row][len(maze[row])-1] == "P"):
			jailyard[row][len(maze[row])-1] = "E"
		for col in xrange(len(maze[row])):
			if (firstrow[col] == "P"):
				firstrow[col] = "E"
			if (lastrow[col] == "P"):
				lastrow[col] = "E"
	return jailyard
	
def findPath(maze, mazeSolution, row, col):
	jailyard = createJailyard(maze)
	if (jailyard[row][col] == "E"):
		mazeSolution.append("Edge: (%d, %d)" % (row, col))
		return True
	if (maze[row][col] == "W"):
		return False
	if ("(%d, %d)" % (row, col) in mazeSolution):
		return False
	mazeSolution.append("(%d, %d)" % (row, col))
	#print mazeSolution
	if (row < len(maze)-1 and row > 0) or (col < len(maze[row])-1 and col > 0):
		return findPath(maze, mazeSolution, row+1, col) or\
		findPath(maze, mazeSolution, row, col-1) or\
		findPath(maze, mazeSolution, row-1, col) or\
		findPath(maze, mazeSolution, row, col+1)
	else:
		mazeSolution.remove("(%d, %d)" % (row, col))
		#print mazeSolution
	return False
