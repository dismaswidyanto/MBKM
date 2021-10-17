def print_Qtable(Q_table):
	print("State \t Right \t Up \t Left \t Down")
	for i in range(25):
		print(i+1, end="\t")
		for j in range (4):
			if(j!=4-1):
				print(format(Q_table[i][j],'.5f'), end="\t");
			else:
				print(format(Q_table[i][j],'.5f'))
