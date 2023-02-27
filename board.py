
# Global Variables
whiteTurn = True


# Creates the initial board, its a board contaning a bunch of strings indicating the positions
def create_board():
    board = [
        ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'], #1
        ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'], #2
        ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '], #3
        ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '], #4
        ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '], #5
        ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '], #6
        ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'], #7
        ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR']  #8
    ]    #A     B     C     D     E     F     G     H

    return board


# This prints th current board to the screen
def print_board(board):
    for i in range(8):
        print(i+1, '   '.join(board[i]))

    print("  A    B    C    D    E    F    G    H")


# Given an input from the user, this splits it up into the starting column, starting row, ending column, and ending row, if the input is invalid, it returns false
def get_moves(input):
    if input ==  "0-0":
        return "castleRight"
    elif input == "0-0-0":
        return "castleLeft"

    try:
        positions = input.split(" ")
        start = positions[0]
        end = positions[1]

        startColumn = start[0].upper()
        startRow = start[1]

        endColumn = end[0].upper()
        endRow = end[1]

        return startColumn, startRow, endColumn, endRow
    except:
        return False


# This function takes in the board, starting column, starting row, ending column, and ending row, and then moves the piece from the starting position to the ending position
def makeMove(board, startColumn, startRow, endColumn, endRow):
    if startColumn == "A":
        startColumn = 0
    elif startColumn == "B":
        startColumn = 1
    elif startColumn == "C":
        startColumn = 2
    elif startColumn == "D":
        startColumn = 3
    elif startColumn == "E":
        startColumn = 4
    elif startColumn == "F":
        startColumn = 5
    elif startColumn == "G":
        startColumn = 6
    elif startColumn == "H":
        startColumn = 7

    if endColumn == "A":
        endColumn = 0
    elif endColumn == "B":
        endColumn = 1
    elif endColumn == "C":
        endColumn = 2
    elif endColumn == "D":
        endColumn = 3
    elif endColumn == "E":
        endColumn = 4
    elif endColumn == "F":
        endColumn = 5
    elif endColumn == "G":
        endColumn = 6
    elif endColumn == "H":
        endColumn = 7

    startRow = int(startRow) - 1
    endRow = int(endRow) - 1

    if validateMove(board, startColumn, startRow, endColumn, endRow):

        piece = board[startRow][startColumn]
        board[startRow][startColumn] = ". "

        #Check if it's a promotion
        if piece == "wP" and endRow == 7:
             while(True):
                newPiece = input("What piece would you like to promote to (Queen, Rook, Bishop, Knight)? ").lower()

                if newPiece == "queen":
                    board[endRow][endColumn] = "wQ"
                    break
                elif newPiece == "rook":
                    board[endRow][endColumn] = "wR"
                    break
                elif newPiece == "bishop":
                    board[endRow][endColumn] = "wB"
                    break
                elif newPiece == "knight":
                    board[endRow][endColumn] = "wN"
                    break
                else:
                    print("Invalid Piece")
        elif piece == "bP" and endRow == 0:
             while(True):
                newPiece = input("What piece would you like to promote to (Queen, Rook, Bishop, Knight)? ").lower()

                if newPiece == "queen":
                    board[endRow][endColumn] = "bQ"
                    break
                elif newPiece == "rook":
                    board[endRow][endColumn] = "bR"
                    break
                elif newPiece == "bishop":
                    board[endRow][endColumn] = "bB"
                    break
                elif newPiece == "knight":
                    board[endRow][endColumn] = "bN"
                    break
                else:
                    print("Invalid Piece")
        else:
            board[endRow][endColumn] = piece

        return board

    else:
        return False



def validateMove(board, startColumn, startRow, endColumn, endRow):

    if board[startRow][startColumn] == ". ":
        return False

    # Check that the end position is either open position or a capture
    if 'w' in board[startRow][startColumn]:
        if 'b' not in board[endRow][endColumn] and board[endRow][endColumn] != ". ":
            return False
    elif 'b' in board[startRow][startColumn]:
        if 'w' not in board[endRow][endColumn] and board[endRow][endColumn] != ". ":
            return False

    #Conditions for a pawn
    if board[startRow][startColumn] == "wP":
        answer = False

        #If it's in the start row, it can move forward 1 or 2 spaces
        if startRow == 1:
            if endRow == 2 and board[endRow][endColumn] == ". ":
                answer = True
            elif endRow == 3 and board[endRow][endColumn] == ". " and board[2][startColumn] == ". ":
                answer = True

        # If it's not in the start row, it can only move forward 1 space
        elif startRow != 1:
            if endRow == startRow + 1 and board[endRow][endColumn] == ". ":
                answer = True

        # If there is a piece diagonal to it fowards it can take the piece
        if endRow == startRow + 1 and (endColumn == startColumn + 1 or endColumn == startColumn - 1):
            if 'b' in board[endRow][endColumn]:
                answer = True

        # Handle Promotion
        if answer == True and endRow == 7:
            while(True):
                newPiece = input("What piece would you like to promote to (Queen, Rook, Bishop, Knight)? ").lower()

                if newPiece == "queen":
                    board[endRow][endColumn] = "wQ"
                    break
                elif newPiece == "rook":
                    board[endRow][endColumn] = "wR"
                    break
                elif newPiece == "bishop":
                    board[endRow][endColumn] = "wB"
                    break
                elif newPiece == "knight":
                    board[endRow][endColumn] = "wN"
                    break
                else:
                    print("Invalid Piece")

        return answer


    elif board[startRow][startColumn] == "bP":
        if startRow == 6:
            if endRow == 5 and board[endRow][endColumn] == ". ":
                return True
            elif endRow == 4 and board[endRow][endColumn] == ". " and board[5][startColumn] == ". ":
                return True

        if startRow != 6:
            if endRow == startRow - 1 and board[endRow][endColumn] == ". ":
                return True

        if endRow == startRow - 1 and (endColumn == startColumn + 1 or endColumn == startColumn - 1):
            if 'w' in board[endRow][endColumn]:
                return True

    # Conditions for a rook
    elif board[startRow][startColumn] == "wR" or board[startRow][startColumn] == "bR":

        #If the rook is moving in the same row
        if startRow == endRow:
            if startColumn < endColumn:
                for i in range(startColumn + 1, endColumn -1):
                    if board[startRow][i] != ". ":
                        return False
            elif startColumn > endColumn:
                for i in range(startColumn - 1, endColumn -1, -1):
                    if board[startRow][i] != ". ":
                        return False

            return True

        elif startColumn == endColumn:
            if startRow < endRow:
                for i in range(startRow + 1, endRow):
                    if board[i][startColumn] != ". ":
                        return False
            elif startRow > endRow:
                for i in range(startRow - 1, endRow, -1):
                    if board[i][startColumn] != ". ":
                        return False
            return True

    # Conditions for a knight
    if board[startRow][startColumn] == "wN" or board[startRow][startColumn] == "bN":
        if abs(startRow - endRow) == 2 and abs(startColumn - endColumn) == 1:
            return True
        elif abs(startRow - endRow) == 1 and abs(startColumn - endColumn) == 2:
            return True

    # Conditions for a bishop
    if board[startRow][startColumn] == 'wB' or board[startRow][startColumn] == 'bB':
        if abs(startRow - endRow) == abs(startColumn - endColumn): #Check that it's on a diagonal
            if startRow < endRow and startColumn < endColumn:
                for i in range(1, abs(startRow - endRow)):
                    if board[startRow + i][startColumn + i] != ". ":
                        return False
            elif startRow < endRow and startColumn > endColumn:
                for i in range(1, abs(startRow - endRow)):
                    if board[startRow + i][startColumn - i] != ". ":
                        return False
            elif startRow > endRow and startColumn < endColumn:
                for i in range(1, abs(startRow - endRow)):
                    if board[startRow - i][startColumn + i] != ". ":
                        return False
            elif startRow > endRow and startColumn > endColumn:
                for i in range(1, abs(startRow - endRow)):
                    if board[startRow - i][startColumn - i] != ". ":
                        return False
            return True

    # Conditions for a queen
    if board[startRow][startColumn] == 'wQ' or board[startRow][startColumn] == 'bQ':
        if startRow == endRow:
            if startColumn < endColumn:
                for i in range(startColumn + 1, endColumn -1):
                    if board[startRow][i] != ". ":
                        return False
            elif startColumn > endColumn:
                for i in range(startColumn - 1, endColumn -1, -1):
                    if board[startRow][i] != ". ":
                        return False
            return True

        elif startColumn == endColumn:
            if startRow < endRow:
                for i in range(startRow + 1, endRow):
                    if board[i][startColumn] != ". ":
                        return False
            elif startRow > endRow:
                for i in range(startRow - 1, endRow, -1):
                    if board[i][startColumn] != ". ":
                        return False
            return True

        elif abs(startRow - endRow) == abs(startColumn - endColumn):
            if startRow < endRow and startColumn < endColumn:
                for i in range(1, abs(startRow - endRow)):
                    if board[startRow + i][startColumn + i] != ". ":
                        return False
            elif startRow < endRow and startColumn > endColumn:
                for i in range(1, abs(startRow - endRow)):
                    if board[startRow + i][startColumn - i] != ". ":
                        return False
            elif startRow > endRow and startColumn < endColumn:
                for i in range(1, abs(startRow - endRow)):
                    if board[startRow - i][startColumn + i] != ". ":
                        return False
            elif startRow > endRow and startColumn > endColumn:
                for i in range(1, abs(startRow - endRow)):
                    if board[startRow - i][startColumn - i] != ". ":
                        return False
            return True

    # Conditions for a king
    if board[startRow][startColumn] == 'wK' or board[startRow][startColumn] == 'bK':
        if abs(startRow - endRow) <= 1 and abs(startColumn - endColumn) <= 1:
            return True

    #If they're trying to move a empty space for some reason
    return False


# Check if the king is in check
def check(board, king):
    kingRow = None
    kingColumn = None

    #find the king
    for i in range(8):
        for j in range(8):
            if board[i][j] == king:
                kingRow = i
                kingColumn = j

    #Check if the king is in check by a pawn
    if king == "wK":
        if kingRow != 0 and kingColumn != 0:
            if board[kingRow - 1][kingColumn - 1] == "bP":
                return True
        if kingRow != 0 and kingColumn != 7:
            if board[kingRow - 1][kingColumn + 1] == "bP":
                return True
    else:
        if kingRow != 7 and kingColumn != 0:
            if board[kingRow + 1][kingColumn - 1] == "wP":
                return True
        if kingRow != 7 and kingColumn != 7:
            if board[kingRow + 1][kingColumn + 1] == "wP":
                return True

    #Check if the king is in check by a knight
    if king == "wK":
        if kingRow + 1 < 8 and kingColumn + 2 < 8:
            if board[kingRow + 1][kingColumn + 2] == "bN":
                return True
        if kingRow + 1 < 8 and kingColumn - 2 >= 0:
            if board[kingRow + 1][kingColumn - 2] == "bN":
                return True
        if kingRow - 1 >= 0 and kingColumn + 2 < 8:
            if board[kingRow - 1][kingColumn + 2] == "bN":
                return True
        if kingRow - 1 >= 0 and kingColumn - 2 >= 0:
            if board[kingRow - 1][kingColumn - 2] == "bN":
                return True
        if kingRow + 2 < 8 and kingColumn + 1 < 8:
            if board[kingRow + 2][kingColumn + 1] == "bN":
                return True
        if kingRow + 2 < 8 and kingColumn - 1 >= 0:
            if board[kingRow + 2][kingColumn - 1] == "bN":
                return True
        if kingRow - 2 >= 0 and kingColumn + 1 < 8:
            if board[kingRow - 2][kingColumn + 1] == "bN":
                return True
        if kingRow - 2 >= 0 and kingColumn - 1 >= 0:
            if board[kingRow - 2][kingColumn - 1] == "bN":
                return True
    else:
        if kingRow + 1 < 8 and kingColumn + 2 < 8:
            if board[kingRow + 1][kingColumn + 2] == "wN":
                return True
        if kingRow + 1 < 8 and kingColumn - 2 >= 0:
            if board[kingRow + 1][kingColumn - 2] == "wN":
                return True
        if kingRow - 1 >= 0 and kingColumn + 2 < 8:
            if board[kingRow - 1][kingColumn + 2] == "wN":
                return True
        if kingRow - 1 >= 0 and kingColumn - 2 >= 0:
            if board[kingRow - 1][kingColumn - 2] == "wN":
                return True
        if kingRow + 2 < 8 and kingColumn + 1 < 8:
            if board[kingRow + 2][kingColumn + 1] == "wN":
                return True
        if kingRow + 2 < 8 and kingColumn - 1 >= 0:
            if board[kingRow + 2][kingColumn - 1] == "wN":
                return True
        if kingRow - 2 >= 0 and kingColumn + 1 < 8:
            if board[kingRow - 2][kingColumn + 1] == "wN":
                return True
        if kingRow - 2 >= 0 and kingColumn - 1 >= 0:
            if board[kingRow - 2][kingColumn - 1] == "wN":
                return True

    #Check if the king is in check by a bishop or queen
    if king == "wK":
        for i in range(1, 8):
            if kingRow + i < 8 and kingColumn + i < 8:
                if board[kingRow + i][kingColumn + i] == "bB" or board[kingRow + i][kingColumn + i] == "bQ":
                    return True
                if board[kingRow + i][kingColumn + i] != ". ":
                    break
            else:
                break

        for i in range(1, 8):
            if kingRow + i < 8 and kingColumn - i >= 0:
                if board[kingRow + i][kingColumn - i] == "bB" or board[kingRow + i][kingColumn - i] == "bQ":
                    return True
                if board[kingRow + i][kingColumn - i] != ". ":
                    break
            else:
                break

        for i in range(1, 8):
            if kingRow - i >= 0 and kingColumn + i < 8:
                if board[kingRow - i][kingColumn + i] == "bB" or board[kingRow - i][kingColumn + i] == "bQ":
                    return True
                if board[kingRow - i][kingColumn + i] != ". ":
                    break
            else:
                break

        for i in range(1, 8):
            if kingRow - i >= 0 and kingColumn - i >= 0:
                if board[kingRow - i][kingColumn - i] == "bB" or board[kingRow - i][kingColumn - i] == "bQ":
                    return True
                if board[kingRow - i][kingColumn - i] != ". ":
                    break
            else:
                break
    else:
        for i in range(1, 8):
            if kingRow + i < 8 and kingColumn + i < 8:
                if board[kingRow + i][kingColumn + i] == "wB" or board[kingRow + i][kingColumn + i] == "wQ":
                    return True
                if board[kingRow + i][kingColumn + i] != ". ":
                    break
            else:
                break

        for i in range(1, 8):
            if kingRow + i < 8 and kingColumn - i >= 0:
                if board[kingRow + i][kingColumn - i] == "wB" or board[kingRow + i][kingColumn - i] == "wQ":
                    return True
                if board[kingRow + i][kingColumn - i] != ". ":
                    break
            else:
                break

        for i in range(1, 8):
            if kingRow - i >= 0 and kingColumn + i < 8:
                if board[kingRow - i][kingColumn + i] == "wB" or board[kingRow - i][kingColumn + i] == "wQ":
                    return True
                if board[kingRow - i][kingColumn + i] != ". ":
                    break
            else:
                break

        for i in range(1, 8):
            if kingRow - i >= 0 and kingColumn - i >= 0:
                if board[kingRow - i][kingColumn - i] == "wB" or board[kingRow - i][kingColumn - i] == "wQ":
                    return True
                if board[kingRow - i][kingColumn - i] != ". ":
                    break
            else:
                break

    #Check if the king is in check by a rook or queen
    if king == "wK":
        for i in range(1, 8):
            if kingRow + i < 8:
                if board[kingRow + i][kingColumn] == "bR" or board[kingRow + i][kingColumn] == "bQ":
                    return True
                if board[kingRow + i][kingColumn] != ". ":
                    break
            else:
                break

        for i in range(1, 8):
            if kingRow - i >= 0:
                if board[kingRow - i][kingColumn] == "bR" or board[kingRow - i][kingColumn] == "bQ":
                    return True
                if board[kingRow - i][kingColumn] != ". ":
                    break
            else:
                break

        for i in range(1, 8):
            if kingColumn + i < 8:
                if board[kingRow][kingColumn + i] == "bR" or board[kingRow][kingColumn + i] == "bQ":
                    return True
                if board[kingRow][kingColumn + i] != ". ":
                    break
            else:
                break

        for i in range(1, 8):
            if kingColumn - i >= 0:
                if board[kingRow][kingColumn - i] == "bR" or board[kingRow][kingColumn - i] == "bQ":
                    return True
                if board[kingRow][kingColumn - i] != ". ":
                    break
            else:
                break
    else:
        for i in range(1, 8):
            if kingRow + i < 8:
                if board[kingRow + i][kingColumn] == "wR" or board[kingRow + i][kingColumn] == "wQ":
                    return True
                if board[kingRow + i][kingColumn] != ". ":
                    break
            else:
                break

        for i in range(1, 8):
            if kingRow - i >= 0:
                if board[kingRow - i][kingColumn] == "wR" or board[kingRow - i][kingColumn] == "wQ":
                    return True
                if board[kingRow - i][kingColumn] != ". ":
                    break
            else:
                break

        for i in range(1, 8):
            if kingColumn + i < 8:
                if board[kingRow][kingColumn + i] == "wR" or board[kingRow][kingColumn + i] == "wQ":
                    return True
                if board[kingRow][kingColumn + i] != ". ":
                    break
            else:
                break

        for i in range(1, 8):
            if kingColumn - i >= 0:
                if board[kingRow][kingColumn - i] == "wR" or board[kingRow][kingColumn - i] == "wQ":
                    return True
                if board[kingRow][kingColumn - i] != ". ":
                    break
            else:
                break

    return False



# Check if the requested move is a castle and if so, make the move
def castle(board, userInput):

    if whiteTurn:
        isInCheck = check(board, "wK")


    if userInput == "O-O":
        if whiteTurn:
            if board[7][4] == "wK" and board[7][7] == "wR" and board[7][5] == ". " and board[7][6] == ". ":
                board[7][4] = ". "
                board[7][5] = "wK"
                board[7][6] = "wR"
                board[7][7] = ". "
                return board, True

            else:
                print("Invalid move!")

        else:
            if board[0][4] == "bK" and board[0][7] == "bR" and board[0][5] == ". " and board[0][6] == ". ":
                board[0][4] = ". "
                board[0][5] = "bK"
                board[0][6] = "bR"
                board[0][7] = ". "
                return board, True

            else:
                print("Invalid move!")

    elif userInput == "O-O-O":
        if whiteTurn:
            if board[7][4] == "wK" and board[7][0] == "wR" and board[7][1] == ". " and board[7][2] == ". " and board[7][3] == ". ":
                board[7][4] = ". "
                board[7][3] = "wK"
                board[7][2] = "wR"
                board[7][0] = ". "
                return board, True

            else:
                print("Invalid move!")

        else:
            if board[0][4] == "bK" and board[0][0] == "bR" and board[0][1] == ". " and board[0][2] == ". " and board[0][3] == ". ":
                board[0][4] = ". "
                board[0][3] = "bK"
                board[0][2] = "bR"
                board[0][0] = ". "
                return board, True

            else:
                print("Invalid move!")

    return board, False


userInput = None
board = create_board()
while userInput != "quit":
    print_board(board)
    userInput = input("Enter your move: ")

    if userInput == "quit":
        break

    #Check if the move is a castle
    if userInput == "O-O" or userInput == "O-O-O":
        board, isCastle = castle(board, userInput)

    else:
        startColumn, startRow, endColumn, endRow = get_moves(userInput)
        ans = makeMove(board, startColumn, startRow, endColumn, endRow)

    if not ans:
        print("Invalid move!")