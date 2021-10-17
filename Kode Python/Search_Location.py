def Search_Location(maze):
	global state, state_i, state_j
	for i in range(5):
		for j in range(5):
			if(maze[i][j] == 1):
				state_i = i
				state_j = j
				state = 5 * (i) + (j)
	
	return (state, state_i, state_j)
