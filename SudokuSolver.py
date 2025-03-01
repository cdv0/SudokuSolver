import random
import copy
import heapq
import requests  # Needed if fetching Sudoku from an API

# ========================
# Step 1: Load Sudoku Puzzle
# ========================

def load_sudoku():
    """
    Returns a randomly chosen Sudoku puzzle from predefined puzzles.
    """
    puzzles = [
        # Puzzle 1
        [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ],
        # Puzzle 2
        [
            [0, 0, 3, 0, 2, 0, 6, 0, 0],
            [9, 0, 0, 3, 0, 5, 0, 0, 1],
            [0, 0, 1, 8, 0, 6, 4, 0, 0],
            [0, 0, 8, 1, 0, 2, 9, 0, 0],
            [7, 0, 0, 0, 0, 0, 0, 0, 8],
            [0, 0, 6, 7, 0, 8, 2, 0, 0],
            [0, 0, 2, 6, 0, 9, 5, 0, 0],
            [8, 0, 0, 2, 0, 3, 0, 0, 9],
            [0, 0, 5, 0, 1, 0, 3, 0, 0]
        ]
    ]
    return random.choice(puzzles)

def load_sudoku_from_file(filename="Sudoko_Puzzles.txt"):
    """
    Loads Sudoku puzzles from a text file and returns a random one.
    """
    with open(filename, "r") as file:
        lines = file.readlines()

    puzzles = []
    temp = []

    for line in lines:
        if line.strip():
            temp.append(list(map(int, line.split())))
        else:
            if temp:
                puzzles.append(temp)
            temp = []

    # Add the first puzzle if there's only one puzzle in the txt file
    if temp:
        puzzles.append(temp)

    if not puzzles:
        return None

    return random.choice(puzzles)



# ========================
# Step 2: Validity Check Functions
# ========================

def is_valid(grid, row, col, num):
    """
    Returns True if placing num at (row, col) is valid according to Sudoku rules.
    """
    # Write your code here

def in_row(grid, row, num):
    """
    Checks if num is already present in the row.
    """
    # Write your code here

def in_col(grid, col, num):
    """
    Checks if num is already present in the column.
    """
    # Write your code here

def in_box(grid, row, col, num):
    """
    Checks if num is already present in the 3x3 subgrid.
    """
    # Write your code here

# ========================
# Step 3: Successor Function
# ========================

def get_successors(grid):
    """
    Finds the first empty cell and returns all valid states with one number filled.
    """
    # Write your code here

# ========================
# Step 4: Goal Check
# ========================

def is_goal(grid):
    """
    Returns True if the grid is a valid solved Sudoku.
    """
    # Write your code here

def has_duplicates(lst):
    """
    Returns True if there are duplicate numbers (excluding 0s).
    """
    # Write your code here

# ========================
# Step 5: A* Search Algorithm
# ========================

def heuristic(grid):
    """
    Returns the number of empty cells (lower values are better).
    """
    # Write your code here

def a_star_sudoku(grid):
    """
    Solves Sudoku using A* search.
    """
    # Write your code here


# ========================
# Step 6: Simulated Annealing (SA)
# ========================
def simulated_annealing(grid, max_iter=10000, temp=1.0, cooling_rate=0.99):
    """
    Solves Sudoku using SA search.
    """
    # Write your code here

# ========================
# Step 7: Running and Testing
# ========================

def print_sudoku(grid):
    """
    Prints the Sudoku grid in a readable format.
    """
    for row in grid:
        print(" ".join(str(num) if num != 0 else "." for num in row))
    print()

# Load a Sudoku puzzle (Choose one option)
sudoku_grid = load_sudoku()  # Option 1: Hardcoded
# sudoku_grid = load_sudoku_from_file()  # Option 2: From file


print("Loaded Sudoku Puzzle:")
print_sudoku(sudoku_grid)

# Solve using A*
solved_grid = a_star_sudoku(sudoku_grid)

if solved_grid:
    print("\nSolved Sudoku:")
    print_sudoku(solved_grid)
else:
    print("No solution found.")

# Solve using SA
solved_sa = simulated_annealing(sudoku_grid)

if solved_sa:
    print("\nSolved Sudoku (Simulated Annealing):")
    print_sudoku(solved_sa)
else:
    print("No solution found.")