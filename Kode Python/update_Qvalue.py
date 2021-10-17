from isDemon import isDemon
def update_Qvalue(state, new_state, Q_table, act, alpha, gamma, t, demon_table):
	
	if (new_state == 24):
		reward = 100
	elif (t == 15):
		reward = -50
		
	elif (isDemon(demon_table,new_state)):
		reward = -100
		
	else:
		reward = 0
	
	Q_table[state][act] = (1 - alpha) * Q_table[state][act] + alpha * (reward +  gamma * max(Q_table[new_state]))
	
	return (Q_table, new_state)
