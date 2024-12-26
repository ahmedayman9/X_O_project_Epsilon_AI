import random as r
mat=[["","","_"],
     ["","","_"],
     ["","","_"]]

def display():
    for i in mat:
        print(i)
display()
print("*"*50)
while True:
    while True:
        x=r.choice([0,1,2])
        y=r.choice([0,1,2])
        z=mat[x][y]
        if z!="x" and z!="o":
            mat[x][y] ="x"
            break    
    display()
    userinput=list(map(int,input("enter your position as '1 0' :").split()))
    mat[userinput[0]][userinput[1]]="o"
    display()
    print("*"*50)