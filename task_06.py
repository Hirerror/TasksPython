class Task:
    
    def rps_game_winner(plist):

        varmove = "PSRpsr"
        wintxt = " win!, move = "
        rock  = [False]
        paper = [False]
        shear = [False]
        player1 = []
        player2 = []
        win = ""

        for n in range(0,len(plist)):
            if n > 1:
                raise TypeError("WrongNumberOfPlayersError")
                
        player1 = plist[0][0]
        player2 = plist[1][0]
        pm1 = plist[0][1]
        pm2 = plist[1][1]

        if len(pm1.strip(varmove)) != 0 or len(pm2.strip(varmove))!= 0:
            raise TypeError("NoSuchStrategyError")

        if(pm1 == pm2):
            win = player1 + wintxt + pm1

        else:
            if(len(pm1.strip("Rr")) == 0):
                rock = [True,player1,pm1]
            elif(len(pm1.strip("Pp")) == 0):
                paper = [True,player1,pm1]
            elif(len(pm1.strip("Ss")) == 0):
                shear = [True,player1,pm1]
            if(len(pm2.strip("Rr")) == 0):
                rock = [True,player2,pm2]
            elif(len(pm2.strip("Pp")) == 0):
                paper = [True,player2,pm2]
            elif(len(pm2.strip("Ss")) == 0):
                shear = [True,player2,pm2]
          
            if(rock[0] and shear[0]):
                win = rock[1] + wintxt + rock[2]
            elif(shear[0] and paper[0]):
                win = shear[1] + wintxt + shear[2]
            elif(paper[0] and rock[0]):
                win = paper[1] + wintxt + paper[2]
        return win
game = [['player1', 'P'], ['player2', 'S'],]#['player3', 'S']]
t = Task
print(t.rps_game_winner(game))
#print(t.rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']])) #=> WrongNumberOfPlayersError
#print(t.rps_game_winner([['player1', 'P'], ['player2', 'A']])) #=> NoSuchStrategyError
print(t.rps_game_winner([['player1', 'P'], ['player2', 'S']])) #=> 'player2 S'
print(t.rps_game_winner([['player1', 'P'], ['player2', 'P']])) #=> 'player1 P'