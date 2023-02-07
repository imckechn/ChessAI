def init_board():
    board = [
        ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
        ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
        ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
        ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
        ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
        ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
        ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
        ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR']
    ]

    return board


def print_board(board):
    for i in range(8):
        print(i, '   '.join(board[i]))

    print("  A    B    C    D    E    F    G    H")