from game import NPuzzleState
from search import *

# start = NPuzzleState([
#     [7, 2, 4],
#     [5, 0, 6],
#     [8, 3, 1]
# ])

# goal = NPuzzleState([
#     [0, 1, 2],
#     [3, 4, 5],
#     [6, 7, 8]
# ])

start = NPuzzleState.start(8) 
goal = NPuzzleState.goal(8)

solvers: dict[str, Search] = {
    # 'BFS': BreadthFirstSearch(),
    # 'IDS': IterativeDeepeningSearch(),
    # 'ASTAR_H1': AStarSearch(NPuzzleState.tiles_out_of_place),
    'ASTAR_H2': AStarSearch(NPuzzleState.manhattan_distance),
    # 'BIDIRECTIONAL_ASTAR_H1': BidirectionalAStarSearch(NPuzzleState.tiles_out_of_place),
    # 'BIDIRECTIONAL_ASTAR_H2': BidirectionalAStarSearch(NPuzzleState.manhattan_distance)
}

print('-' * 10 + f' START ' + '-' * 10)
print(start)

print('-' * 10 + f' GOAL ' + '-' * 10)
print(goal)

for name in solvers:
    print('-' * 10 + f' {name} ' + '-' * 10)
    
    solver = solvers[name]
    
    solver.search(start, goal)
    
    for i, state in enumerate(solver.path):
        print('-' * 10 + f' STEP {i} ' + '-' * 10)
        print(state)
    
    print('STEPS:', len(solver.path) - 1)
    print('ELAPSED TIME:', solver.timer)
    print('MAX MEMORY:', solver.memory)
    print('EXPANDED:', solver.expanded)
    print('FACTOR:', solver.expanded / solver.cycles if solver.cycles > 0 else 0)
