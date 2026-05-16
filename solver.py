default_board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


# this function is to print the board in a nice format, with lines separating the 3x3 boxes, and spaces between the numbers
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:  # this is to print the horizontal lines after every 3 rows, but not before the first row, also on each coloumn
            print("- - - - - - - - - - - - -") 
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0: # this is to print the vertical lines after every 3 columns, but not before the first column, and on each row
                print(' | ', end='')

            # now print out the numbers on the board
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + ' ', end='') # str is used to allow string concatenation
    

# this function is to find the empty spaces on the board, and return the row and column of the first empty space found
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0: # this is to check if the current cell is empty, which is represented by 0
                return (i, j) # this is to return the row and column of the empty cell as a tuple
    return None # this is to return None if there are no empty cells found, which means the board is complete


def valid(board, number, position):
    # this function is to check if the number is valid in the current position, which means it is not already present in the same row, column, or 3x3 box

    # check row
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i: # this is to check if the number is already present in the same row, and also to ignore the current position
            return False

    # check column
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i: # this is to check if the number is already present in the same column, and also to ignore the current position
            return False

    # check the 3x3 the box we are in. We can access a box using for example (0, 0) for the top left box, (0, 1) for the top middle box, (0, 2) for the top right box(1, 0) for the middle left box, (1, 1) for the middle box, (1, 2) for the middle right box, (2, 0) for the bottom left box, (2, 1) for the bottom middle box, and (2, 2) for the bottom right box. We can calculate the box coordinates using integer division by 3.
    box_x = position[1] // 3  # this is to get the x coordinate of the box, which is the column index divided by 3. It takes values from 0 to 2 becuase max value of position[1] is 8, and 8 // 3 is 2
    box_y = position[0] // 3  # this is to get the y coordinate of the box, which is the row index divided by 3

    for i in range(box_y * 3, box_y * 3 + 3): # this is to loop through the rows of the box, which starts from box_y * 3 and ends at box_y * 3 + 2
        for j in range(box_x * 3, box_x * 3 + 3): # this is to loop through the columns of the box, which starts from box_x * 3 and ends at box_x * 3 + 2
            if board[i][j] == number and (i, j) != position: # this is to check if the number is already present in the same box, and also to ignore the current position
                return False

    return True

def solve(board):
    find = find_empty(board) # this is to find the first empty cell on the board
    if not find: # this is to check if there are no empty cells found, which means the board is complete
        return True
    else:
        row, col = find # this is to unpack the row and column of the empty cell from the tuple returned by find_empty

    for i in range(1, 10): # this is to loop through the numbers from 1 to 9, which are the possible values for a cell in Sudoku
        if valid(board, i, (row, col)): # this is to check if the number i is valid in the current position (row, col)
            board[row][col] = i # this is to place the number i in the current position (row, col)

            if solve(board): # this is to recursively call the solve function to see if it leads to a solution
                return True

            else:
                board[row][col] = 0 # this is to reset the current position (row, col) back to 0 if placing the number i does not lead to a solution

    return False # this is to return False if none of the numbers from 1 to 9 lead to a solution, which means we need to backtrack and try a different number for a previous cell


solve(default_board) # this is to call the solve function with the default board to solve it
print_board(default_board) # this is to print the solved board in a nice format
