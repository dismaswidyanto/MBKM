#call library
import random

#print_qtable: print q_table
def print_qtable(Q_table):
	print("State \t North \t East \t South \t West")
	for i in range(16):
		print(i+1, end="\t")
		for j in range (4):
			if(j!=4-1):
				print(format(Q_table[i][j],'.5f'), end="\t");
			else:
				print(format(Q_table[i][j],'.5f'))

#get_state: get state representation from traffic condition
def get_state(kondisi):
	return kondisi[0]*pow(2,3) + kondisi[1]*pow(2,2) + kondisi[2]*pow(2,1) + kondisi[3]*pow(2,0)
	
#update_kondisi: update traffic condition based on action
def update_kondisi(green, kondisi, red_count):
	new_kondisi = kondisi[:]
	new_red_count = red_count[:]

	for i in range(4):
		if(i == green):
			new_kondisi[i] -= 1
			new_red_count [i] = 0
			if(new_kondisi[i] <= 0):
				new_kondisi[i] = 0
		else:
			new_kondisi[i] += 1
			new_red_count [i] += 1
			if(new_kondisi[i] >= 1):
				new_kondisi[i] = 1
	

	return new_kondisi, new_red_count

#action: choose action based on condition and q-table
def action(epsilon, state, kondisi, red_count, q_table):
	
	randomnum = random.random();
	if(epsilon <= randomnum):
		max_value = max(q_table[state])
		for j in range(4):
			if(max_value == q_table[state][j]):
				green = j
	else:
		number = random.random()
		if(number <= 0.25):
			green = 0 #lane north
		elif(number <= 0.5):
			green  = 1 #lane east
		elif(number <= 0.75):
			green = 2 #lane south
		else:
			green = 3 #lane west
	
	[new_kondisi, new_red_count] = update_kondisi(green, kondisi, red_count)
	
	return new_kondisi, green

#update_qvalue: update q-value in q-table based on action and reward
def update_qvalue(green, state, kondisi, new_state, new_kondisi, red_count, q_table, alpha, gamma):
	#derajat 1 diberi hijau
	if(kondisi[green] == 1 and red_count[green] == 3):
		reward = 100
	
	elif(kondisi[green] == 1 and red_count[green] < 3):
		reward = 50
		
	#derajat 0 diberi hijau
	elif(kondisi[green] == 0):
		reward = -50
		
	else:
		reward = 0
	
	#print(reward)
	q_table[state][green] = (1 - alpha) * q_table[state][green] + alpha * (reward +  gamma * max(q_table[new_state]))
	
	return q_table

#parameter
alpha = 0.5
gamma = 0.9


#make q-table
q_table = [[random.random() for i in range(4)] for j in range(16)]
print_qtable(q_table)


for episode in range(300):
	kondisi = [random.randrange(0,2,1) for i in range(4)]
	red_count = [0 for i in range(4)]
	#print(kondisi)
	
	epsilon = 1 - ((episode+1) / 301)
	
	for t in range(200):
		#print(kondisi)
		state =  get_state(kondisi)
		#print(state)
		
		[new_kondisi, green_light] = action(epsilon, state, kondisi, red_count, q_table)
		#print(kondisi)
		#print(new_kondisi)
		#print(green_light)
		
		new_state = get_state(new_kondisi)
		#print(new_state)
		
		q_table = update_qvalue(green_light, state, kondisi, new_state, new_kondisi, red_count, q_table, alpha, gamma)
		
		kondisi = new_kondisi
		#print(kondisi, "\n")
		#break
		#print_qtable(q_table)
		#break
	#break
print_qtable(q_table)
print(q_table)

# #test
# kondisi = [0,1,0,1]
# print(kondisi)
# state = get_state(kondisi)
# temp = action(state, kondisi, q_table)
# print(temp[0])
# print(temp[1])
