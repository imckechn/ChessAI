from board import *
from TARS import *
import globals

def print_ai_move(startRow, startColumn, endRow, endColumn):
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

    print("TARS moved from " + str(startColumn) + str(startRow) + " to " + str(endColumn) + str(endRow))


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
    globals.aiGame = True
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
            print("TARS is making a move")
            board, ans, alpha, beta, bestMove = depth_first_search(board, whiteTurn, 0, aiColour, aiColour, True, -1000000, 1000000)

            print_ai_move(bestMove[0], bestMove[1], bestMove[2], bestMove[3])
            board, ans = make_move(board, whiteTurn, bestMove[0], bestMove[1], bestMove[2], bestMove[3])

        whiteTurn = not whiteTurn
        print("\n")
