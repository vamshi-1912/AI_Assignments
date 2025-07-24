from collections import deque

initial_state = ('E', 'E', 'E', '_', 'W', 'W', 'W')
goal_state = ('W', 'W', 'W', '_', 'E', 'E', 'E')

def get_neighbors(state):
    neighbors = []
    for i in range(len(state)):
        if state[i] == '_':
            continue
        if state[i] == 'E':
            if i+1 < 7 and state[i+1] == '_':
                s = list(state)
                s[i], s[i+1] = s[i+1], s[i]
                neighbors.append(tuple(s))
            if i+2 < 7 and state[i+1] == 'W' and state[i+2] == '_':
                s = list(state)
                s[i], s[i+2] = s[i+2], s[i]
                neighbors.append(tuple(s))
        elif state[i] == 'W':
            if i-1 >= 0 and state[i-1] == '_':
                s = list(state)
                s[i], s[i-1] = s[i-1], s[i]
                neighbors.append(tuple(s))
            if i-2 >= 0 and state[i-1] == 'E' and state[i-2] == '_':
                s = list(state)
                s[i], s[i-2] = s[i-2], s[i]
                neighbors.append(tuple(s))
    return neighbors

def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        current, path = queue.popleft()
        if current == goal:
            return path
        visited.add(current)
        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    return None

def dfs(start, goal, visited=None, path=None):
    if visited is None: visited = set()
    if path is None: path = [start]
    if start == goal:
        return path
    visited.add(start)
    for neighbor in get_neighbors(start):
        if neighbor not in visited:
            result = dfs(neighbor, goal, visited, path + [neighbor])
            if result:
                return result
    return None

bfs_result = bfs(initial_state, goal_state)
dfs_result = dfs(initial_state, goal_state)

for state in bfs_result:
    print(state)

print()

for state in dfs_result:
    print(state)

