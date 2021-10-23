board = [0,1,2,3,4,5,6,7,8,9]

def display_board(board):
    print(board[1],'|',board[2],'|',board[3])
    print(board[4],'|',board[5],'|',board[6])
    print(board[7],'|',board[8],'|',board[9])

#Game win or loss

def game_result():
    if board[1] == board[2] == board[3] == "X":
        print("X won the game")
    elif board[4] == board[5] == board[6] == "X":
        print("X won the game")
    elif board[7] == board[8] == board[9] == "X":
        print("X won the game")
    elif board[1] == board[5] == board[9] == "X":
        print("X won the game")
    elif board[3] == board[5] == board[7] == "X":
        print("X won the game")
    elif board[1] == board[4] == board[7] == "X":
        print("X won the game")
    elif board[2] == board[5] == board[8] == "X":
        print("X won the game")
    elif board[3] == board[6] == board[9] == "X":
        print("X won the game")
    elif board[4] == board[5] == board[6] == "O":
        print("O won the game")
    elif board[7] == board[8] == board[9] == "O":
        print("O won the game")
    elif board[1] == board[5] == board[9] == "O":
        print("O won the game")
    elif board[3] == board[5] == board[7] == "O":
        print("O won the game")
    elif board[1] == board[4] == board[7] == "O":
        print("O won the game")
    elif board[2] == board[5] == board[8] == "O":
        print("O won the game")
    elif board[3] == board[6] == board[9] == "O":
        print("O won the game")
    elif board[1] == board[2] == board[3] == "O":
        print("O won the game")
    else:
        pass



#Position Choice

def position_choice():
    choice = input("Where do you want to place? (1-9)? ")
    return int(choice)




#Func for taking user input and placing on the board
def placing_input(board, position):
    marker_input = input("Choose your marker 'X' or 'O': ")

    board[position]= marker_input

    return board







#logic

#1st Round

display_board(board)


position = position_choice()

placing_input(board, position)

display_board(board)  

game_result()

#2nd round

position = position_choice()

placing_input(board, position)

display_board(board)

game_result()

#3rd round

position = position_choice()

placing_input(board, position)

display_board(board) 

game_result()

#4th round
position = position_choice()

placing_input(board, position)

display_board(board)

game_result()

#5th round
position = position_choice()

placing_input(board, position)

display_board(board)

game_result()
#6th round
position = position_choice()

placing_input(board, position)

display_board(board)

game_result()
#7th round
position = position_choice()

placing_input(board, position)

display_board(board)

game_result()

#8th round
position = position_choice()

placing_input(board, position)

display_board(board)

game_result()

#9th round

position = position_choice()

placing_input(board, position)

display_board(board)

#Result out

game_result()













