def isDemon(demon_table, state):
	if(demon_table[state//5][state%5] == 1):
		return True
