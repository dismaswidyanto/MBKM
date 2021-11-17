#call library
import random
from Search_Location import Search_Location

# action
def Action(maze, Q_table, epsilon, SIZE):
	#variable
	global act
	out = 0;
	
	while (out == 0):
		(state,state_i,state_j) = Search_Location(maze, SIZE)
		#print(state,state_i,state_j)
		
		randomnum = random.random();
		#print(randomnum)
		if (epsilon <= randomnum):
			max_value = max(Q_table[state])
			for j in range(4):
				if(max_value == Q_table[state][j]):
					act = j
		else:
			random_value = random.random()
			#print(random_value)
			if (random_value <= 0.25):
				act = 0
			elif (random_value <= 0.5):
				act = 1
			elif (random_value <= 0.75):
				act = 2
			else:
				act = 3
		
		if (act == 0):
			state_j = state_j + 1
		elif (act == 1):
			state_i = state_i - 1
		elif (act == 2):
			state_j = state_j - 1
		else:
			state_i = state_i + 1
		
		if (state_i == -1):
			out = 0
		elif (state_j == -1):
			out = 0
		elif (state_i == SIZE):
			out = 0
		elif (state_j == SIZE):
			out = 0
		else:
			out = out + 1
	
	new_maze = [[0 for i in range(SIZE)] for j in range(SIZE)]
	new_maze[state_i][state_j] = 1
	
	return (act, new_maze)
