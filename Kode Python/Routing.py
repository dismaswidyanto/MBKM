from isDemon import isDemon
def Routing(Q_table, demon_table):
	print("Route")
	s = 1
	for i in range(25):
		if(isDemon(demon_table,s-1)):
			print("error")
			break
		if (s == 25):
			print("S",s," Goal!\n")
			break
		
		print("S",s,end=" ")
		M = max(Q_table[s-1])
		I = Q_table[s-1].index(M)
		
		if(I == 0):
			if(s%5 != 0):
				s = s+1
			else:
				print("error")
				break
		elif(I == 1):
			if(s > 5):
				s = s-5
			else:
				print("error")
				break
		elif(I == 2):
			if(s%5 != 1):
				s = s-1
			else:
				print("error")
				break
		elif(I == 3):
			if(s < 21):
				s = s+5
			else:
				print("error")
				break
	
	if(i == 24):
		print("error")
		
