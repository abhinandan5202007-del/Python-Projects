"""
Concept: This program creates a Sudoku game in Python. First, it generates a valid solved Sudoku board using a backtracking algorithm 
that fills numbers while following Sudoku rules (no repetition in rows, columns, or 3×3 boxes). Based on the chosen difficulty level, 
some numbers are shown as clues while the remaining cells are left empty. The user then enters values to complete the puzzle. 
The program checks inputs, prevents filling already given cells, displays the board after each move, and finally verifies 
whether the user’s solution matches the correct Sudoku solution.
"""
import random
Size = 9
Box = 3

def create_unsolved_board():
    c = []
    for i in range(9):
        row = []
        for j in range(9):
            row.append("")
        c.append(row)
    return c
def create_empty_board():
    b=[]
    for i in range(Size):
        row = []
        for j in range(Size):
            row.append(0)
        b.append(row)

    return b

def is_safe(board, row, col, num):
    # Check row
    for c in range(Size):
        if board[row][c] == num:
            return False

    # Check column
    for r in range(Size):
        if board[r][col] == num:
            return False

    # Check 3x3 box
    start_row = row - row % Box
    start_col = col - col % Box

    for r in range(start_row, start_row + Box):
        for c in range(start_col, start_col + Box):
            if board[r][c] == num:
                return False

    return True

def find_empty_cell(board):
    for row in range(Size):
        for col in range(Size):
            if board[row][col] == 0:
                return row, col
    return None

def solve_board(board):
    empty = find_empty_cell(board)
    if not empty:
        return True   # board filled

    row, col = empty

    numbers = list(range(1, 10))
    random.shuffle(numbers)   # makes each solution different

    for num in numbers:
        if is_safe(board, row, col, num):
            board[row][col] = num

            if solve_board(board):
                return True
            board[row][col] = 0   

    return False

def generate_solved_sudoku():   #creation of solved sudoku
    board = create_empty_board()
    solve_board(board)
    return board

def display(un):    #display the sudoku grid
    for i in range(9):
        print("-"*35)
        for j in range(9):
            print(un[i][j],"|", end=" ")
        print()
    print("-"*35)
    
def sudoku_board(unsolved,solved,clue): #

    global flag,l
    i=1
    flag=0
    l=[]
    while(i<=clue):
        
        row=random.randint(0,8)
        column=random.randint(0,8)
        j=[row,column]
        
        if j not in l:
            
            l.append(j)
            unsolved[row][column]=solved[row][column]
            i+=1
            
    flag=81-len(l)
    display(unsolved)

def user_enter():   #taking user input

    global flag,l
    i=1
    
    while(i<=flag):
        
        try:
            row=int(input("Enter row: "))-1
            column=int(input("Enter column: "))-1
        except:
            print("Invalid input")
            continue
        
        if row >= 0 and column >= 0 and row<9 and column < 9:
            j=[row,column]
            value=int(input("Enter value: "))
            
            if value < 1 or value > 9 :
                print("Invalid number")
                continue
            if j not in l:
                l.append(j)
                unsolved[row][column]=value
                display(unsolved)
                i+=1
                
            else:
                print("Cell already filled")
                
        else:
            print("Invalid input")
        
def check(un,sol):  #check for solution

    for i in range(0,9):
        for j in range(0,9):
            
            if un[i][j]!=sol[i][j]:
                print("\nIncorrect solution\n Try Again!\n")                
                return None
            
    print("Correct Solution !\n")


# Function calls 
print("Welcome to Sudoku !\n")

solved=create_empty_board()
unsolved=create_unsolved_board()

while (True):
    ch=int(input("Choose level:\n1.Easy\n2.Medium\n3.Hard\nEnter number:"))
    if ch ==1 :
        clue=80
        break
    if ch ==2 :
        clue=32
        break
    if ch ==3 :
        clue=25
        break
    else:
        print("Enter again")
        continue       

sudoku = generate_solved_sudoku()
sudoku_board(unsolved,sudoku,clue)
user_enter()
check(unsolved,sudoku)

print("Thank you")
