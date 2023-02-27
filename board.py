
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

        #If it's in the start row, it can move forward 1 or 2 spaces
        if startRow == 1:
            if endRow == 2 and board[endRow][endColumn] == ". ":
                return True
            elif endRow == 3 and board[endRow][endColumn] == ". " and board[2][startColumn] == ". ":
                return True

        # If it's not in the start row, it can only move forward 1 space
        elif startRow != 1:
            if endRow == startRow + 1 and board[endRow][endColumn] == ". ":
                return True

        # If there is a piece diagonal to it fowards it can take the piece
        if endRow == startRow + 1 and (endColumn == startColumn + 1 or endColumn == startColumn - 1):
            if 'b' in board[endRow][endColumn]:
                return True

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


userInput = None
board = create_board()
while userInput != "quit":
    print_board(board)
    userInput = input("Enter your move: ")

    if userInput == "quit":
        break

    startColumn, startRow, endColumn, endRow = get_moves(userInput)

    ans = makeMove(board, startColumn, startRow, endColumn, endRow)

    if not ans:
        print("Invalid move!")