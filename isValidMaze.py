#Kairavi Chahal
#kchahal@andrew.cmu.edu

from lab2 import *

def checkStart(maze):
	start = 0
	for row in xrange(len(maze)):
		for col in xrange(len(maze[row])):
			if (maze[row][col] == "S"):
				start += 1
	if (start == 1):
		return True
	return False
	
def checkFinish(maze):
	finish = 0
	for row in xrange(len(maze)):
		for col in xrange(len(maze[row])):
			if (maze[row][col] == "F"):
				finish += 1
	if (finish == 1):
		return True
	return False

def checkCharacters(maze):
	for row in xrange(len(maze)):
		for col in xrange(len(maze[row])):
			if (maze[row][col] != "S"):
				if (maze[row][col] != "F"):
					if(maze[row][col] != "P"):
						if (maze[row][col] != "W"):
							return False
	return True

def checkSolve(maze):
	mazeSolution = []
	if solveMaze(maze, mazeSolution):
		return True
	return False

def findPathToStart(row, col, maze, mazeSolution):
    if (maze[row][col] == "S"):
        mazeSolution.append("(%d, %d)" % (row, col))
        return True
    if (maze[row][col] == "W"):
        return False
    if ("(%d, %d)" % (row, col) in mazeSolution):
        return False
    mazeSolution.append("(%d, %d)" % (row, col))
    #print mazeSolution
    if ((row < len(maze)-1) and (findPathToStart(row+1, col, maze, mazeSolution))) or ((col > 0) and (findPathToStart(row, col-1, maze, mazeSolution))) or ((row > 0) and (findPathToStart(row-1, col, maze, mazeSolution))) or ((col < len(maze[row])-1) and (findPathToStart(row, col+1, maze, mazeSolution))):
        return True
    else:
        mazeSolution.remove("(%d, %d)" % (row, col))
        #print mazeSolution
    return False

def checkPaths(maze):
	for row in xrange(len(maze)):
		for col in xrange(len(maze[row])):
			if (maze[row][col] == "P"):
				mazeSolution = []
				if not findPathToStart(row, col, maze, mazeSolution):
					return False
	return True

def isValidMaze(maze):
	if not checkCharacters(maze):
		print "Maze contains invalid characters."
		return False
	if not checkStart(maze):
		print "Maze contains invalid number of starts."
		return False
	if not checkFinish(maze):
		print "Maze contains invalid number of finishes."
		return False
	if not checkSolve(maze):
		print "Maze is not solvable."
		return False
	if not checkPaths(maze):
		print "Maze contains invalid paths."
		return False
	return True
