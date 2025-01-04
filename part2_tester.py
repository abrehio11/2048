#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Code used to test the AI functions in part 2 of the project.
NOTE: Does NOT test your final AI.

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


def test_vertical_stacker():
    all_zeroes = []
    for r in range(7):
        all_zeroes.append([0 for i in range(5)])
    blocks = [2,4,8,16,32,64]
    answer = ai.play_vertical_matcher(16,all_zeroes)
    if answer is None:
            print("INCORRECT: For function play_vertical matcher")
            print('Failure: Returned None')
            print_board(all_zeroes)
            return False
    if answer not in range(5):
            print("INCORRECT: For function play_vertical matcher")
            print('Failure: On empty 7x5 board  Your column: ',answer)
            return False
    for i in range(20):
        test_board1 = copy.deepcopy(all_zeroes)
        ran_block = random.randint(0,5)
        ran_col = random.randint(0,4)
        test_board1[len(test_board1)-1][ran_col] = blocks[ran_block]
        answer = ai.play_vertical_matcher(blocks[ran_block],test_board1)
        if answer is None:
            print("INCORRECT: For function play_vertical matcher")
            print('Failure: Returned None')
            print_board(test_board1)
            return False
        if answer != ran_col:
            print("INCORRECT: For function play_vertical matcher")
            print('Failure: Failed to stack on existing block.  Your column: ',answer)
            print_board(test_board1)
            return False
    # make sure you don't play in a full column
    almost_full = [
        [0, 0, 0, 0, 0, 0],
        [2, 4, 8, 16, 32, 64],
        [4, 32, 4, 32, 8, 32],
        [2, 16, 2, 16, 4, 16],
        [4, 8, 16, 8, 2, 8],
        [2, 4, 8, 4, 16, 4],
        [4, 2, 4, 2, 32, 2]
    ]
    for i in range(len(blocks)):
       test_board = copy.deepcopy(almost_full)
       if i < len(blocks) - 1:
           block = blocks[i+1]
       else:
           block = 2
       test_board[1][i] = block
       test_board[0][i] = blocks[i]
       answer = ai.play_vertical_matcher(blocks[i],test_board)
       if answer is None:
            print("INCORRECT: For function play_vertical_matcher")
            print('Failure: Returned None')
            print_board(test_board)
            return False
       if answer == i:
            print("INCORRECT: For function play_vertical_matcher")
            print('Failure: Tried to play in full column: ',answer)
            print_board(test_board)
            return False
       if answer <0 or answer > 5:
            print("INCORRECT: For function play_vertical_matcher")
            print('Failure: Tried to play in illegal column: ',answer)
            print_board(test_board)
            return False
    return True


def test_better_vertical_stacker():
    all_zeroes = []
    for r in range(7):
        all_zeroes.append([0 for i in range(5)])
    blocks = [2,4,8,16,32,64]
    for i in range(20):
        test_board1 = copy.deepcopy(all_zeroes)
        ran_block = random.randint(0,5)
        ran_col = random.randint(0,4)
        test_board1[len(test_board1)-1][ran_col] = blocks[ran_block]
        answer = ai.play_better_vertical_matcher(blocks[ran_block],test_board1)
        if answer is None:
            print("INCORRECT: For function play_better_vertical_matcher")
            print('Failure: Returned None')
            print_board(test_board1)
            return False
        if answer != ran_col:
            print("INCORRECT: For function play_better vertical_matcher")
            print('Failure: Failed to stack on existing block.  Your column: ',answer)
            print_board(test_board1)
            return False
    # make sure you don't play in a full column
    almost_full = [
        [0, 0, 0, 0, 0, 0],
        [2, 4, 8, 16, 32, 64],
        [4, 32, 4, 32, 8, 32],
        [2, 16, 2, 16, 4, 16],
        [4, 8, 16, 8, 2, 8],
        [2, 4, 8, 4, 16, 4],
        [4, 2, 4, 2, 32, 2]
    ]
    for i in range(len(blocks)):
       test_board = copy.deepcopy(almost_full)
       if i < len(blocks) - 1:
           block = blocks[i+1]
       else:
           block = 2
       test_board[1][i] = block
       test_board[0][i] = blocks[i]
       answer = ai.play_better_vertical_matcher(blocks[i],test_board)
       if answer is None:
            print("INCORRECT: For function play_better_vertical_matcher")
            print('Failure: Returned None')
            print_board(test_board)
            return False
       if answer == i:
            print("INCORRECT: For function play_better_vertical_matcher")
            print('Failure: Tried to play in full column: ', answer)
            print_board(test_board)
            return False
       if answer < i and i !=5:
            print("INCORRECT: For function play_better_vertical_matcher")
            print('Failure to play on smaller tile: ', answer)
            print_board(test_board)
            return False
    return True

if __name__ == '__main__':
    print("Testing vertical_matcher:")
    if test_vertical_stacker():
        print("******** ALL TESTS PASSED")
    print("Testing better_vertical_matcher:")
    if test_better_vertical_stacker():
        print("******** ALL TESTS PASSED")
