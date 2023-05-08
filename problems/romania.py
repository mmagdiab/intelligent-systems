from search import *

romania_problem = GraphProblem('Bucharest', 'Arad', romania_map)
solution=breadth_first_tree_search(romania_problem).solution()
print(solution)
