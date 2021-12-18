import pandas as pd
import os
import csv
import numpy as np


def d4_1():
    data = pd.read_csv("input_4.csv", skiprows = 1, header = None, delim_whitespace = True, names = [1, 2, 3, 4, 5])
    CHUNK_SIZE = 5
    boards = []
    boards.extend([data.iloc[i-CHUNK_SIZE:i] for i in range(CHUNK_SIZE, len(data) + 1, CHUNK_SIZE)])
    with open("input_4.csv") as input:
        reader = csv.reader(input)
        nums_called = [int(x) for x in next(reader)]

    found = None
    i = 0
    while not isinstance(found, pd.DataFrame):
        altered_boards = [board.replace(nums_called[:i + 1], np.nan) for board in boards]
        found = check_board_1(altered_boards)
        i = i + 1

    print(int(nums_called[i-1] * found.fillna(0).to_numpy().sum()))

def check_board_1(altered_boards):
    for board in altered_boards:
        for col in board.columns:
            if board[col].isnull().values.all():
                return board
            else:
                continue

        for index, row in board.iterrows():
            if row.isnull().values.all():
                return board
            else:
                continue

    return None

def d4_2():
    data = pd.read_csv("input_4.csv", skiprows = 1, header = None, delim_whitespace = True, names = [1, 2, 3, 4, 5])
    CHUNK_SIZE = 5
    boards = []
    boards.extend([data.iloc[i-CHUNK_SIZE:i] for i in range(CHUNK_SIZE, len(data) + 1, CHUNK_SIZE)])

    with open("input_4.csv") as input:
        reader = csv.reader(input)
        nums_called = [int(x) for x in next(reader)]

    final_win = None

    found = boards
    for i in range(len(nums_called)):
        altered_boards = [board.replace(nums_called[:i+1], np.nan) for board in found]
        found = check_board_2(altered_boards)

        if len(found) == 1:
            final_board = found[0]
            while not isinstance(final_win, pd.DataFrame):
                final_win = check_board_1([final_board.replace(nums_called[:i+1], np.nan) for board in found])
                i = i + 1
            break

    print(int(nums_called[i-1] * final_win.fillna(0).to_numpy().sum()))


def check_board_2(altered_boards):
    no_win = []
    for board in altered_boards:
        win = False
        for col in board.columns:
            if board[col].isnull().values.all():
                win = True
                break

        for index, row in board.iterrows():
            if row.isnull().values.all():
                win = True
                break

        if win == False:
            no_win.append(board)

    return no_win

d4_1()
d4_2()
