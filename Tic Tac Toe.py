#this is the code for tic tac toe
""" Concept : we will create a total of 9 tuples within
the give parent list to access the elements of the grid.
Then we will create a function which will contain 3 checking cases  for column , diagonal , row
We will make 2 user input different and the user will enter only the row and column number
To c
"""
import tkinter as tk
Li=[
    ["","",""],
    ["","",""],
    ["","",""]
   ]
player = "O"
count = 0  
def user(x,row,column):

    if Li[row][column]!="":
        status["text"] = "Cannot Override an existing input"
        return False
    
    Li[row][column]=x
    buttons[row][column]["text"] = x
    return True

def win(y,row,column):
  
    if(Li[0][0]==Li[1][1]==Li[2][2]==y):
        status["text"] = "Game End\nWins = " + y
        return False

    if(Li[row][0]==Li[row][1]==Li[row][2]==y):
        status["text"] = "Game End\nWins = " + y
        return False

    if(Li[0][column]==Li[1][column]==Li[2][column]==y):
        status["text"] = "Game End\nWins = " + y
        return False

    if(Li[0][2]==Li[1][1]==Li[2][0]==y):
        status["text"] = "Game End\nWins = " + y
        return False

    return True

def click(row, column):
    
    global player, count
    
    if user(player, row, column) == False:
        return None

    count += 1
    
    if win(player, row, column) == False:
        disable()
        return None
    
    if count == 9:
        status["text"] = "Game Draw"
        disable()
        return None
    
    # switching between player
    
    if player == "O":
        player = "X"
        status["text"] = "User 2 turn"
    else:
        player = "O"
        status["text"] = "User 1 turn"
        
def disable():
    for r in range(3):
        for c in range(3):
            buttons[r][c]["state"] = "disabled"
    
root = tk.Tk()
root.title("Tic Tac Toe")

buttons = []

for r in range(3):
    row = []
    for c in range(3):
        b = tk.Button(root,text="",font=("Times New Roman", 24),width=6,height=3,command=lambda r=r, c=c: click(r, c))
        b.grid(row=r, column=c)
        row.append(b)
    buttons.append(row)

status = tk.Label(root, text="User 1 turn", font=("Arial", 16))
status.grid(row=3, column=0, columnspan=3)

root.mainloop()
