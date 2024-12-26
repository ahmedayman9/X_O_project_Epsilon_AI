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