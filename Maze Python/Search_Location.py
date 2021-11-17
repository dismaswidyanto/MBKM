def Search_Location(maze, SIZE):
	global state, state_i, state_j
	for i in range(SIZE):
		for j in range(SIZE):
			if(maze[i][j] == 1):
				state_i = i
				state_j = j
				state = SIZE * (i) + (j)
	
	return (state, state_i, state_j)
