import random
matrix = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]
def print_matrix():
    for row in matrix:
        print(" | ".join(str(elem) for elem in row))
        print("-" * 9)
def check_winner(player):
    return (
        (matrix[0][0] == matrix[0][1] == matrix[0][2] == player) or
        (matrix[1][0] == matrix[1][1] == matrix[1][2] == player) or
        (matrix[2][0] == matrix[2][1] == matrix[2][2] == player) or
        (matrix[0][0] == matrix[1][0] == matrix[2][0] == player) or
        (matrix[0][1] == matrix[1][1] == matrix[2][1] == player) or
        (matrix[0][2] == matrix[1][2] == matrix[2][2] == player) or
        (matrix[0][0] == matrix[1][1] == matrix[2][2] == player) or
        (matrix[0][2] == matrix[1][1] == matrix[2][0] == player)
    )

def is_full():
    for row in matrix:
        for cell in row:
            if cell not in ["X", "O"]:
                return False
    return True

print("Welcome to x o")
print_matrix()


while True:
    print("your turn:")
    while True:
        try:
            move = int(input("Enter the position (0-8): "))
            if move in [matrix[i][j] for i in range(3) for j in range(3)]:
                break
            else:
                print("Invalid entry. Try again.")
        except ValueError:
            print("Invalid input. Enter a number between 0 and 8.")
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == move:
                matrix[i][j] = "X"
                break
    print_matrix()   

    if check_winner("X"):
        print("You win!")
        break
    if is_full():
        print("It's a draw!")
        break
    print("Computer wins!]")
    empty_cells = [(i, j) for i in range(3) for j in range(3) if matrix[i][j] not in ["X", "O"]]
    row, col = random.choice(empty_cells)
    matrix[row][col] = "O"
    print_matrix()

    if check_winner("O"):
        print("Computer wins")
        break
    if is_full():
        print("It's a draw!")
        break

