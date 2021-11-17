#call library
from print_Qtable import print_Qtable
from Routing import Routing
from Action import Action
from Search_Location import Search_Location
from update_Qvalue import update_Qvalue
import random

#q-learning function
def Q_Learning(Q_table, alpha, gamma, demon_table, start, goal, SIZE):
	# #parameter
	# alpha = 0.5
	# gamma = 0.9
	# demon = 8

	# #generate demon table
	# demon_table = [[0 for i in range(5)] for j in range(5)]

	# #input start and goal
	# start = int(input("Masukkan posisi start: "))
	# goal = int(input("Masukkan posisi goal: "))

	# #mark start and goal position
	# demon_table[(start-1)//5][start%5 - 1] = "S"
	# demon_table[(goal-1)//5][goal%5 - 1] = "G"

	# #mark demon position
	# i=0
	# while (i<demon):
		# pos = random.randint(1,25)
		# if((demon_table[(pos-1)//5][pos%5 - 1]!=1) and not((pos==start) or (pos==goal))):
			# demon_table[(pos-1)//5][pos%5 - 1]=1
			# i+=1

	# #print demon table
	# print("Demon Table: ")
	# for i in range (5):
		# print(demon_table[i])

	# #generate Q_table
	# Q_table = [[0 for i in range(4)] for j in range (25)]

	# print("Q-Table and route before learning")
	# print_Qtable(Q_table, SIZE)
	# Routing(Q_table, demon_table, start, goal, SIZE)

	#start learning
	for episode in range (400):
		#place agen in maze
		maze = [[0 for i in range(SIZE)] for j in range (SIZE)]
		maze[(start-1)//SIZE][start%SIZE - 1] = 1
		
		#epsilon for probability function
		epsilon = 1 - ((episode+1) / 401)
		
		for t in range (1,16):
			#find state from maze
			state = Search_Location(maze, SIZE)
			state = state[0]
			#print("state ",state+1)

			if (state == SIZE*SIZE):
				break
			
			#choose action
			[act, new_maze] = Action(maze, Q_table, epsilon, SIZE)
			
			#find new_state from new_maze
			new_state = Search_Location(new_maze, SIZE)
			new_state = new_state[0]
			
			#update q-table
			[Q_table, new_state] = update_Qvalue(state, new_state, Q_table, act, alpha, gamma, t, demon_table, goal,SIZE)
			
			maze = new_maze

	# print("Q-Table and route after learning")
	# print_Qtable(Q_table, SIZE)
	# Routing(Q_table, demon_table, start, goal, SIZE)
