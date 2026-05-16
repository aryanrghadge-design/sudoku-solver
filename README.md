Sudoku Solver
A Python-based Sudoku solver that uses a recursive backtracking algorithm to solve any valid 9×9 Sudoku board.
How It Works
The solver works by finding empty cells and systematically trying numbers 1–9 in each one. Before placing a number, it checks three constraints:

The number doesn't already appear in the same row
The number doesn't already appear in the same column
The number doesn't already appear in the same 3×3 box

If a placement passes all three checks, the algorithm places the number and recurses to the next empty cell. If it reaches a dead end — a cell where no number is valid — it backtracks, undoing the last placement and trying the next candidate.
This is significantly more efficient than brute force. A naive approach would need to evaluate up to 9^81 possible board configurations. Backtracking prunes invalid branches early, solving most boards in milliseconds.
Algorithm Properties

Correct — guaranteed to find a solution if one exists
Efficient — prunes invalid branches before exploring further, avoiding unnecessary computation

Output Format
The solved board is printed with horizontal and vertical separators every 3 rows and columns, replicating the visual structure of a standard Sudoku grid.
7 8 5  | 4 3 9  | 1 2 6
6 1 2  | 8 7 5  | 3 4 9
4 9 3  | 6 2 1  | 5 7 8
- - - - - - - - - - - - -
8 5 7  | 9 4 3  | 2 6 1
2 6 1  | 7 5 8  | 9 3 4
9 3 4  | 1 6 2  | 7 8 5
- - - - - - - - - - - - -
5 7 8  | 3 9 4  | 6 1 2
1 2 6  | 5 8 7  | 4 9 3
3 4 9  | 2 1 6  | 8 5 7
...
Usage:
pythonpython sudoku_solver.py
To use a custom board, modify the default_board variable in the script. Use 0 to represent empty cells.


Python 3
No external libraries required
