print('Welcome to XO game , You are X player , Please select your location from the board of number , Each number ia relaterd to a free location , I wish you a nice time ')
import random
a=[1,2,3,4,5,6,7,8,9] # Free locations
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
wincond=[set(b),set(c),set(d),set(e),set(f),set(g),set(h),set(i)] # conditions SET
for row in matrix:
    print(row)  # Print each row
xl=[] # x  List ofselections
ol=[] # o List of selections
winner = False # winner code continue stop control
while not winner :
    x=int(input('please input x location from board    ')) # X location input selection
    print('You selected      ',x)
    if x in a :
      matrix[a1[x-1]][a2[x-1]]='X'
      for row in matrix:
        print(row)
      a.remove(x) # Removing last selection from the original selections
      xl=xl+[x] # Update  List of selections X
      for condition in wincond :
        if condition.issubset(set(xl)) == True :
         winner=True
         print('X wins Game over')
      if winner :
        break
      elif len(a) == 0 :
        print('No more locations No Winners Game over')
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
      a.remove(o)
      ol=ol+[o] # Update List of selections
      for condition in wincond :
        #print(condition)
        if condition.issubset(set(ol)) == True :
         winner=True
         print('O wins Game over')
      if winner :
        break
