import random


puzzle = [
    [
        random.randint(1, 9) for j in range(0, 9)
    ] for i in range(0,9)
]


def fill_row(row):
    B = [i for i in range(1, len(row) + 1)]
    for i in range(0, len(row)):
        C = random.randint(0, len(B) - 1)
        row[i] = B.pop(C)


def fill_puzzle(puzzle):
    A = fill_row(puzzle[0])
    for i in range():




def draw_puzzle(puzzle):
    for y in range(0, len(puzzle)):
        for x in range(0, len(puzzle[y])):
            if x > 0 and x % 3 == 0:
                print("|", puzzle[y][x], end=' ')
            else:
                print(puzzle[y][x], end=' ')
        if y + 1 in (3, 6):
            print("\n" + "-" * 21)
        else:
            print("")


for pz in puzzle:
    fill_row(pz)
draw_puzzle(puzzle)