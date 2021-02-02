import numpy as np
from collections import deque 

#computes all possible paths through backtracking
def backtrack(grid, end, max_dist, path=[]):
	result = []
	if max_dist == 0:
		return [path[::-1]]
	max_x, max_y = grid.shape
	x,y = end
	if x - 1 >= 0 and grid[x - 1][y] == max_dist:
		new_path = path.copy()
		new_path.append([x - 1,y])
		result = result + backtrack(grid, [x - 1,y], max_dist-1, new_path)
	if x + 1 < max_x and grid[x + 1][y] == max_dist:
		new_path = path.copy()
		new_path.append([x + 1,y])
		result = result + backtrack(grid, [x + 1,y], max_dist-1, new_path)
	if y - 1 >= 0 and grid[x][y - 1] == max_dist:
		new_path = path.copy()
		new_path.append([x,y - 1])
		result = result + backtrack(grid, [x,y - 1], max_dist-1, new_path)
	if y + 1 < max_y and grid[x][y + 1] == max_dist:
		new_path = path.copy()
		new_path.append([x,y + 1])
		result = result + backtrack(grid, [x,y + 1], max_dist-1, new_path)
	return result

def Lee_moore(grid, start, end, other_ends=[]):
	#mark the current wire's sink(s) as 0 to make them accessible
	grid[end[0], end[1]] = 0
	for pin in other_ends:
		grid[pin[0], pin[1]] = 0
	max_dist = -1
	max_x, max_y = grid.shape
	#FIFO for Breadth First Search
	dq = deque([[start, 0]])
	while(dq):
		[x,y],dist = dq.popleft()
		if [x,y] == end:
			max_dist = dist-1
			break
		if x - 1 >= 0 and grid[x - 1][y] == 0:
			grid[x - 1][y] = dist+1
			dq.append([[x - 1, y], dist+1])
		if x + 1 < max_x and grid[x + 1][y] == 0:
			grid[x + 1][y] = dist+1
			dq.append([[x + 1, y], dist+1])
		if y - 1 >= 0 and grid[x][y - 1] == 0:
			grid[x][y - 1] = dist+1
			dq.append([[x, y-1], dist+1])
		if y + 1 < max_y and grid[x][y + 1] == 0:
			grid[x][y+1] = dist+1
			dq.append([[x, y+1], dist+1])
	#if no path can been found
	if max_dist == -1:
		return False
	#compute all possible paths
	result = backtrack(grid, end, max_dist)
	return result