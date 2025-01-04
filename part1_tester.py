#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Code used to test the board validation functions.

Students: No changes are necessary in this file.

author: Your Elon CSC 1300 Professors
"""

import ai
import copy
import random

def print_board(board):
    maxNum = max([max(board[i]) for i in range(len(board))])
    space = len(str(maxNum))+1

    print('[  ')
    for row in range(len(board)):
        print('   [',end='')
        for col in range(len(board[0])-1):
            print(f'{board[row][col]:{space}},', end='')
        print(f'{board[row][col+1]:{space}}]')
    print(']')


def check_answer_board(fun_name, board, your_answer, my_answer):
    if your_answer is None or your_answer!= my_answer:
        print("INCORRECT: For function: ", fun_name)
        print("Your answer was:", your_answer)
        print("But should have been:", my_answer)
        print_board(board)
        return False
    return True

def check_answer_board_column(fun_name, board, col, your_answer, my_answer):
    if your_answer is None or your_answer!= my_answer:
        print("INCORRECT: For function: ", fun_name, "column", col)
        print("Your answer was:", your_answer)
        print("But should have been:", my_answer)
        print_board(board)
        return False
    return True

def test_shortest_column():
    test_boards = [
        [
            [0, 0, 2, 0, 0],
            [0, 4, 8, 0, 0],
            [0, 2, 4, 0, 0],
            [0, 4, 8, 0, 0],
            [0, 8, 2, 0, 0],
            [0, 4, 4, 0, 0],
            [0, 8, 2, 1, 4]
        ],
        [
            [0, 0, 2, 0, 0],
            [0, 4, 8, 0, 0],
            [0, 2, 4, 0, 0],
            [0, 4, 8, 0, 0],
            [0, 8, 2, 0, 0],
            [4, 2, 4, 2, 0],
        ],
        [
            [0, 0, 2, 0, 0, 8],
            [8, 4, 8, 0, 8, 4],
            [4, 2, 4, 2, 4, 2],

        ],
        [
            [8, 0, 2, 8],
            [4, 4, 8, 4],
            [2, 2, 4, 2],
            [8, 4, 8, 1],
            [4, 8, 2, 4],
            [2, 4, 4, 2],
            [8, 8, 2, 1]
        ],
        [
            [0, 0, 2, 0, 0],
            [8, 4, 8, 0, 0],
            [4, 2, 4, 0, 0],
            [2, 4, 8, 0, 0],
            [8, 8, 2, 0, 8],
            [4, 4, 4, 0, 2],
            [2, 8, 2, 1, 4]
        ]
    ]
    answers = [0, 4, 3, 1, 3]
    for i in range(len(test_boards)):
        your_answer = ai.find_shortest(test_boards[i])
        if not check_answer_board("find shortest",test_boards[i],your_answer,answers[i]):
            return False
    return True

def test_is_increasing():
    test_boards = [
        [
            [0, 0, 2, 0, 0],
            [0, 4, 8, 0, 0],
            [0, 2, 4, 0, 0],
            [0, 4, 8, 0, 0],
            [0, 8, 2, 0, 0],
            [0, 4, 4, 0, 0],
            [0, 8, 2, 1, 4]
        ],
        [
            [0, 2, 0, 8, 0],
            [0, 4, 8, 16, 0],
            [0, 8, 16, 32, 0],
            [0, 16, 32, 64, 0],
            [0, 32, 64, 128, 0],
            [4, 64, 64, 256, 0],
        ],
        [
            [2, 0, 2, 0, 0, 8],
            [4, 4, 8, 0, 2, 16],
            [2, 2, 4, 2, 4, 32],

        ],
        [
            [8, 0, 2, 2],
            [4, 2, 4, 4],
            [2, 4, 4, 4],
            [8, 8, 8, 8],
            [4, 16, 4, 8],
            [2, 32, 16, 4],
            [8, 8, 32, 8]
        ]
    ]
    answers = [[True, False, False, True, True],
               [True, True, True, True, True],
               [False, False, False, True, True, True],
               [False, False, False, False]]
    for i in range(len(test_boards)):
        for j in range(len(answers[i])):
            your_answer = ai.is_increasing(test_boards[i], j)
            if not check_answer_board_column("is_increasing",test_boards[i], j,your_answer,answers[i][j]):
                return False
    return True

def test_top_block():
    test_board_basic = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2],
        [0, 0, 0, 32, 8],
        [0, 0, 2, 16, 4],
        [0, 8, 16, 8, 2],
        [2, 4, 8, 4, 16],
        [4, 2, 4, 2, 32]
    ]
    answers_basic = [2, 8, 2, 32, 2]
    test_board_full = [
        [4, 0, 0, 0, 4],
        [2, 0, 0, 0, 2],
        [4, 0, 0, 32, 8],
        [2, 0, 2, 16, 4],
        [4, 0, 16, 8, 2],
        [2, 0, 8, 4, 16],
        [4, 0, 4, 2, 32]
    ]
    answers_full = [-1, 0, 2, 32, -1]
    test_board_dimensions = [
        [0, 0, 16, 0, 0, 0],
        [2, 4, 8, 0, 0, 0],
        [4, 2, 4, 2, 32, 0]
    ]
    answers_dimensions = [2, 4, -1, 2, 32, 0]
    test_boards = [test_board_basic, test_board_full, test_board_dimensions]
    answers = [answers_basic, answers_full, answers_dimensions]
    for i in range(len(test_boards)):
        for col in range(len(test_boards[i][0])):
            your_answer = ai.top_block(test_boards[i],col)
            if not check_answer_board_column("top_block", test_boards[i], col, your_answer, answers[i][col]):
                return False
    return True

def test_all_top_blocks():
    test_board_basic = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2],
        [0, 0, 0, 32, 8],
        [0, 0, 2, 16, 4],
        [0, 8, 16, 8, 2],
        [2, 4, 8, 4, 16],
        [4, 2, 4, 2, 32]
    ]
    answers_basic = [2, 8, 2, 32, 2]
    test_board_full = [
        [4, 0, 0, 0, 4],
        [2, 0, 0, 0, 2],
        [4, 0, 0, 32, 8],
        [2, 0, 2, 16, 4],
        [4, 0, 16, 8, 2],
        [2, 0, 8, 4, 16],
        [4, 0, 4, 2, 32]
    ]
    answers_full = [-1, 0, 2, 32, -1]
    test_board_dimensions = [
        [0, 0, 16, 0, 0, 0],
        [2, 4, 8, 0, 0, 0],
        [4, 2, 4, 2, 32, 0]
    ]
    answers_dimensions = [2, 4, -1, 2, 32, 0]
    test_boards = [test_board_basic, test_board_full, test_board_dimensions]
    answers = [answers_basic, answers_full, answers_dimensions]
    for i in range(len(test_boards)):
        your_answer = ai.all_top_blocks(test_boards[i])
        if not check_answer_board("all_top_blocks", test_boards[i], your_answer, answers[i]):
            return False
    return True


def run_better_random_test(test_board, full_cols, total_blanks, num_tests):
    compare_board = copy.deepcopy(test_board)
    changes = [0 for x in test_board[0]]
    for i in range(num_tests):
        answer = ai.random_column(test_board)
        if answer is None:
            print("INCORRECT: For function random_column")
            print('Failure: Returned None')
            print_board(test_board)
            return False
        if answer < 0 or answer >= len(changes):
            print("INCORRECT: For function random_column")
            print('Failure: Returned column that doesn\'t exist', answer)
            print_board(test_board)
            return False
        if answer in full_cols:
            print("INCORRECT: For function random_column")
            print('Failure: Trying to play in a full column:', answer)
            print_board(test_board)
            return False
        changes[answer] += 1
        test_board = copy.deepcopy(compare_board)
    for i in range(len(changes)):
        if changes[i] == 0 and i not in full_cols:
            print("INCORRECT: For function random_column")
            print('Failure: playing randomly never played in column: ', i)
            print_board(test_board)
            return False
    full_board = copy.deepcopy(test_board)
    for i in range(total_blanks):
        answer = ai.random_column(copy.deepcopy(full_board))
        if answer is None:
            print("INCORRECT: For function random_column")
            print('Failure: Returned None')
            print_board(full_board)
            return False
        if full_board[0][answer] != 0:
            print("INCORRECT: For function random_column")
            print('Failure: Trying to play in a full column:', answer)
            print_board(full_board)
            return False
        row = len(full_board) -1
        while full_board[row][answer] != 0:
            row -= 1
        full_board[row][answer] = 2
    return True

def test_is_full():
    testBoard = [
            [ 128,  2, 4,  2, 4],
            [16,  4, 2,  4, 8],
            [ 8,  2, 8, 16, 4],
            [ 2,  4, 2,  4, 2],
            [ 4, 16, 4,  8, 4],
            [ 2,  4, 2,  4, 2]
        ]
    randRow = [random.choice([0,2])**random.randint(3,6) for i in range(5)]
    testBoard.insert(0,randRow)
    for i in range(3):
        randRow = [random.choice([0,2])**random.randint(3,6) for i in range(5)]
        testBoard[0] = randRow
        ans = [True if testBoard[0][j] > 0 else False for j in range(len(testBoard[0]))]
        for j in range(len(ans)):
            answer = ai.is_full(testBoard, j)
            if not check_answer_board_column("is_full", testBoard, j, answer, ans[j]):
                return False
    randRow = [0 for i in range(5)]
    testBoard[0] = randRow
    for j in range(len(ans)):
        answer = ai.is_full(testBoard, j)
        if not check_answer_board_column("is_full", testBoard, j, answer, False):
            return False
    randRow = [2**i for i in range(1,6)]
    testBoard[0] = randRow
    for j in range(len(ans)):
        answer = ai.is_full(testBoard, j)
        if not check_answer_board_column("is_full", testBoard, j, answer, True):
            return False
    return True


def test_random_column():
    test_board1 = [
        [0, 0, 16, 0, 0],
        [32, 0, 8, 0, 2],
        [16, 0, 4, 0, 8],
        [8, 0, 2, 0, 4],
        [4, 8, 16, 0, 2],
        [2, 4, 8, 0, 16],
        [40, 2, 4, 0, 32]
    ]
    test_board2 = [
        [4, 0, 0, 32, 8, 0, 0],
        [2, 0, 2, 16, 4, 0, 0],
        [16, 8, 16, 8, 2, 0, 0],
        [2, 4, 8, 4, 16, 0, 0],
        [4, 2, 4, 2, 32, 0, 0]
    ]
    passes = run_better_random_test(test_board1, [2], 13, 100)
    if passes:
        passes = run_better_random_test(test_board2, [0, 3, 4], 13, 100)
    return passes


if __name__ == '__main__':
    print("Testing random column:")
    if test_random_column():
        print("******** ALL TESTS PASSED\n")
    print('Testing Is Full:')
    if test_is_full():
        print("******** ALL TESTS PASSED\n")
    print("Testing top block:")
    if test_top_block():
        print("******** ALL TESTS PASSED\n")
    print("Testing all top blocks:")
    if test_all_top_blocks():
        print("******** ALL TESTS PASSED\n")
    print("Testing find shortest:")
    if test_shortest_column():
        print("******** ALL TESTS PASSED\n")
    print("Testing is increasing:")
    if test_is_increasing():
        print("******** ALL TESTS PASSED\n")
