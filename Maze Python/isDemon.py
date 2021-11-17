def isDemon(demon_table, state, SIZE):
	if(demon_table[state//SIZE][state%SIZE] == 1):
		return True
	else:
		return False
