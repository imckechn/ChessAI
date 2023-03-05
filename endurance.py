# Author: Ian McKechnie
# March 3, 2023
# Chess AI

from board import *
from TARS import *
import globals

def print_ai_move(board, startRow, startColumn, endRow, endColumn):

    pieceName = board[startRow][startColumn]
    startRow += 1
    endRow += 1

    if startColumn == 0:
        startColumn = "A"
    elif startColumn == 1:
        startColumn = "B"
    elif startColumn == 2:
        startColumn = "C"
    elif startColumn == 3:
        startColumn = "D"
    elif startColumn == 4:
        startColumn = "E"
    elif startColumn == 5:
        startColumn = "F"
    elif startColumn == 6:
        startColumn = "G"
    elif startColumn == 7:
        startColumn = "H"

    if endColumn == 0:
        endColumn = "A"
    elif endColumn == 1:
        endColumn = "B"
    elif endColumn == 2:
        endColumn = "C"
    elif endColumn == 3:
        endColumn = "D"
    elif endColumn == 4:
        endColumn = "E"
    elif endColumn == 5:
        endColumn = "F"
    elif endColumn == 6:
        endColumn = "G"
    elif endColumn == 7:
        endColumn = "H"

    print("TARS moved the " + pieceName + " from " + str(startColumn) + str(startRow) + " to " + str(endColumn) + str(endRow))


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

        # This checks if the queen is still on the board, if not the game is over
        # It also prints the winner
        if isGameOver(board):
            break

        if check_for_stalemate(board, whiteTurn) or check_for_stalemate(board, not whiteTurn):
            print("Stalemate! Game over!")
            break

        #Check if the game is in checkmate or check
        if whiteTurn:
            if checkmate(board, "bK"):
                print("Checkmate! Black wins!")
                break

            else:
                if check(board, "bK"):
                    print("Black is in check!")

        else:
            if checkmate(board, "wK"):
                print("Checkmate! White wins!")
                break

            if check(board, "wK"):
                    print("White is in check!")

        if whiteTurn:
            print("White's turn!")
        else:
            print("Black's turn!")

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

        whiteTurn = not whiteTurn

#TARS ENGAGE
else:
    globals.AIGAME = True
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
        print_board(board)

        # This checks if the queen is still on the board, if not the game is over
        # It also prints the winner
        if isGameOver(board):
            break

        if check_for_stalemate(board, whiteTurn) or check_for_stalemate(board, not whiteTurn):
            print("Stalemate! Game over!")
            break

        #Check if the game is in checkmate or check
        if checkmate(board, "bK"):
            print("Checkmate! Black wins!")
            break

        elif check(board, "bK"):
                print("Black is in check!")

        else:
            print("Black is not in check!")

        if checkmate(board, "wK"):
            print("Checkmate! White wins!")
            break

        elif check(board, "wK"):
                print("White is in check!")

        else:
            print("White is not in check!")

        # If it's the player's turn
        if (player == "w" and whiteTurn) or (player == "b" and not whiteTurn):
            userInput = input("Enter your move: ")

            if userInput == "quit":
                break

            #Check if the move is a castle
            if userInput == "O-O" or userInput == "O-O-O":
                board, isCastle = castle(board, whiteTurn, userInput)

            else:
                try:
                    startRow, startColumn, endRow, endColumn = get_moves_from_user_input(userInput)
                except:
                    print("Invalid move, use standard chess format (ex. e2 e4) or castle (ex. O-O or O-O-O)")
                    continue

                board, ans = make_move(board, whiteTurn, startRow, startColumn, endRow, endColumn)

                if not ans:
                    print("Move was not valid, try again")
                    continue

        else:
            print("TARS is making a move")
            brd, ans, alpha, beta, bestMove = depth_first_search(board, whiteTurn, 0, aiColour, aiColour, True, -1000000, 1000000)

            print_ai_move(board, bestMove[0], bestMove[1], bestMove[2], bestMove[3])
            board, ans = make_move(board, whiteTurn, bestMove[0], bestMove[1], bestMove[2], bestMove[3])

        whiteTurn = not whiteTurn
        print("\n")