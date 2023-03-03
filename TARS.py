from board import *
import copy

depth_floor = 3
counter = 0
moveCount = 0

# Gets the points given a boardState and a colour (can maximize the player or AI's points)
# Params: the board, the ai colour (w or b), the current colour (w or b)
# Returns: the points
def get_points(board, aiColour, curColour):

    playerColour = "w" if aiColour == "b" else "b"

    aiPieces = get_pieces(board, curColour)
    playerPieces = get_pieces(board, playerColour)

    aiPoints = 0
    aiKing = False
    playerKing = False

    #Maximize the points
    if aiColour == curColour:

        for piece in aiPieces:
            if piece[0][1] == "R":
                aiPoints += 4

            elif piece[0][1] == "N":
                aiPoints += 2

            elif piece[0][1] == "B":
                aiPoints += 3

            elif piece[0][1] == "Q":
                aiPoints += 5

            elif piece[0][1] == "P":
                aiPoints += 1

            elif piece[0][1] == "K":
                aiKing = True

        for piece in playerPieces:
            if piece[0][1] == "R":
                aiPoints -= 4

            elif piece[0][1] == "N":
                aiPoints -= 2

            elif piece[0][1] == "B":
                aiPoints -= 3

            elif piece[0][1] == "Q":
                aiPoints -= 5

            elif piece[0][1] == "P":
                aiPoints -= 1

            elif piece[0][1] == "K":
                playerKing = True

        if not aiKing:
            aiPoints -= 10000000000

        if not playerKing:
            aiPoints += 10000000000

        return aiPoints

    #Minimize the points
    else:
        for piece in aiPieces:
            if piece[0][1] == "R":
                aiPoints -= 4

            elif piece[0][1] == "N":
                aiPoints -= 2

            elif piece[0][1] == "B":
                aiPoints -= 3

            elif piece[0][1] == "Q":
                aiPoints -= 5

            elif piece[0][1] == "P":
                aiPoints -= 1

            elif piece[0][1] == "K":
                aiKing = True

        for piece in playerPieces:
            if piece[0][1] == "R":
                aiPoints += 4

            elif piece[0][1] == "N":
                aiPoints += 2

            elif piece[0][1] == "B":
                aiPoints += 3

            elif piece[0][1] == "Q":
                aiPoints += 5

            elif piece[0][1] == "P":
                aiPoints += 1

            elif piece[0][1] == "K":
                playerKing = True

        if not aiKing:
            aiPoints += 10000000000

        if not playerKing:
            aiPoints -= 10000000000

    return aiPoints


#Main Algorithm that does the searching
def depth_first_search(board, whiteTurn, level, myColour, curColour, isMaxLevel, alpha, beta):
    global counter
    global moveCount

    #Check the points of the board
    if level >= depth_floor:
        #Get the points
        points = get_points(board, myColour, curColour)

        #Maximize the points, only alpha will be changed
        if isMaxLevel:
            alpha = max(points, alpha)

        else:
            beta = min(points, beta)

        return board, False, alpha, beta

    pieces = get_pieces(board, curColour)

    for piece in pieces:
        moves = get_moves(board, whiteTurn, piece[1], piece[2])
        moveCount += len(moves)

        for move in moves:
            newBoard = copy.deepcopy(board)

            #Make the move, ans will be true if the move is valid
            newBoard, ans = make_move(newBoard, whiteTurn, piece[1], piece[2], move[0], move[1])

            if ans:
                newColour = "w" if curColour == "b" else "b"
                newBoard, ans, newAlpha, newBeta = depth_first_search(newBoard, not whiteTurn, level + 1, myColour, newColour, not isMaxLevel, alpha, beta)

                #Maximize the points, only alpha will be changed
                if isMaxLevel:
                    alpha = max(alpha, max(newAlpha, newBeta))

                else:
                    beta = min(beta, min(newAlpha, newBeta))

                #return newBoard, True, alpha, beta

    # There's no pieces left on the board
    return board, False, alpha, beta