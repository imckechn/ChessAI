import globals

# Creates the initial board, its a board contaning a bunch of strings indicating the positions
# Returns the board array
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
    ]   # A     B     C     D     E     F     G     H
    board = [
        ['. ',   '. ',   '. ',   '. ',   '. ',   '. ',   'wN',   'wR'],
        ['. ',   '. ',   'wP',   'wP',   'wB',   'wK',   'wP',   'wP'],
        ['. ',   '. ',   '. ',   '. ',   '. ',   '. ',   '. ',   '. '],
        ['. ',   '. ',   '. ',   '. ',   '. ',   'bP',   '. ',   '. '],
        ['. ',   '. ',   '. ',   '. ',   '. ',   '. ',   '. ',   '. '],
        ['bB',   '. ',   '. ',   '. ',   '. ',   '. ',   '. ',   '. '],
        ['. ',   '. ',   'bP',   'bP',   'bP',   '. ',   '. ',   'bP'],
        ['wR',   '. ',   '. ',   'bQ',   'bK',   'bB',   'bN',   'wB']
    ]   # A     B     C     D     E     F     G     H
    return board


# This prints th current board to the screen
# @params: The board array
def print_board(board):
    for i in range(8):
        print(i+1, '   '.join(board[i]))
    print("  A    B    C    D    E    F    G    H")


# Given an input from the user, this splits it up into the starting column, starting row, ending column, and ending row, if the input is invalid, it returns false
# @params: The input from the user
# @return: The starting row, starting column, the ending row, and then ending column, unless it's castling, in which case it returns "castleRight" or "castleLeft"
def get_moves_from_user_input(input):

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

        return startRow, startColumn, endRow, endColumn
    except:
        return False


# This function takes in the board, starting column, starting row, ending column, and ending row, and then moves the piece from the starting position to the ending position
# @params: The board, the starting row, starting column, ending row, and ending column
# @return: the board with the updates (if they are valid), and a boolean indicating if the move was valid
def make_move(board, whiteTurn, startRow, startColumn, endRow, endColumn):

    #Check if the move makes sense accourding to the turn
    if whiteTurn:
        if board[startRow][startColumn][0] == "b":
            print("Not your piece to move, try again")
            return board, False
    else:
        if board[startRow][startColumn][0] == "w":
            print("Not your piece to move, try again")
            return board, False

    if validate_move(board, startRow, startColumn, endRow, endColumn):

        piece = board[startRow][startColumn]
        board[startRow][startColumn] = ". "

        #Check if it's a promotion
        if piece == "wP" and endRow == 7:
            while(True):

                if globals.AIGAME:
                    newPiece = "queen"
                else:
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

                if globals.AIGAME:
                    newPiece = "queen"
                else:
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

        board[startRow][startColumn] = ". "
        return board, True

    else:
        return board, False


# This checks if the piece at the given position has any avalible moves
# @params: The board, if it's whites turn, the starting row, and starting column
# Returns true if it can move, false if it can't
def can_move(board, whiteTurn, x, y):
    if get_moves(board, whiteTurn, x, y) != []:
        return True
    else:
        return False


#This lists all the moves for the piece at position x and y
# @params: The board, if it's whites turn, the starting row, and starting column
# Returns a list of the moves that can be made
def get_moves(board, whiteTurn, x, y):
    moves = []

    x = int(x)
    y = int(y)

    #White moves
    if whiteTurn:

        #Check if it's a pawn
        if board[x][y] == "wP":

            #If it's in the start row, it can move forward 1 or 2 spaces
            if x == 1:
                if board[x + 1][y] == ". ":
                    moves.append([x + 1, y])

                    if board[x + 1][y] == ". ":
                        moves.append([x + 1, y])

            #Otherwise it can only move forward 1 space
            else:
                if x <= 6 and board[x+1][y] == ". ":
                    moves.append([x+1, y])

            #Check if get_movesit can capture
            if y != 0 and x != 7:
                if 'b' in board[x+1][y-1]:
                    moves.append([x+1, y-1])
            if y != 7 and x != 7:
                if 'b' in board[x+1][y+1]:
                    moves.append([x+1, y+1])

        #Check if it's a rook
        elif board[x][y] == "wR":

            #Check up
            for i in range(x-1, -1, -1):
                if board[i][y] == ". ":
                    moves.append([i, y])
                elif 'b' in board[i][y]:
                    moves.append([i, y])
                    break
                else:
                    break

            #Check down
            for i in range(x+1, 8):
                if board[i][y] == ". ":
                    moves.append([i, y])
                elif 'b' in board[i][y]:
                    moves.append([i, y])
                    break
                else:
                    break

            #Check left
            for i in range(y-1, -1, -1):
                if board[x][i] == ". ":
                    moves.append([x, i])
                elif 'b' in board[x][i]:
                    moves.append([x, i])
                    break
                else:
                    break

            #Check right
            for i in range(y+1, 8):
                if board[x][i] == ". ":
                    moves.append([x, i])
                elif 'b' in board[x][i]:
                    moves.append([x, i])
                    break
                else:
                    break

        #Check if it's a knight
        elif board[x][y] == "wN":

            #Check up
            if x > 1:
                if y > 0:
                    if board[x-2][y-1] == ". " or 'b' in board[x-2][y-1]:
                        moves.append([x-2, y-1])
                if y < 7:
                    if board[x-2][y+1] == ". " or 'b' in board[x-2][y+1]:
                        moves.append([x-2, y+1])

            #Check down
            if x < 6:
                if y > 0:
                    if board[x+2][y-1] == ". " or 'b' in board[x+2][y-1]:
                        moves.append([x+2, y-1])
                if y < 7:
                    if board[x+2][y+1] == ". " or 'b' in board[x+2][y+1]:
                        moves.append([x+2, y+1])

            #Check left
            if y > 1:
                if x > 0:
                    if board[x-1][y-2] == ". " or 'b' in board[x-1][y-2]:
                        moves.append([x-1, y-2])
                if x < 7:
                    if board[x+1][y-2] == ". " or 'b' in board[x+1][y-2]:
                        moves.append([x+1, y-2])

            #Check right
            if y < 6:
                if x > 0:
                    if board[x-1][y+2] == ". " or 'b' in board[x-1][y+2]:
                        moves.append([x-1, y+2])
                if x < 7:
                    if board[x+1][y+2] == ". " or 'b' in board[x+1][y+2]:
                        moves.append([x+1, y+2])

        #Check if it's a bishop
        elif board[x][y] == "wB":

            #Check up and left
            for i in range(1, 8):
                if x-i < 0 or y-i < 0:
                    break
                if board[x-i][y-i] == ". ":
                    moves.append([x-i, y-i])
                elif 'b' in board[x-i][y-i]:
                    moves.append([x-i, y-i])
                    break
                else:
                    break

            #Check up and right
            for i in range(1, 8):
                if x-i < 0 or y+i > 7:
                    break
                if board[x-i][y+i] == ". ":
                    moves.append([x-i, y+i])
                elif 'b' in board[x-i][y+i]:
                    moves.append([x-i, y+i])
                    break
                else:
                    break

            #Check down and left
            for i in range(1, 8):
                if x+i > 7 or y-i < 0:
                    break
                if board[x+i][y-i] == ". ":
                    moves.append([x+i, y-i])
                elif 'b' in board[x+i][y-i]:
                    moves.append([x+i, y-i])
                    break
                else:
                    break

            #Check down and right
            for i in range(1, 8):
                if x+i > 7 or y+i > 7:
                    break
                if board[x+i][y+i] == ". ":
                    moves.append([x+i, y+i])
                elif 'b' in board[x+i][y+i]:
                    moves.append([x+i, y+i])
                    break
                else:
                    break

        #Check if it's a queen
        elif board[x][y] == "wQ":

            #Check up
            for i in range(x-1, -1, -1):
                if board[i][y] == ". ":
                    moves.append([i, y])
                elif 'b' in board[i][y]:
                    moves.append([i, y])
                    break
                else:
                    break

            #Check down
            for i in range(x+1, 8):
                if board[i][y] == ". ":
                    moves.append([i, y])
                elif 'b' in board[i][y]:
                    moves.append([i, y])
                    break
                else:
                    break

            #Check left
            for i in range(y-1, -1, -1):
                if board[x][i] == ". ":
                    moves.append([x, i])
                elif 'b' in board[x][i]:
                    moves.append([x, i])
                    break
                else:
                    break

            #Check right
            for i in range(y+1, 8):
                if board[x][i] == ". ":
                    moves.append([x, i])
                elif 'b' in board[x][i]:
                    moves.append([x, i])
                    break
                else:
                    break

            #Check up and left
            for i in range(1, 8):
                if x-i < 0 or y-i < 0:
                    break
                if board[x-i][y-i] == ". ":
                    moves.append([x-i, y-i])
                elif 'b' in board[x-i][y-i]:
                    moves.append([x-i, y-i])
                    break
                else:
                    break

            #Check up and right
            for i in range(1, 8):
                if x-i < 0 or y+i > 7:
                    break
                if board[x-i][y+i] == ". ":
                    moves.append([x-i, y+i])
                elif 'b' in board[x-i][y+i]:
                    moves.append([x-i, y+i])
                    break
                else:
                    break

            #Check down and left
            for i in range(1, 8):
                if x+i > 7 or y-i < 0:
                    break
                if board[x+i][y-i] == ". ":
                    moves.append([x+i, y-i])
                elif 'b' in board[x+i][y-i]:
                    moves.append([x+i, y-i])
                    break
                else:
                    break

        #Check if it's a king
        elif board[x][y] == "wK":

            #Check up
            if x > 0:
                if board[x-1][y] == ". " or board[x-1][y][0] == 'b':
                    moves.append([x-1, y])

            #Check down
            if x < 7:
                if board[x+1][y] == ". " or board[x+1][y][0] == 'b':
                    moves.append([x+1, y])

            #Check left
            if y > 0:
                if board[x][y-1] == ". " or board[x][y-1][0] == 'b':
                    moves.append([x, y-1])

            #Check right
            if y < 7:
                if board[x][y+1] == ". " or board[x][y+1][0] == 'b':
                    moves.append([x, y+1])

            #Check up and left
            if x > 0 and y > 0:
                if board[x-1][y-1] == ". " or board[x-1][y-1][0] == 'b':
                    moves.append([x-1, y-1])

            #Check up and right
            if x > 0 and y < 7:
                if board[x-1][y+1] == ". " or board[x-1][y+1][0] == 'b':
                    moves.append([x-1, y+1])

            #Check down and left
            if x < 7 and y > 0:
                if board[x+1][y-1] == ". " or board[x+1][y-1][0] == 'b':
                    moves.append([x+1, y-1])

            #Check down and right
            if x < 7 and y < 7:
                if board[x+1][y+1] == ". " or board[x+1][y+1][0] == 'b':
                    moves.append([x+1, y+1])

    #Black moves
    else:

        if board[x][y] == "bP":

            # If it's in the start row
            if x == 6:
                if board[x-1][y] == ". ":
                    moves.append([x-1, y])
                    if board[x-2][y] == ". ":
                        moves.append([x-2, y])

            # If it's not in the start row
            else:
                if y - 1 >= 0 and board[x-1][y] == ". ":
                    moves.append([x-1, y])

            # Check if it can take a piece
            if y > 0 and x > 0:
                if 'w' in board[x-1][y-1]:
                    moves.append([x-1, y-1])
            if y < 7 and x > 0:
                if 'w' in board[x-1][y+1]:
                    moves.append([x-1, y+1])

        #Check if it's a rook
        elif board[x][y] == "bR":

            #Check up
            for i in range(x-1, -1, -1):
                if board[i][y] == ". ":
                    moves.append([i, y])
                elif 'w' in board[i][y]:
                    moves.append([i, y])
                    break
                else:
                    break

            #Check down
            for i in range(x+1, 8):
                if board[i][y] == ". ":
                    moves.append([i, y])
                elif 'w' in board[i][y]:
                    moves.append([i, y])
                    break
                else:
                    break

            #Check left
            for i in range(y-1, -1, -1):
                if board[x][i] == ". ":
                    moves.append([x, i])
                elif 'w' in board[x][i]:
                    moves.append([x, i])
                    break
                else:
                    break

            #Check right
            for i in range(y+1, 8):
                if board[x][i] == ". ":
                    moves.append([x, i])
                elif 'w' in board[x][i]:
                    moves.append([x, i])
                    break
                else:
                    break

        #Check if it's a knight
        elif board[x][y] == "bN":

            #Check up and left
            if x > 1 and y > 0:
                if board[x-2][y-1] == ". " or 'w' in board[x-2][y-1]:
                    moves.append([x-2, y-1])

            #Check up and right
            if x > 1 and y < 7:
                if board[x-2][y+1] == ". " or 'w' in board[x-2][y+1]:
                    moves.append([x-2, y+1])

            #Check down and left
            if x < 6 and y > 0:
                if board[x+2][y-1] == ". " or 'w' in board[x+2][y-1]:
                    moves.append([x+2, y-1])

            #Check down and right
            if x < 6 and y < 7:
                if board[x+2][y+1] == ". " or 'w' in board[x+2][y+1]:
                    moves.append([x+2, y+1])

            #Check left and up
            if x > 0 and y > 1:
                if board[x-1][y-2] == ". " or 'w' in board[x-1][y-2]:
                    moves.append([x-1, y-2])

            #Check left and down
            if x < 7 and y > 1:
                if board[x+1][y-2] == ". " or 'w' in board[x+1][y-2]:
                    moves.append([x+1, y-2])

            #Check right and up
            if x > 0 and y < 6:
                if board[x-1][y+2] == ". " or 'w' in board[x-1][y+2]:
                    moves.append([x-1, y+2])

            #Check right and down
            if x < 7 and y < 6:
                if board[x+1][y+2] == ". " or 'w' in board[x+1][y+2]:
                    moves.append([x+1, y+2])

        #Check if it's a bishop
        elif board[x][y] == "bB":

            #Check up and left
            for i in range(1, 8):
                if x-i >= 0 and y-i >= 0:
                    if board[x-i][y-i] == ". ":
                        moves.append([x-i, y-i])
                    elif 'w' in board[x-i][y-i]:
                        moves.append([x-i, y-i])
                        break
                    else:
                        break

            #Check up and right
            for i in range(1, 8):
                if x-i >= 0 and y+i < 8:
                    if board[x-i][y+i] == ". ":
                        moves.append([x-i, y+i])
                    elif 'w' in board[x-i][y+i]:
                        moves.append([x-i, y+i])
                        break
                    else:
                        break

            #Check down and left
            for i in range(1, 8):
                if x+i < 8 and y-i >= 0:
                    if board[x+i][y-i] == ". ":
                        moves.append([x+i, y-i])
                    elif 'w' in board[x+i][y-i]:
                        moves.append([x+i, y-i])
                        break
                    else:
                        break

            #Check down and right
            for i in range(1, 8):
                if x+i < 8 and y+i < 8:
                    if board[x+i][y+i] == ". ":
                        moves.append([x+i, y+i])
                    elif 'w' in board[x+i][y+i]:
                        moves.append([x+i, y+i])
                        break
                    else:
                        break

        #Check if it's a queen
        elif board[x][y] == "bQ":

            #Check up
            for i in range(x-1, -1, -1):
                if board[i][y] == ". ":
                    moves.append([i, y])
                elif 'w' in board[i][y]:
                    moves.append([i, y])
                    break
                else:
                    break

            #Check down
            for i in range(x+1, 8):
                if board[i][y] == ". ":
                    moves.append([i, y])
                elif 'w' in board[i][y]:
                    moves.append([i, y])
                    break
                else:
                    break

            #Check left
            for i in range(y-1, -1, -1):
                if board[x][i] == ". ":
                    moves.append([x, i])
                elif 'w' in board[x][i]:
                    moves.append([x, i])
                    break
                else:
                    break

            #Check right
            for i in range(y+1, 8):
                if board[x][i] == ". ":
                    moves.append([x, i])
                elif 'w' in board[x][i]:
                    moves.append([x, i])
                    break
                else:
                    break

            #Check up and left
            for i in range(1, 8):
                if x-i >= 0 and y-i >= 0:
                    if board[x-i][y-i] == ". ":
                        moves.append([x-i, y-i])
                    elif 'w' in board[x-i][y-i]:
                        moves.append([x-i, y-i])
                        break
                    else:
                        break

            #Check up and right
            for i in range(1, 8):
                if x-i >= 0 and y+i < 8:
                    if board[x-i][y+i] == ". ":
                        moves.append([x-i, y+i])
                    elif 'w' in board[x-i][y+i]:
                        moves.append([x-i, y+i])
                        break
                    else:
                        break

            #Check down and left
            for i in range(1, 8):
                if x+i < 8 and y-i >= 0:
                    if board[x+i][y-i] == ". ":
                        moves.append([x+i, y-i])
                    elif 'w' in board[x+i][y-i]:
                        moves.append([x+i, y-i])
                        break
                    else:
                        break

            #Check down and right
            for i in range(1, 8):
                if x+i < 8 and y+i < 8:
                    if board[x+i][y+i] == ". ":
                        moves.append([x+i, y+i])
                    elif 'w' in board[x+i][y+i]:
                        moves.append([x+i, y+i])
                        break
                    else:
                        break

        #Check if it's a king
        elif board[x][y] == "bK":

            #Check up
            if x-1 >= 0:
                if board[x-1][y] == ". " or 'w' in board[x-1][y]:
                    moves.append([x-1, y])

            #Check down
            if x+1 < 8:
                if board[x+1][y] == ". " or 'w' in board[x+1][y]:
                    moves.append([x+1, y])

            #Check left
            if y-1 >= 0:
                if board[x][y-1] == ". " or 'w' in board[x][y-1]:
                    moves.append([x, y-1])

            #Check right
            if y+1 < 8:
                if board[x][y+1] == ". " or 'w' in board[x][y+1]:
                    moves.append([x, y+1])

            #Check up and left
            if x-1 >= 0 and y-1 >= 0:
                if board[x-1][y-1] == ". " or 'w' in board[x-1][y-1]:
                    moves.append([x-1, y-1])

            #Check up and right
            if x-1 >= 0 and y+1 < 8:
                if board[x-1][y+1] == ". " or 'w' in board[x-1][y+1]:
                    moves.append([x-1, y+1])

            #Check down and left
            if x+1 < 8 and y-1 >= 0:
                if board[x+1][y-1] == ". " or 'w' in board[x+1][y-1]:
                    moves.append([x+1, y-1])

            #Check down and right
            if x+1 < 8 and y+1 < 8:
                if board[x+1][y+1] == ". " or 'w' in board[x+1][y+1]:
                    moves.append([x+1, y+1])

    return moves


# This function checks if the move is valid
# @params: the baord, the start row, start column, end row, end column. Rows and columns need to start at zero
# Returns: True if the move is valid, False otherwise
def validate_move(board, startRow, startColumn, endRow, endColumn):
    answer = False

    if board[startRow][startColumn] == ". ":
        return False

    # Check that the end position is either open position or a capture
    if 'w' in board[startRow][startColumn]:
        if 'b' not in board[endRow][endColumn] and board[endRow][endColumn] != ". ":
            return False

    elif 'b' in board[startRow][startColumn]:
        if 'w' not in board[endRow][endColumn] and board[endRow][endColumn] != ". ":
            return False

    # Conditions for a white pawn
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

        return answer

    # Conditions for a black pawn
    elif board[startRow][startColumn] == "bP":
        if startRow == 6:
            if endRow == 5 and board[endRow][endColumn] == ". ":
                answer = True
            elif endRow == 4 and board[endRow][endColumn] == ". " and board[5][startColumn] == ". ":
                answer = True

        if startRow != 6:
            if endRow == startRow - 1 and board[endRow][endColumn] == ". ":
                answer = True

        if endRow == startRow - 1 and (endColumn == startColumn + 1 or endColumn == startColumn - 1):
            if 'w' in board[endRow][endColumn]:
                answer = True

        return answer

    # Conditions for a rook
    elif board[startRow][startColumn] == "wR" or board[startRow][startColumn] == "bR":
        #If the rook is moving in the same row
        if startRow == endRow:
            if startColumn < endColumn:
                for i in range(startColumn + 1, endColumn -1):
                    if board[startRow][i] != ". ":
                        return False
            elif startColumn > endColumn:
                for i in range(startColumn - 1, endColumn, -1):
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
    elif board[startRow][startColumn] == "wN" or board[startRow][startColumn] == "bN":
        if abs(startRow - endRow) == 2 and abs(startColumn - endColumn) == 1:
            return True
        elif abs(startRow - endRow) == 1 and abs(startColumn - endColumn) == 2:
            return True

    # Conditions for a bishop
    elif board[startRow][startColumn] == 'wB' or board[startRow][startColumn] == 'bB':
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
    elif board[startRow][startColumn] == 'wQ' or board[startRow][startColumn] == 'bQ':
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
    elif board[startRow][startColumn] == 'wK' or board[startRow][startColumn] == 'bK':

        if abs(startRow - endRow) <= 1 and abs(startColumn - endColumn) <= 1:
            return True

    #If they're trying to move a empty space for some reason
    else:
        print("Error, you're trying to move an empty space")
        return False


# Check if the king is in check
# @param the board, the king, which can be either b w bK or wK
# returns true if the king is in check, false otherwise
def check(board, king):
    kingRow = -1
    kingColumn = -1

    if king == "w" or king == "wK":
        king = "wK"
    else:
        king = "bK"

    #find the king
    for i in range(8):
        for j in range(8):
            if board[i][j] == king:
                kingRow = i
                kingColumn = j
                break

        if kingRow != -1:
            break

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


# Gets all the pieces for a given colour
# Params: board is the game board, colour is a string of just 'w' or 'b'
# Returns a list containing all the piece positions for the given colour
def get_pieces(board, colour):
    pieces = []

    colour = colour.lower()

    for i in range(8): # For each row
        for j in range(8): # For each column
            if board[i][j][0] == colour:
                pieces.append([board[i][j], i, j])

    return pieces


# If the king is in check, this checks if there is any pieces that can block the check
# @Params: The board, whiteTurn, and the king which can be either w k b or bk
# Returns true if there is a piece that can block the check, false otherwise
def can_check_be_blocked(board, whiteTurn, king):

    pieces = get_pieces(board, king[0])

    for piece in pieces:
        moves = get_moves(board, whiteTurn, piece[1], piece[2])

        for move in moves:
            newBoard, ans = make_move(board, whiteTurn, piece[1], piece[2], move[0], move[1])

            if not check(newBoard, king):
                return True

    return False


# Checks for checkmate
# @params: the board, whiteTurn and king which can be either w k b or bk
# Returns true if the king is in checkmate, false otherwise
def checkmate(board, king):

    if king == "w":
        king = "wK"
        whiteTurn = True
    else:
        king = "bK"
        whiteTurn = False

    #check if the king is in check
    isInCheck = check(board, king)

    kingRow = -1
    kingColumn = -1

    for i in range(8):
        for j in range(8):
            if board[i][j] == king:
                kingRow = i
                kingColumn = j
                break
        if kingRow != -1:
            break

    if isInCheck:
        #Get all the moves for the king
        moves = get_moves(board, whiteTurn, kingRow, kingColumn)

        #see if there is a move that the king can perform to get out of check
        for move in moves:
            newBoard, ans = make_move(board, whiteTurn, kingRow, kingColumn, move[0], move[1])

            if not check(newBoard, king):
                return False

        #See if another piece can block the check
        ans = can_check_be_blocked(board, whiteTurn, king)

        return not ans
    return False


# Check if the requested move is a castle and if so, make the move
# Params: The board, whiteTurn, and the user input
# Returns: The board, and true or false depending on if the move was valid
def castle(board, whiteTurn, userInput):

    newBoard = board
    answer = False
    isInCheck = None

    if whiteTurn:
        isInCheck = check(newBoard, "wK")
    else:
        isInCheck = check(newBoard, "bK")

    if isInCheck:
        return newBoard, False

    if userInput == "O-O":
        if whiteTurn:
            if newBoard[7][4] == "wK" and newBoard[7][7] == "wR" and newBoard[7][5] == ". " and newBoard[7][6] == ". ":
                newBoard[7][4] = ". "
                newBoard[7][5] = "wK"
                newBoard[7][6] = "wR"
                newBoard[7][7] = ". "
                answer = True

        else:
            if newBoard[0][4] == "bK" and newBoard[0][7] == "bR" and newBoard[0][5] == ". " and newBoard[0][6] == ". ":
                newBoard[0][4] = ". "
                newBoard[0][5] = "bK"
                newBoard[0][6] = "bR"
                newBoard[0][7] = ". "
                answer = True

    elif userInput == "O-O-O":
        if whiteTurn:
            if newBoard[7][4] == "wK" and newBoard[7][0] == "wR" and newBoard[7][1] == ". " and newBoard[7][2] == ". " and newBoard[7][3] == ". ":
                newBoard[7][4] = ". "
                newBoard[7][3] = "wK"
                newBoard[7][2] = "wR"
                newBoard[7][0] = ". "
                answer = True

        else:
            if newBoard[0][4] == "bK" and newBoard[0][0] == "bR" and newBoard[0][1] == ". " and newBoard[0][2] == ". " and newBoard[0][3] == ". ":
                newBoard[0][4] = ". "
                newBoard[0][3] = "bK"
                newBoard[0][2] = "bR"
                newBoard[0][0] = ". "
                answer = True

    if answer:
        if whiteTurn:
            if check(newBoard, "wK"):
                return board, False
            else:
                return newBoard, answer

        else:
            if check(newBoard, "bK"):
                return board, False
            else:
                return newBoard, answer

    return board, answer


# Checks if the game is in a stalemate
# A stalemate occurs when the king is not in check, but the king cannot move to a square that is not under attack
# and there is no pieces on the board that can move
# @params: the board, whiteTurn
# Returns true if the game is in a stalemate, false otherwise
def check_for_stalemate(board, whiteTurn):
    #Check if the black king can move, and if so is it a move that doesnt result in check
    if whiteTurn:
        for i in range(8):
            for j in range(8):
                #Find the white king
                if board[i][j] == "wK":
                    #Check if the king can move to any of the 8 squares around it
                    for k in range(-1, 2):
                        for l in range(-1, 2):

                            #Check that the position being checked is in bounds
                            if i + k >= 0 and i + k < 8 and j + l >= 0 and j + l < 8:

                                #Check that the square being checked is open
                                if board[i + k][j + l] == ". ":

                                    #Check if the move results in check
                                    board[i + k][j + l] = "wK"
                                    board[i][j] = ". "

                                    if not check(board, "wK"):
                                        board[i + k][j + l] = ". "
                                        board[i][j] = "wK"
                                        return False
                                    else:
                                        board[i + k][j + l] = ". "
                                        board[i][j] = "wK"

                    #Check if any other pieces can move
                    for k in range(8):
                        for l in range(8):
                            if 'w' in board[k][l] and 'wK' != board[k][l]:
                                if can_move(board, whiteTurn, k, l):
                                    return False
                    return True

    else:
        for i in range(8):
            for j in range(8):
                #Find the black king
                if board[i][j] == "bK":
                    #Check if the king can move to any of the 8 squares around it
                    for k in range(-1, 2):
                        for l in range(-1, 2):

                            #Check that the position being checked is in bounds
                            if i + k >= 0 and i + k < 8 and j + l >= 0 and j + l < 8:

                                #Check that the square being checked is open
                                if board[i + k][j + l] == ". ":

                                    #Check if the move results in check
                                    board[i + k][j + l] = "bK"
                                    board[i][j] = ". "

                                    if not check(board, "bK"):
                                        board[i + k][j + l] = ". "
                                        board[i][j] = "bK"
                                        return False
                                    else:
                                        board[i + k][j + l] = ". "
                                        board[i][j] = "bK"

                    #Check if any other pieces can move
                    for k in range(8):
                        for l in range(8):
                            if 'b' in board[k][l] and 'bK' != board[k][l]:
                                if can_move(board, whiteTurn, k, l):
                                    return False

                    return True

# Checks if the game is over
# A game is over when a king is in checkmate or a stalemate occurs
# @params: the board
# Returns true if the game is over, false otherwise
def isGameOver(board):
    whiteQueenFound = False
    blackQueenFound = False

    #Check if the game is in a stalemate
    for i in range(8):
        for j in range(8):
            if board[i][j] == "wK":
                whiteQueenFound = True
            elif board[i][j] == "bK":
                blackQueenFound = True

    if not whiteQueenFound:
        print("Black wins by checkmate")
        return True
    elif not blackQueenFound:
        print("White wins by checkmate")
        return True

    return False