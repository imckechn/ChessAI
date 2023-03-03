from board import *
import copy

depth_floor = 4

#Gets the points given a boardState and a colour
def get_points(board, colour):
    colour = colour.lower()
    if len(colour) != 1:
        colour = colour[0]

    points = 0

    for i in range(8):
        for j in range(8):
            if board[i][j][0] == colour:
                if board[i][j][1] == "P":
                    points += 1

                elif board[i][j][1] == "R":
                    points += 4

                elif board[i][j][1] == "K":
                    points += 3

                elif board[i][j][1] == "B":
                    points += 3

                elif board[i][j][1] == "Q":
                    points += 5

    return points


#Main Algorithm that does the searching
def depth_first_search(board, whiteTurn, level, myColour, curColour):

    #Check the points of the board
    if level >= depth_floor:
        return board, False

    pieces = get_pieces(board,curColour)

    for piece in pieces:
        moves = get_moves(board, whiteTurn, piece[1], piece[2])

        for move in moves:
            newBoard = copy.deepcopy(board)
            newBoard, ans = make_move(newBoard, whiteTurn, piece[1], piece[2], move[0], move[1])

            if ans:
                if checkmate(newBoard, whiteTurn,myColour):
                    return newBoard, True
                
                newColour = "wK" if curColour == "bK" else "bK"
                newBoard, ans = depth_first_search(newBoard, not whiteTurn, level + 1, myColour, newColour)

                if ans:
                    return newBoard, True

