
import random
game = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]
def check_win(game, player):

  for row in game:
    if all(cell == player for cell in row):
      return True

  for col in range(3):
    if all(row[col] == player for row in game):
      return True

  if (game[0][0] == player and game[1][1] == player and game[2][2] == player) or \
     (game[0][2] == player and game[1][1] == player and game[2][0] == player):
    return True

  return False
while True:

    user = int(input("Choose a place to put an 'O' :- \n123 \n456 \n789"))
    
    if user == 1 :
        if game[0][0] != ("o" or "x"):
            game[0][0] = "o"
    elif user == 2:
        if game[0][1] != ("o" or "x"):
            game[0][1] = "o"
    elif user == 3:
        if game[0][2] != ("o" or "x"):
            game[0][2] = "o"
    elif user == 4 :
        if game[1][0] != ("o" or "x"):
            game[1][0] = "o"
    elif user == 5:
        if game[1][1] != ("o" or "x"):
            game[1][1] = "o"
    elif user == 6:
       if game[1][2] != ("o" or "x"): 
           game[1][2] = "o"
    elif user == 7 :
        if game[2][0] != ("o" or "x"):
            game[2][0] = "o"
    elif user == 8:
        if game[2][1] != ("o" or "x"):
            game[2][1] = "o"
    elif user == 9:
        if game[2][2] != ("o" or "x"):
            game[2][2] = "o"
    else:
        print('invalid input')
        
    print(game)
    
    --
    
    if check_win(game, "x"):
      print("Player 'x' has won!")
      break
    elif check_win(game, "o"):
      print("Player 'o' has won!")
      break
    else:
      print("No winner yet.") 
      continue