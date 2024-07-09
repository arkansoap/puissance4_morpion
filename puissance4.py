"""Morpion

command : sudo venv/bin/python3.9 -m puissance4
"""

import keyboard
import subprocess


def emptyboard():
    return [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]


def printboard(board):
    subprocess.call("clear")
    for row in board:
        print(row)


def init():
    board = emptyboard()
    cursor = [0, 1]
    return board, cursor


def moove_cursor(cursor):
    if keyboard.is_pressed("q"):
        cursor[1] -= 1
    elif keyboard.is_pressed("d"):
        cursor[1] += 1
    if cursor[1] < 0:
        cursor[1] = 6
    if cursor[1] > 6:
        cursor[1] = 0
    return cursor


def drop_token(board, cursor, player):
    for i in reversed(range(6)):
        print(i)
        if board[i][cursor[1]] in [4, 8]:
            pass
        else:
            board[i][cursor[1]] = player[1]
            break
    printboard(board)
    game = check_endgame(board, player)
    return board, game


def check_4_follow(board):
    if board():
        pass


def check_victory(board, player):
    for i in range(5):
        for j in range(6):
            # horizontal
            # vertival
            # diagonal
            pass


def check_draw(board):
    for row in board:
        if 0 in row:
            return 0
    print("Draw")
    return 1


def check_endgame(board, player):
    if check_victory(board, player) == 1:
        return 1
    elif check_draw(board) == 1:
        return 1
    return 0


def player_turn(turn):
    if turn % 2 == 0:
        player = "player 1"
        player_piece = 3
    else:
        player = "player 2"
        player_piece = 8
    return [player, player_piece]


def main():
    game = 0
    turn = 0
    board, cursor = init()
    board[cursor[0]][cursor[1]] = 1
    touch = None
    printboard(board)
    while game != 1:
        player = player_turn(turn)
        print(f"{player[0]} plays")
        print(f"tour {turn}")
        touch = keyboard.read_event()
        if touch.name == "esc":
            game = 1
        elif keyboard.is_pressed("enter"):
            board, game = drop_token(board, cursor, player)
            turn += 1
        else:
            if board[cursor[0]][cursor[1]] not in [4, 8]:
                board[cursor[0]][cursor[1]] = 0
            cursor = moove_cursor(cursor)
            if board[cursor[0]][cursor[1]] not in [4, 8]:
                board[cursor[0]][cursor[1]] = 1
            printboard(board)


if __name__ == "__main__":
    main()