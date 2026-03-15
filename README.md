# Python-Projects
    <h1>Project Overview</h1>
    <p>
        This project contains two Python games: <strong>Tic-Tac-Toe</strong> and <strong>Sudoku</strong>.
        Both programs demonstrate the use of basic programming concepts such as lists, functions, loops,
        and conditional statements. The Tic-Tac-Toe game uses the <strong>Tkinter</strong> library to create
        a graphical user interface. In contrast, the Sudoku game runs in the console and uses a
        <strong>backtracking algorithm</strong> to generate and solve Sudoku boards.
    </p>

    <h2>1. Tic-Tac-Toe Game</h2>
    <p>
        The Tic-Tac-Toe program creates a 3×3 board using nested lists and displays it using
        Tkinter buttons. Two players take turns placing <strong>X</strong> and <strong>O</strong> by clicking
        on the grid. The program checks for winning conditions in rows, columns, and diagonals
        after every move. It also prevents players from overriding an already filled cell.
        If a player wins or the board becomes full, the game stops and displays the result.
    </p>

    <h3>Key Features</h3>
    <ul>
        <li>Graphical interface using Tkinter</li>
        <li>Two-player turn-based gameplay</li>
        <li>Win detection for rows, columns, and diagonals</li>
        <li>Prevention of invalid moves</li>
        <li>Draw detection when the board is full</li>
    </ul>

    <h2>2. Sudoku Game</h2>
    <p>
        The Sudoku program generates a valid 9×9 Sudoku puzzle using a backtracking algorithm.
        The solved Sudoku board is first created automatically. Based on the selected difficulty level
        (<strong>Easy, Medium, Hard</strong>), a certain number of cells are revealed as clues while the
        remaining cells are left empty. The player enters values to complete the puzzle, and the
        program finally checks whether the entered solution is correct.
    </p>

    <h3>Key Features</h3>
    <ul>
        <li>Automatic generation of a solved Sudoku grid</li>
        <li>Random puzzle creation with adjustable difficulty</li>
        <li>User input for filling missing values</li>
        <li>Validation of the final solution</li>
    </ul>

    <h2>Requirements</h2>
    <ul>
        <li>Python 3.x</li>
        <li>Tkinter library (included with standard Python installation)</li>
    </ul>

    <h2>How to Run</h2>
    <ol>
        <li>Save the Tic-Tac-Toe and Sudoku programs as separate Python files.</li>
        <li>Open a terminal or command prompt in the project folder.</li>
        <li>Run the desired game:</li>
    </ol>

    <p><strong>For Tic-Tac-Toe:</strong></p>
    <pre><code>python tic_tac_toe.py</code></pre>

    <p><strong>For Sudoku:</strong></p>
    <pre><code>python sudoku.py</code></pre>

    <h2>Learning Objectives</h2>
    <p>This project helps in understanding:</p>
    <ul>
        <li>Python functions and modular programming</li>
        <li>Lists and nested lists for grid representation</li>
        <li>Basic GUI development using Tkinter</li>
        <li>Algorithmic problem solving using backtracking</li>
        <li>User input handling and validation</li>
    </ul>
