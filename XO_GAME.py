
import random
game = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]
counter = 0
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
    print(counter)
    
    while True:
        user = int(input("Choose a place to put an 'O' :- \n123 \n456 \n789"))
        if user == 1 and game[0][0] == "":
            game[0][0] = "o"
            break
        elif user == 2 and game[0][1] == "":
            game[0][1] = "o"
            break
        elif user == 3 and game[0][2] == "":
            game[0][2] = "o"
            break
        elif user == 4 and game[1][0] == "":
            game[1][0] = "o"
            break
        elif user == 5 and game[1][1] == "":
            game[1][1] = "o"
            break
        elif user == 6 and game[1][2] == "": 
            game[1][2] = "o"
            break
        elif user == 7 and game[2][0] == "":
            game[2][0] = "o"
            break
        elif user == 8 and game[2][1] == "":
            game[2][1] = "o"
            break
        elif user == 9 and game[2][2] == "":
            game[2][2] = "o"
            break
        else:
            print('invalid input')
            print(game)

            continue
        
    print(f"{game[0]} \n {game[1]} \n {game[2]}")
    
    counter += 1
    
    while True and counter < 5:
        row = random.randint(0,2)
        col = random.randint(0,2)
        if game[row][col] == "":
            game[row][col] = 'x'
            print(f"My turn: \n{game[0]} \n{game[1]} \n{game[2]}")
            break
    
    

    if check_win(game, "x"):
        print("I won!")
        break
    elif check_win(game, "o"):
        print("You won!")
        break
    elif counter == 5:
        print("It's a tie!")
        break     
    else:
      print("No winner yet.") 
      continue