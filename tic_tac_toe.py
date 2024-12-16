import tkinter #tk-interface (graphical user interface libaray)

def set_tile(row, column):
    global curr_player
    if board[row][column]["text"] != '' or game_over:
        return
    board[row][column]["text"] = curr_player # mark the board

    if curr_player == playerO:
        curr_player = playerX
    else:
        curr_player = playerO

    label["text"] = curr_player+"'s turn"
    
    #check winner
    chekc_winner()

    pass

def chekc_winner():
    global turns, game_over
    turns += 1
    
     # horizontal chekc 3 rows
    for row in range(3):
       if board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] and board[row][0]["text"] != '':
           label.config(text=board[row][0]["text"]+" is the winner!", foreground=color_yellow)
           for column in range(3):
               board[row][column].config(foreground=color_yellow, background=color_blue)
           game_over = True
           return
    
    # vertical check 3 columns 
    for col in range(3):
       if board[0][col]["text"] ==  board[1][col]["text"] == board[2][col]["text"]  and board[0][col]["text"] != '':
           label.config(text=board[0][col]["text"]+" is the winner!", foreground=color_yellow)
           for row in range(3):
               board[row][col].config(foreground=color_yellow, background=color_blue)
           game_over = True
           return
    
    # check diagonally
    if ( board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and board[0][0]["text"] != ''):
           label.config(text=board[0][0]["text"]+" is the winner!", foreground=color_yellow)
           for row in range(3):
               board[row][row].config(foreground=color_yellow, background=color_blue)
           game_over = True
           return
    if ( board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] and board[0][2]["text"] != ''):
           label.config(text=board[0][2]["text"]+" is the winner!", foreground=color_yellow)
           for row in range(3):
               board[row][2-row].config(foreground=color_yellow, background=color_blue)
           game_over = True
           return

    #tie 
    if (turns == 9):
           game_over = True
           label.config(text = "Tie", foreground = color_yellow)

def new_game():
    global turns, game_over

    turns = 0
    game_over = False

    label.config(text = curr_player+"'s turn", foreground="white")

    for row in range(3):
        for col in range(3):
            board[row][col].config(text='', foreground = color_blue, background = color_gray)
    pass
#game setup 
playerX = "X"
playerO = "O"
curr_player = playerX

board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

color_blue = "#4584b6"
color_yellow = "#ffde57"
color_gray = "#343434"
color_light_gray = "#646464"

turns = 0
game_over = False
#window setup
window = tkinter.Tk() # create the game window
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text = curr_player + "'s turn", font = ("consolas", 20), background=color_gray)

label.grid(row = 0, column = 0, columnspan=3, sticky="we")
for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text='', font=("consolar", 50, "bold"),background=color_gray,\
                                          foreground= color_blue, width = 4, height=1,\
                                          command= lambda row=row, column = column: set_tile(row, column)) 
        board[row][column].grid(row = row + 1, column = column)    
        
button = tkinter.Button(frame, text="Restart", font=("consolas", 20), background=color_gray,foreground="white",\
                        command=new_game)
button.grid(row=4, column=0, columnspan=3, sticky='we')

frame.pack()

#center the window

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

#format "(w)*(h)+(x)+(y)" space bhi aise hi hona chiye mtlab no extra space 
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()

