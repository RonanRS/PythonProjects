
# ----- Global variables -----


# Game board

board = ["-", "-", "-", 
         "-", "-", "-", 
         "-", "-", "-", ]


# if game still going
game_still_going = True


# Whi won? Or tie?
winner = None


# Whos turn is it
current_player = "X"





# ----- Functions -----

# display board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# play a game of tic tac toe
def play_game():
    # Display initial board
    display_board()

    # while the game is still going
    while game_still_going:
        
        # handle a single turn of an arbitrary player
        handle_turn(current_player)

        # check if the game has ended
        check_if_game_over()

        # flip to the other player
        flip_palyer()

    # The game has ended

    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie")



 # handle a single turn of an arbitrary player
def handle_turn(player):

    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")


    valid = False
    while not valid:

        # checking wrong caracter input
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose a position from 1-9 using numbers only.")

        position = int(position) -1

        if board[position] == "-":
            valid = True
        else:    
            print("You can't go there, try another square.")
        

    
    board[position] = player
    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():

    # Set up global variables
    global winner

    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner

    elif column_winner:
        winner = column_winner

    elif diagonal_winner:
        winner = diagonal_winner

    else:
        winner = None
    return


def check_rows():

    # Set up global variables
    global game_still_going

    # Check if any rows have the same value (and is not empty)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    
    # if any row have a match, flag that there's a win
    if row_1 or row_2 or row_3:
        game_still_going = False

    # return the winner (X or O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():

     # Set up global variables
    global game_still_going

     # if any column have a match, flag that there's a win
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3:
        game_still_going = False

    # return the winner (X or O)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


def check_diagonals():

    # Set up global variables
    global game_still_going

    # if any diagonal have a match, flag that there's a win
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"
    if diagonal_1 or diagonal_2:
        game_still_going = False

    # return the winner (X or O)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return


def check_if_tie():
    
    global game_still_going
    
    if "-" not in board:
        game_still_going = False
    return


def flip_palyer():
    
    global current_player

    # if the current player was X, then change it for O
    if current_player == "X":
        current_player = "O"
    # if the current player was O, then change it for X    
    elif current_player == "O":
        current_player = "X"
    return



play_game()





# --------------Scheme--------------
# board
# display board
# play game
# handle turn
# check win
    # check rows
    # check columns
    # check diagonals
# check tie
# flip players