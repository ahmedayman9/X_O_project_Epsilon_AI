import random
a=[1,2,3,4,5,6,7,8,9] # avialable locations list
matrix = [['1','2','3'], ['4','5','6'], ['7','8','9']] #board
a1=[0,0,0,1,1,1,2,2,2] #row index
a2=[0,1,2,0,1,2,0,1,2] #column index
b=[1,2,3] # win condition
c=[4,5,6] # win condition
d=[7,8,9] # win condition
e=[1,4,7] # win condition
f=[2,5,8]  # win condition
g=[3,6,9] # win condition
h=[1,5,9] # win condition
f=[3,5,7] # win condition
i=[3,5,7] # win condition
for row in matrix:
    print(row)  # Print each row
xl=[] # x  List ofselections
ol=[] # o List of selections
while True :
    x=int(input('please input x location from board    ')) # X location input selection
    print('You selected      ',x)
    if x in a :
      matrix[a1[x-1]][a2[x-1]]='X'
      for row in matrix:
        print(row)
      a.remove(x) # Removing last selection from the original selections
      xl=xl+[x] # Update  List of selections X
      cx1= set(b).issubset(set(xl)) # check if x selections wins
      cx2= set(c).issubset(set(xl)) # check if x selelctions wins
      cx3= set(d).issubset(set(xl)) # check if x selelctions wins
      cx4= set(e).issubset(set(xl)) # check if x selelctions wins
      cx5= set(f).issubset(set(xl)) # check if x selelctions wins
      cx6= set(g).issubset(set(xl)) # check if x selelctions wins
      cx7= set(h).issubset(set(xl)) # check if x selelctions wins
      cx8= set(i).issubset(set(xl)) # check if x selelctions wins
      if (cx1 or cx2 or cx3 or cx4 or cx5 or cx6 or cx7 or cx8) == True :
        print('X wins') # Win condition
        break
      elif len(a) == 0 :
        print('no more locations No Winner Game ended')
        break
    else :
      print(' not avialable select again')
      continue
    o=random.choice(a) # O selections from avialable locations
    print('Your opponent selected =    ',o)
    if o in a:
      matrix[a1[o-1]][a2[o-1]]='O' # Update natrix
      for row in matrix: # print updated matrix
        print(row)
      a.remove(o) #update  avialable locations list
      ol=ol+[o] # Update List of selections
      co1= set(b).issubset(set(ol)) # check if o selelctions wins
      co2= set(c).issubset(set(ol)) # check if o selelctions wins
      co3= set(d).issubset(set(ol)) # check if o selelctions wins
      co4= set(e).issubset(set(ol)) # check if o selelctions wins
      co5= set(f).issubset(set(ol)) # check if o selelctions wins
      co6= set(g).issubset(set(ol)) # check if o selelctions wins
      co7= set(h).issubset(set(ol)) # check if o selelctions wins
      co8= set(i).issubset(set(ol)) # check if o selelctions wins
      if (co1 or co2 or co3 or co4 or co5 or co6 or co7 or co8) == True :
        print('O wins')
        break
