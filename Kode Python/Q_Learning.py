from print_Qtable import print_Qtable
from Routing import Routing
from Action import Action
from Search_Location import Search_Location
from update_Qvalue import update_Qvalue
import random

alpha = 0.5
gamma = 0.9
demon = 8

demon_table = [[0 for i in range(5)] for j in range(5)]

start = int(input("Masukkan posisi start: "))
goal = int(input("Masukkan posisi goal: "))

demon_table[(start-1)//5][start%5 - 1] = "S"
demon_table[(goal-1)//5][goal%5 - 1] = "G"

i=0
while (i<demon):
	pos = random.randint(1,25)
	if((demon_table[(pos-1)//5][pos%5 - 1]!=1) and not((pos==start) or (pos==goal))):
		demon_table[(pos-1)//5][pos%5 - 1]=1
		i+=1
	
print("Demon Table: ")
for i in range (5):
	print(demon_table[i])

Q_table = [[0 for i in range(4)] for j in range (25)]

print("Q-Table and route before learning")
print_Qtable(Q_table)
Routing(Q_table, demon_table, start, goal)

for episode in range (400):
	maze = [[0 for i in range(5)] for j in range (5)]
	maze[(start-1)//5][start%5 - 1] = 1
	
	epsilon = 1 - ((episode+1) / 401)
	
	for t in range (1,16):
		state = Search_Location(maze)
		state = state[0]
		#print("state ",state+1)

		if (state == 25):
			break
		
		[act, new_maze] = Action(maze, Q_table, epsilon)
		
		new_state = Search_Location(new_maze)
		new_state = new_state[0]
		
		[Q_table, new_state] = update_Qvalue(state, new_state, Q_table, act, alpha, gamma, t, demon_table, goal)
		
		maze = new_maze

print("Q-Table and route after learning")
print_Qtable(Q_table)
Routing(Q_table, demon_table, start, goal)
