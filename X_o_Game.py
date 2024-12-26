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