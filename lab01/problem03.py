"""
Repeat with intial state =
Initial state = 123
405
786
Using both of DFS, BFS and A*
"""

import numpy as np

from lab01.problem01 import EightPuzzle, h_manhattan, h_manhattan_lsq, h_linear, h_linear_lsq
from lab01.problem02 import Puzzle

start = np.array([[1, 2, 3], [4, 0, 5], [7, 8, 6]])
goal = np.array([[1, 2, 3], [4, 5, 6], [7, 0, 8]])
startIndex = (1, 1)
goalIndex = (1, 0)
p = Puzzle(start, startIndex, goal, goalIndex)
p.solve()
p.print()


p = EightPuzzle([[1, 2, 3], [4, 0, 5], [7, 8, 6]])

print(p)

path, count = p.solve(h_manhattan)
path.reverse()
for i in path:
    print(i)

print("Solved with Manhattan distance exploring", count, "states")
path, count = p.solve(h_manhattan_lsq)
print("Solved with Manhattan least squares exploring", count, "states")
path, count = p.solve(h_linear)
print("Solved with linear distance exploring", count, "states")
path, count = p.solve(h_linear_lsq)
print("Solved with linear least squares exploring", count, "states")