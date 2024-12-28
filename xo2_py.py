import random
#from IPython.display import clear_output

a=[1,2,3,4,5,6,7,8,9] #locations
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
   # print('avialable locations = ' ,a)
    x=int(input('please input x location from board    ')) # X location input selection
    #clear_output() # clear screen
    print('You selected      ',x)
    if x in a :
     # print(' len a = ',(len(a)))
      #print(a1[x-1])
      #print(a2[x-1])
      matrix[a1[x-1]][a2[x-1]]='X'
      for row in matrix:
        print(row)
      a.remove(x) # Removing last selection from the original selections
      xl=xl+[x] # Update  List of selections X
    #  print('xl=',xl) # Updated list of selections X
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
    #clear_output()
    print('Your opponent selected =    ',o)
    if o in a:
      #print(a1[o-1]) # raw index
      #print(a2[o-1]) # column index
      matrix[a1[o-1]][a2[o-1]]='O' # Update natrix
      for row in matrix: # print updated matrix
        print(row)
      a.remove(o)
      ol=ol+[o] # Update List of selections
     # print('ol=',ol)   #Updated list of selections O
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