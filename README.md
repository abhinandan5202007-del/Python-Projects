# Python-Projects
    # Tic-Tac-Toe and Sudoku Python Games

## **Project Overview**
This project contains two Python games: **Tic-Tac-Toe** and **Sudoku**. Both programs demonstrate the use of basic programming concepts such as **lists, functions, loops, and conditional statements**.  

The **Tic-Tac-Toe** game uses the **Tkinter library** to create a graphical user interface, while the **Sudoku** game runs in the **console** and uses a **backtracking algorithm** to generate and solve Sudoku boards.

---

# **1. Tic-Tac-Toe Game**

The Tic-Tac-Toe program creates a **3×3 board** using nested lists and displays it using **Tkinter buttons**. Two players take turns placing **X** and **O** by clicking on the grid.  

The program checks for **winning conditions in rows, columns, and diagonals** after every move. It also prevents players from overriding an already filled cell. If a player wins or the board becomes full, the game stops and displays the result.

## **Key Features**
- **Graphical interface using Tkinter**
- **Two-player turn-based gameplay**
- **Win detection for rows, columns, and diagonals**
- **Prevention of invalid moves**
- **Draw detection when the board is full**

---

# **2. Sudoku Game**

The Sudoku program generates a **valid 9×9 Sudoku puzzle** using a **backtracking algorithm**. The solved Sudoku board is first created automatically.  

Based on the selected difficulty level (**Easy, Medium, Hard**), a certain number of cells are revealed as clues while the remaining cells are left empty. The player enters values to complete the puzzle, and the program finally checks whether the entered solution is correct.

## **Key Features**
- **Automatic generation of a solved Sudoku grid**
- **Random puzzle creation with adjustable difficulty**
- **User input for filling missing values**
- **Validation of the final solution**

---

# **Requirements**
- **Python 3.x**
- **Tkinter library** (included with standard Python installation)

---

# **How to Run**

1. Save the **Tic-Tac-Toe** and **Sudoku** programs as separate Python files.  
2. Open a **terminal or command prompt** in the project folder.  
3. Run the desired game.
