"""X O  game"""
import random as r
mat=[["_","_","_"],
     ["_","_","_"],
     ["_","_","_"]]
def display():
    """this func to show the game """
    for i in mat:
        for j in i:
            print(j,end="  ")
        print("\n")


def check():
    """this function to check if the player win or lose."""
    #these are two global variables for end the game.
    global stop_1 ,stop_2
    stop_1=0
    stop_2=0
    constant=-1
    axe1=[]
    axe2=[]
    # this loop to check on (row ,colum,axe1,axe2)
    for i in range(0,3):
        row=[]
        colum=[]
        axe1.append(mat[i][i])
        axe2.append(mat[i][constant])
        constant-=1
        for j in range(0,3):
            row.append(mat[i][j])
            colum.append(mat[j][i])
        if ["X","X","X"] in(row , colum , axe1, axe2):
            if choic==1:
                print("*"*20,"\nplayer_2  win")
            else:print("*"*20,"\nyou lose")
            display()
            stop_1=1
            break
        if ["O","O","O"] in(row , colum , axe1, axe2):
            if choic==1:
                print("*"*20,"\nplayer_1 win")
            print("*"*20,"\nyou win")
            display()
            stop_1=1
            break
    #to check if the Game end or Not.
    for t in mat:
        for u in t:
            if u =="_":
                stop_2=1
continu="y"
while continu=="y":
    choic=int(input("\n\nif You are Two players Enter (1) or Enter (2) to play with PC : "))
    if choic==2:
        # whofirst to select who will start game.
        print("the player_1 play with 'O'   player_2 play with 'X'")
        whofirst=r.choice(["pc","player_1"])
        if whofirst=="pc":
            print("PC will start")
        else:print("You will start")
    if choic==1:
        # whofirst to select who will start game.
        whofirst=r.choice(["player_2","player_1"])
        if whofirst=="player_2":
            print("player_2 will start")
            display()
        else:print("player_1 will start")
    
    while True:
        if whofirst=="pc":
            #this loop for computer to choice position of "X".
            while True:
                X=r.choice([0,1,2])
                y=r.choice([0,1,2])
                z=mat[X][y]
                if z not in("X","O"):
                    mat[X][y] ="X"
                    whofirst="player_1"
                    break
        if whofirst=="player_2":
            while True:
                #this variable index for stor the index like that[[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
                index=[[i,j]for i in range(3) for j in range(3)]
                try:
                    enter=int(input("For Player_2 'X':\n"+"plese enter number of position from 1 to 9 in the empty place:"))
                except ValueError as e:
                    print(e)
                    continue
                #this to check if input from 1 to 9
                if enter in [i for i in range(1,10)]:
                    userinput=index[enter-1]
                    f=mat[userinput[0]][userinput[1]]
                    if f not in("X" ,"O"):
                        mat[userinput[0]][userinput[1]]="X"
                        whofirst="player_1"
                        break
                    else:print("Are you joking ? Do you want to play on old play ?")
                else:print("your number is out of range 1 to 9")
            
        # to show the bord of 'XO' and check if game is end or not.
        display()
        check()
        # end if he win or lose.
        if stop_1==1:
            break
        #end if  all positions are complet and no one is winer.
        if stop_2==0:
            print("the game is end")
            break
        # and this for player_1 to choice his\him position of "O"
        if whofirst=="player_1":
            while True:
                #this variable index for stor the index like that[[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
                index=[[i,j]for i in range(3) for j in range(3)]
                try:
                    string="'O':\n"+"plese enter number of position from 1 to 9 in the empty place:"
                    enter=int(input(f"For Player_1 {string}" if choic==1 else f"For Player {string}"))
                except ValueError as e:
                    print(e)
                    continue
                #this to check if input from 1 to 9
                if enter in [i for i in range(1,10)]:
                    userinput=index[enter-1]
                    f=mat[userinput[0]][userinput[1]]
                    if f not in("X" ,"O"):
                        mat[userinput[0]][userinput[1]]="O"
                        if choic==1:
                            whofirst="player_2"
                        else:
                            whofirst="pc"
                        break
                    else:print("Are you joking ? Do you want to play on old play ?")
                else:print("your number is out of range 1 to 9")
        display()
        check()
    
        if stop_1==1:
            break
        if stop_2==0:
            if whofirst=="pc":
                display()
            print("the game is end")
            break
    continu=str(input("To play again enter (y) If NOt enter (n): "))