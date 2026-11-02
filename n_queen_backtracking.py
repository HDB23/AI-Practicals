N = 8
def is_safe(cols, row, col):
    """Can we put a queen at (row, col)? cols[r] = column of queen in row r."""
    for r in range(row):
        if cols[r] == col:                        # same column
            return False
        if abs(cols[r] - col) == abs(r - row):    # same diagonal
            return False
    return True
def solve(cols, row, solutions):
    if row == N:                                  # all 8 queens placed
        solutions.append(cols[:])
        return
    for col in range(N):
        if is_safe(cols, row, col):
            cols.append(col)                      # place queen
            solve(cols, row + 1, solutions)       # go to next row
            cols.pop()                            # BACKTRACK: remove queen
def show(cols):
    for r in range(N):
        print(" ".join("Q" if cols[r] == c else "." for c in range(N)))
if __name__ == "__main__":
    solutions = []
    solve([], 0, solutions)
    print(f"Total solutions for {N}-Queens: {len(solutions)}\n")
    print("First solution (column of queen in each row):", solutions[0], "\n")
    show(solutions[0])