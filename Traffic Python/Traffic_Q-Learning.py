#call library
import random

#get_state: get state representation from traffic condition
def get_state(kondisi):
	return kondisi[0]*pow(2,3) + kondisi[1]*pow(2,2) + kondisi[2]*pow(2,1) + kondisi[3]*pow(2,0)
	
#update_kondisi: update traffic condition based on action
def update_kondisi(green, kondisi):
	for i in range(4):
		if(i == green):
			kondisi[i] -= 1
			if(kondisi[i] <= 0):
				kondisi[i] = 0
		else:
			kondisi[i] += 1
			if(kondisi[i] >= 1):
				kondisi[i] = 1
				
	return kondisi

#action: choose action based on condition and q-table
def action(state, kondisi, q_table):
	
	number = random.random()
	if(number <= 0.25):
		green = 0 #lane 1
	elif(number <= 0.5):
		green  = 1 #lane 2
	elif(number <= 0.75):
		green = 2 #lane 3
	else:
		green = 3 #lane 4
		
	kondisi = update_kondisi(green, kondisi)
	
	return green, kondisi

#update_qvalue: update q-value in q-table based on action and reward
# def update_qvalue():
	
#parameter
alpha = 0.5
gamma = 0.9


#make q-table
q_table = [[0 for i in range(4)] for j in range(16)]

for episode in range(300):
	kondisi = [0 for i in range(4)]
	
	for t in range(20):
		state =  get_state(kondisi)
		
		[new_kondisi, green_light] = action(kondisi, q-table)
		
		new_state = get_state(new_kondisi)
		
		q-table = update_qvalue(state, kondisi, new_state, new_kondisi, q-table)
		
		kondisi = new_kondisi
	
	
# #test
# kondisi = [0,1,0,1]
# print(kondisi)
# state = get_state(kondisi)
# temp = action(state, kondisi, q_table)
# print(temp[0])
# print(temp[1])
