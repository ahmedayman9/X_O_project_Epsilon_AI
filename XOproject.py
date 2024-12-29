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


def check(matrix)->list:
    """this function to check if the player win or lose,
        and must take list of lists """
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
        axe1.append(matrix[i][i])
        axe2.append(matrix[i][constant])
        constant-=1
        for j in range(0,3):
            row.append(matrix[i][j])
            colum.append(matrix[j][i])
        if ["X","X","X"] in(row , colum , axe1, axe2):
            print("*"*20,"\nyou lose")
            display()
            stop_1=1
            break
        if ["O","O","O"] in(row , colum , axe1, axe2):
            print("*"*20,"\nyou win")
            display()
            stop_1=1
            break
    #to check if the Game end or Not.
    for t in matrix:
        for u in t:
            if u =="_":
                stop_2=1
# whofirst to select who will start game.
whofirst=r.choice(["pc","player"])
if whofirst=="pc":
    print("PC will start")
else:print("You will start")
plist=[]
while True:
    if whofirst=="pc":
        #this loop for computer to choice position of "X".
        
        while True:
            X=r.choice([0,1,2])
            y=r.choice([0,1,2])
            z=mat[X][y]
            if z not in("X","O"):
                mat[X][y] ="X"
                whofirst="player"
                break
    # to show the bord of 'XO' and check if game is end or not.
    display()
    check(mat)
    # end if he win or lose.
    if stop_1==1:
        break
    #end if  all positions are complet and no one is winer.
    if stop_2==0:
        print("the game is end")
        break
    # and this for player to choice his\him position of "O"
    if whofirst=="player":
        while True:
            #this variable index for stor the index like that[[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
            index=[[i,j]for i in range(3) for j in range(3)]
            try:
                enter=int(input("plese enter number of position from 1 to 9 in the empty place:"))
            except ValueError as e:
                print(e)
                continue
            #this to check if input from 1 to 9
            if enter in [i for i in range(1,10)]:
                userinput=index[enter-1]
                f=mat[userinput[0]][userinput[1]]
                if f not in("X" ,"O"):
                    mat[userinput[0]][userinput[1]]="O"
                    whofirst="pc"
                    break
                else:print("Are you joking ? Do you want to play on old play ?")
            else:print("your number is out of range 1 to 9")
    check(mat)
    if stop_1==1:
        break
    if stop_2==0:
        if whofirst=="pc":
            display()
        print("the game is end")
        break
