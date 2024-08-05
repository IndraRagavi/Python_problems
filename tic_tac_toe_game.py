def tic_tac(matr):
    #rows
    for i in range(0,3):
        r = set((matr[i][0], matr[i][1],matr[i][2]))
        if len(r) == 1 and r != 0:
            return matr[i][0]
        
    for i in range(0,3):
        cl = set((matr[0][i] , matr[1][i],matr[2][i]))
        if len(cl) ==1 and cl != 0:
            return matr[0][i]
    
    #diagnol
    
    for i in range(0,3):
        d = set((matr[0][0],matr[1][1],matr[2][2]))
        d1 = set((matr[0][2],matr[1][1],matr[2][0]))
        
        if len(d) == 1 or len(d1) == 1 and matr[1][1] !=0:
            return matr[0][0]
    
    return 0


winner_is_2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_1 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

also_no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]

j = tic_tac(winner_is_1)
print("winner is {}".format(j))