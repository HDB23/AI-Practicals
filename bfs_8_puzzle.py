from collections import deque

start = (1,2,3,
         4,0,6,
         7,5,8)

goal = (1,2,3,
        4,5,6,
        7,8,0)

def bfs(start) :
    queue = deque([start])
    visited = {start}
    parent = {start : None}

    while queue :
        current = queue.popleft()

        if current == goal :
            path = []

            while current is not None :
                path.append(current)
                current = parent[current]

            return path[::-1]

        zero = current.index(0)
        row, col = divmod(zero, 3)

        moves = [(-1,0), (1,0), (0,-1), (0,1)]

        for dr, dc in moves :
            r, c = row + dr, col + dc

            if 0 <= r < 3 and 0 <= c < 3 :
                new_pos = r * 3 + c

                new_state = list(current)

                new_state[zero], new_state[new_pos] = (new_state[new_pos], new_state[zero])
                new_state = tuple(new_state)

                if new_state not in visited :
                    visited.add(new_state)
                    parent[new_state] = current
                    queue.append(new_state)
    return None

solution = bfs(start)

if solution:
    print("Solution Found!")
    print("Total Moves:", len(solution) - 1)

    for step, state in enumerate(solution):
        print("\nStep", step)

        for i in range(0, 9, 3):
            print(state[i:i+3])
else:
    print("No Solution Found!")