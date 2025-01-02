"""X O  game"""
from termcolor import colored 

#omar's part start
import random as r
mat=[["_","_","_"],
     ["_","_","_"],
     ["_","_","_"]]
#these two variables to select whene the game is over or not
S1=0
S2=0

def display():
    """this func to show the game """
    print(">"*50)
    for i in mat:
        for j in i:
            if j=="X":
                print(colored(j,"red",None,["bold","blink"]),end="  ")
            elif j=="O":
                print(colored(j,"green",None,["bold","blink"]),end="  ")
            else:
                print(colored(j,"white","on_white",["bold","blink"]),end="  ")
        print("\n")
#omar's part end


def check():
    """this function to check if the player win or lose."""
    global S1,S2
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
            if choic==2:
                print("\\/"*25,colored("\n\nplayer_2  =>'win'","yellow",None,["bold","blink"]))
            else:print("\\/"*25,colored("\n\nyou lose","red",None,["bold","blink"]))
            display()
            S1=1
            break
        if ["O","O","O"] in(row , colum , axe1, axe2):
            if choic==2:
                print("\\/"*25,colored("\n\nplayer_1 =>'win'","yellow",None,["bold","blink"]))
            else:print("\\/"*25,colored("\n\nyou =>'win'","yellow",None,["bold","blink"]))
            display()
            S1=1
            break
    #to check if the Game end or Not.
    S2=0
    for t in mat:
        for u in t:
            if u =="_":
                S2=1
GO="y"
#******************this loop to end game or try again.****************************
while GO=="y":


    #***this loop to aske the player if he want to play with PC or with his frind*****
    while True:
        try:
            choic=int(input(colored("\nFOR one player Enter (1) and FOR two players Enter (2) : ","magenta","on_grey")))
            if choic not in [1,2]:
                print("please enter  1 or 2")
            else:
                print(">"*50)
                break
        except ValueError :
            print("please enter  1 or 2")
    if choic==1:
        # W to select who will start game.
        W=r.choice(["pc","player_1"])
        if W=="pc":
            print(colored("PC will start","red"))
        else:
            print(colored("You will start","green"))
    if choic==2:
        # W to select who will start game.
        print("the player_1 play with 'O'   player_2 play with 'X'")
        W=r.choice(["player_2","player_1"])
        if W=="player_2":
            print(colored("player_2 will start","red"))
            display()
        else:print(colored("player_1 will start","green"))



#******************this loop to display the game***********************
    while True:
        if W=="pc":
            #this loop for computer to choice position of "X".
            while True:
                X=r.choice([0,1,2])
                y=r.choice([0,1,2])
                z=mat[X][y]
                if z not in("X","O"):
                    mat[X][y] ="X"
                    W="player_1"
                    break
        if W=="player_2":
            while True:
                #this variable index for stor the index like that[[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
                index=[[i,j]for i in range(3) for j in range(3)]
                try:
                    text=colored("plese enter number of position from 1 to 9 in the empty place:","magenta","on_grey")
                    text2=colored("For Player_2 'X'\n","red")
                    enter=int(input(text2+text))
                except ValueError as e:
                    print(e)
                    continue
                #this to check if input from 1 to 9
                if enter in range(1,10):
                    userinput=index[enter-1]
                    f=mat[userinput[0]][userinput[1]]
                    if f not in("X" ,"O"):
                        mat[userinput[0]][userinput[1]]="X"
                        W="player_1"
                        break
                    print("Are you joking ? Do you want to play on old play ?")
                else:print("your number is out of range 1 to 9")

        # to show the bord of 'XO' and check if game is end or not.
        display()
        check()
        # end if he 'win !'or lose.
        if S1==1:
            break
        #end if  all positions are complet and no one is winer.
        if S2==0:
            print("the match ended in a draw with.")
            break
        # and this for player_1 to choice his\him position of "O"
        if W=="player_1":
            while True:
                #this variable index for stor the index like that[[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
                index=[[i,j]for i in range(3) for j in range(3)]
                try:
                    tex=colored("plese enter number of position from 1 to 9 in the empty place:","magenta","on_grey")
                    V=colored("For Player_1 'O'\n","green")+tex
                    D=colored("For Player 'O'\n","green")+tex
                    enter=int(input(V if choic==2 else D))
                except ValueError as e:
                    print(e)
                    continue
                #this to check if input from 1 to 9
                if enter in range(1,10):
                    userinput=index[enter-1]
                    f=mat[userinput[0]][userinput[1]]
                    if f not in("X" ,"O"):
                        mat[userinput[0]][userinput[1]]="O"
                        if choic==2:
                            W="player_2"
                        else:
                            W="pc"
                        break
                    print("Are you joking ? Do you want to play on old play ?")
                else:print("your number is out of range 1 to 9")
        display()
        check()
        if S1==1:
            break
        if S2==0:
            if W in("pc","player_2"):
                display()
            print("the match ended in a draw with.")
            break
    #****this variable to aske the player if he want play again or not******
    GO=str(input("\\/"*25+"\nTo play again enter (y)  And to exit enter any key another: "))
    print(">"*50)
    if GO=="y":
        mat=[["_","_","_"],
             ["_","_","_"],
             ["_","_","_"]]
        S1=0
        S2=0
    else:print("the game is closed.")
