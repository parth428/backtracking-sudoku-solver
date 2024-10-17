# Sudoku Solver with Backtracking/Rercursion Algorithm with GUI
# Parth Patel

board = [ 
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

# Backtracking Algorithm
def solve(bo):
    # Base Case
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10): # 1-9 inclusive
        if valid(bo, i, (row, col)): # Check if the number is valid
            bo[row][col] = i # If valid, place the number in the board

            if solve(bo): # Recursion
                return True

            bo[row][col] = 0 # Backtrack
    
    return False

# Check if current board is valid
def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i: 
            return False
        
    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
        
    # Check 3x3 boxes
    box_x = pos[1] // 3  
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 +3):
            if bo[i][j] == num and (i, j) != pos:
                return False
            
    return True


# Function to print the board
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ") #

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)
            
    return None

# Print Initial and Solved Board
print("Initial Sudoku Board:")
print_board(board)
solve(board)
print("__________________________")
print("Solved Sudoku Board:")
print_board(board)