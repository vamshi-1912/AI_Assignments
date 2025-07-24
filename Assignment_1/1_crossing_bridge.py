from collections import deque

people = {'vamshi':10, 'uday':20, 'adarsh':20, 'vinay':25}

def is_goal(state):
    return len(state[0]) == 0 and len(state[1]) == 4

def get_successors(state):
    left, right, torch, time = state
    successors = []
    if torch == 'L':
        for i in range(len(left)):
            for j in range(i+1, len(left)):
                p1, p2 = left[i], left[j]
                new_left = [p for p in left if p not in (p1, p2)]
                new_right = right + [p1, p2]
                added_time = max(people[p1], people[p2])
                successors.append((new_left, new_right, 'R', time + added_time))
    else:
        for i in range(len(right)):
            p = right[i]
            new_right = [r for r in right if r != p]
            new_left = left + [p]
            added_time = people[p]
            successors.append((new_left, new_right, 'L', time + added_time))
    return successors

def bfs_bridge():
    initial_state = (['vamshi','uday','adarsh','vinay'], [], 'L', 0)
    queue = deque([(initial_state, [])])
    visited = set()
    while queue:
        (left, right, torch, time), path = queue.popleft()
        state_key = (tuple(sorted(left)), tuple(sorted(right)), torch)
        if state_key in visited or time > 60:
            continue
        visited.add(state_key)
        if is_goal((left, right, torch, time)):
            return path + [((left, right, torch), time)]
        for new_state in get_successors((left, right, torch, time)):
            queue.append((new_state, path + [((left, right, torch), time)]))
    return None

def dfs_bridge(state, path, visited):
    left, right, torch, time = state
    state_key = (tuple(sorted(left)), tuple(sorted(right)), torch)
    if time > 60 or state_key in visited:
        return None
    if is_goal(state):
        return path + [((left, right, torch), time)]
    visited.add(state_key)
    for new_state in get_successors(state):
        result = dfs_bridge(new_state, path + [((left, right, torch), time)], visited)
        if result:
            return result
    return None

print("BFS Solution:")
bfs_result = bfs_bridge()
if bfs_result:
    for step in bfs_result:
        print(f"State: {step[0]}, Time: {step[1]}")
else:
    print("No solution within 60 minutes")

print("\nDFS Solution:")
initial_state = (['vamshi','uday','adarsh','vinay'], [], 'L', 0)
dfs_result = dfs_bridge(initial_state, [], set())
if dfs_result:
    for step in dfs_result:
        print(f"State: {step[0]}, Time: {step[1]}")
else:
    print("No solution within 60 minutes")

