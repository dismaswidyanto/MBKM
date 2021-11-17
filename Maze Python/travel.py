from isDemon import isDemon
def travel(Q_table, demon_table, start, goal, agenPos):
	s = start
	for i in range(25):
		if(isDemon(demon_table,s-1)):
			break
		if (s == goal):
			break
		
		M = max(Q_table[s-1])
		I = Q_table[s-1].index(M)
		
		#right
		if(I == 0):
			if(s%5 != 0):
				s = s+1
				agenPos[0] += 120
			else:
				break
		#up
		elif(I == 1):
			if(s > 5):
				s = s-5
				agenPos[1] -= 120
			else:
				break
		#left
		elif(I == 2):
			if(s%5 != 1):
				s = s-1
				agenPos[0] -= 120
			else:
				break
		#down
		elif(I == 3):
			if(s < 21):
				s = s+5
				agenPos[1] += 120
			else:
				break
	
	if(i == 24):
		print("error")
	
	return agenPos
