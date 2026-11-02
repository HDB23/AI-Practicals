jug1 = 4
jug2 = 3
target = 2

visited = set()

def dfs(x, y) :
    if x == target or y == target :
        print("Goal reached", (x,y))
        return True

    if (x,y) in visited :
        return False

    visited.add((x,y))
    print("Current state : ", (x, y))

    states = [
        (jug1, y),
        (x, jug2),
        (0, y),
        (x, 0),
        (x - min(x, jug2-y), y+min(x, jug2-y)),
        (x + min(y, jug1-x), y-min(y, jug1-x))
    ]

    for state in states :
        if state not in visited :
            if dfs(state[0], state[1]) :
                return True
    return False

print("Water Jug Problem using DFS")

if not dfs(0, 0) :
    print("Solution Not Found !")