print("\033[34mWELCOME TO OPEN SIZE XO GAME\033[0m")
import random
while True:
  n = int(input('Please input an odd number for the XO order 3 for 3x3 or 5 for 5x5 or 9 for 9x9 ...etc: '))
  if n % 2 == 0:
   print('Invalid input. Please enter an odd number.')
  else:
    break                                                                                # Exit the loop if n is odd
print('your game order =       ',n)
a=[i+1 for i in range(n*n)]                                                                          #free locations
a1=[]
for i in range(n):
    a1.extend([i] * n)
a2=[]
a2=[i for i in range(n)]*n
w1 = [a[i:i + n] for i in range(0, len(a), n)]                                                    #list of winning raws
#w1s=[[f"{item:<5}" for item in row] for row in w1] 
w1s=[['{:^7}'.format(str(item)) for item in sublist] for sublist in w1] #Transfer winning list from integer into string
matrix = w1s
for row in matrix:
    print(row)
w2 = [[a[i + j * n] for j in range(n)] for i in range(n)]                                       #list of winning columns
w3 = [[a[i * (n+1)] for i in range(n)], [a[(n-1) + i * (n-1)] for i in range(n)]]                  #list of winning axis
w=w1+w2+w3                                                                         # list contains all winning conditions
wincond = [set(sublist) for sublist in w]                                           #winner conditions from list into set
xl=[]                                                                                           # x  List of x selections
ol=[]                                                                                           # o List of  o selections
winner = False                                                                        # winner code continue stop control
while not winner :
    print("\033[31mIF ANYTIME YOU WANT STOP PLEASE ENTER 3333\033[0m")
    x=int(input('please input x location from board    '))                                   # X location input selection
    print('You selected      ',x)
    if x in a :
      matrix[a1[x-1]][a2[x-1]]= '\033[34m   X   \033[0m'
      a.remove(x)                                                    # Removing last selection from the original selections
      xl=xl+[x] # Update  List of selections X
      for condition in wincond :
        if condition.issubset(set(xl))  :
         winner=True
         for row in matrix:                                                                          # print X winner matrix
            print("".join(row))
         print('X wins Game over')
      if winner :
        break
      elif len(a) == 0 :
        for row in matrix :                                                                          # print no winner  matrix 
          print("".join(row))
        print('No more locations , No Winners Game over, Please restart')
        break
    elif x==3333 :                                                                                            #STOP SELECTION
      print("\033[31mFORCE STOP BY USER\033[0m")
      break    
    else :
      print(' Not avialable , Please select again')
      continue
    o=random.choice(a)                                                                 # O selections from avialable locations
    print('Your opponent selected =    ',o)
    if o in a:
      matrix[a1[o-1]][a2[o-1]]= '\033[31m   O   \033[0m'                                                        # Update matrix
      for row in matrix:                                                                                 # print updated matrix
        print("".join(row))
      a.remove(o)
      ol=ol+[o]                                                                                       # Update List of selections
      for condition in wincond :   
        if condition.issubset(set(ol)) == True :
         winner=True
         print('O wins , Game over')
      if winner :
        break
