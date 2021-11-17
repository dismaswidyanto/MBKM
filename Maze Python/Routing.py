from isDemon import isDemon
def Routing(Q_table, demon_table, start, goal, SIZE):
	print("Route")
	s = start
	for i in range(SIZE*SIZE):
		if(isDemon(demon_table,s-1,SIZE)):
			print("error")
			break
		if (s == goal):
			print("S",s," Goal!\n")
			break
		
		print("S",s,end=" ")
		M = max(Q_table[s-1])
		I = Q_table[s-1].index(M)
		
		if(I == 0):
			if(s%SIZE != 0):
				s = s+1
			else:
				print("error")
				break
		elif(I == 1):
			if(s > SIZE):
				s = s-SIZE
			else:
				print("error")
				break
		elif(I == 2):
			if(s%SIZE != 1):
				s = s-1
			else:
				print("error")
				break
		elif(I == 3):
			if(s < (SIZE*SIZE)-SIZE):
				s = s+SIZE
			else:
				print("error")
				break
	
	if(i == SIZE-1):
		print("error")
		
