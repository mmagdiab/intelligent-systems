"""
Write a program to get the 8-puzzle after sequence of actions.
Move blank (Right-Left-Up)
"""
from sheet01.problem02 import search


def do_actions(puzzle, actions_sequence):
    blank_row, blank_column = search(puzzle, 0)
    try:
        for action in actions_sequence:
            if action == "R":  # Do the swap, update blank tile position
                puzzle[blank_row][blank_column], puzzle[blank_row][blank_column + 1] = \
                    puzzle[blank_row][blank_column + 1], puzzle[blank_row][blank_column]
                blank_column += 1
            elif action == "L":
                puzzle[blank_row][blank_column], puzzle[blank_row][blank_column - 1] = \
                    puzzle[blank_row][blank_column - 1], puzzle[blank_row][blank_column]
                blank_column -= 1
            elif action == "U":
                puzzle[blank_row][blank_column], puzzle[blank_row - 1][blank_column] = \
                    puzzle[blank_row - 1][blank_column], puzzle[blank_row][blank_column]
                blank_row -= 1
            elif action == "D":
                puzzle[blank_row][blank_column], puzzle[blank_row + 1][blank_column] = \
                    puzzle[blank_row + 1][blank_column], puzzle[blank_row][blank_column]
                blank_row += 1
    except:
        print("Invalid sequence")


arr = [[1, 0, 4],
       [5, 3, 6],
       [7, 2, 8]]
do_actions(arr, "RDL")
print(arr)
