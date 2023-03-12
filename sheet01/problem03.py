"""Write a function to test if the 8-piece puzzle is arranged."""


def is_arranged(puzzle):
    rows, columns = len(puzzle), len(puzzle[0])
    next_value = 1
    for r in range(rows):
        for c in range(columns):
            if puzzle[r][c] not in [next_value, 0]:
                return False
            next_value = next_value + 1 if puzzle[r][c] != 0 else next_value
    return True

def is_arranged_with_goal(start, goal):
    rows, columns = len(start), len(start[0])
    for r in range(rows):
        for c in range(columns):
            if start[r][c] != goal[r][c]:
                return False
    return True

puzzle_1 = [[1, 0, 2],
            [3, 4, 5],
            [6, 7, 8]]

puzzle_2 = [[1, 0, 4],
            [5, 3, 6],
            [7, 2, 8]]
# print(is_arranged(puzzle_1))
# print(is_arranged(puzzle_2))

print(is_arranged_with_goal(puzzle_2, puzzle_2))
