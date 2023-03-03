from board import *
from TARS import *

userInput = None
board = create_board()

# Global Variables
whiteTurn = True


print("Hello there! Welcome to TARS, a chess engine written in Python!")

while(True):
    print("Would you like to play 2 player or the ai? (2p/ai)")
    userInput = input("Enter your choice: ")

    if userInput == "2p" or userInput == "ai":
        break

if userInput == "2p":
    while userInput != "quit":

        #First thign to do is check for a stalemate, if so end the game in a tie
        ans = check_for_stalemate(board, whiteTurn)
        if ans:
            print("Stalemate! Game over!")
            break

        #Check if the game is in checkmate
        if whiteTurn:
            if checkmate(board, whiteTurn, "bK"):
                print("Checkmate! Black wins!")
                break
        else:
            if checkmate(board, whiteTurn, "wK"):
                print("Checkmate! White wins!")
                break

        print_board(board)
        userInput = input("Enter your move: ")

        if userInput == "quit":
            break

        #Check if the move is a castle
        if userInput == "O-O" or userInput == "O-O-O":
            board, isCastle = castle(board, whiteTurn, userInput)

        else:
            startRow, startColumn, endRow, endColumn = get_moves_from_user_input(userInput)
            board, ans = make_move(board, whiteTurn, startRow, startColumn, endRow, endColumn)

            if not ans:
                continue

        #Check if the game is in checkmate
        if whiteTurn:
            if checkmate(board, whiteTurn, "wK"):
                print("Checkmate!, Black wins!")
                break
        else:
            if checkmate(board, whiteTurn, "bK"):
                print("Checkmate!, White wins!")
                break

        whiteTurn = not whiteTurn


#TARS ENGAGE
else:
    aiColour = None

    while(True):
        print("Would you like to play as white or black? (w/b)")
        player = input("Enter your choice: ")

        if player == "w" or player == "b":
            break

    if player == "w":
        aiColour = "b"
    else:
        aiColour = "w"

    while userInput != "quit":

        if (player == "w" and whiteTurn) or (player == "b" and not whiteTurn):

            #First thign to do is check for a stalemate, if so end the game in a tie
            ans = check_for_stalemate(board, whiteTurn)
            if ans:
                print("Stalemate! Game over!")
                break

            #Check if the game is in checkmate
            if whiteTurn:
                if checkmate(board, whiteTurn, "bK"):
                    print("Checkmate! Black wins!")
                    break
            else:
                if checkmate(board, whiteTurn, "wK"):
                    print("Checkmate! White wins!")
                    break

            print_board(board)
            userInput = input("Enter your move: ")

            if userInput == "quit":
                break

            #Check if the move is a castle
            if userInput == "O-O" or userInput == "O-O-O":
                board, isCastle = castle(board, whiteTurn, userInput)

            else:
                startRow, startColumn, endRow, endColumn = get_moves_from_user_input(userInput)
                board, ans = make_move(board, whiteTurn, startRow, startColumn, endRow, endColumn)

                if not ans:
                    continue

            #Check if the game is in checkmate
            if whiteTurn:
                if checkmate(board, whiteTurn, "wK"):
                    print("Checkmate!, Black wins!")
                    break
            else:
                if checkmate(board, whiteTurn, "bK"):
                    print("Checkmate!, White wins!")
                    break

        else:
            board, ans, alpha, beta = depth_first_search(board, whiteTurn, 0, aiColour, aiColour, True, -1000000, 1000000)
            print("Alpha = ", alpha)
            print("Beta = ", beta)

        whiteTurn = not whiteTurn
