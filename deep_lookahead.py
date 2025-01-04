#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
this implements the greedy 2048 strategy
"""

import random

# Part 1: Helper Functions ###################################################

def is_full(board, col):
    for r in range(len(board)):
        if board[r][col] == 0:
            return False
    return True

def random_column(board):
    empty_cols = []
    for c in range(len(board[0])):
        if not is_full(board, c):
            empty_cols.append(c)
    return random.choice(empty_cols)

def top_block(board, col):
    if is_full(board, col):
        return -1
    for r in range(len(board)):
        if board[r][col] != 0:
            return board[r][col]
    return 0

def all_top_blocks(board):
    top_blocks = []
    for c in range(len(board[0])):
        if top_block(board, c):
            top_blocks.append(top_block(board, c))
        elif is_full(board, c):
            top_blocks.append(-1)
        elif not is_full(board, c):
            top_blocks.append(0)
    return top_blocks

def find_shortest(board):
    x = 0
    col = 0
    for c in range(len(board[0])):
        zeros = 0
        for r in range(len(board)):
            if board[r][c] == 0:
                zeros += 1
        if zeros > x:
            col = c
            x = zeros
    return col

def is_increasing(board, col):
    for r in range(1, len(board)):
        if board[r][col] < board[r -1][col]:
            return False
    return True




# Part 2: AI Functions #######################################################


def play_vertical_matcher(block, board):
    for c in range(len(board[0])):
        top = top_block(board, c)
        if top == block:
            return c
    return random_column(board)


def play_better_vertical_matcher(block, board):
    for c in range(len(board[0])):
        top = top_block(board, c)
        if top == block:
            return c
    for c in range(len(board[0])):
        top = top_block(board, c)
        if top > block:
            return c
    return random_column(board)

#this is super fast logic
def play_super_fast_strategy(board):
    num_cols = len(board[0])

    for col in range(num_cols):
        # Check if the column has space for the block
        if not is_full(board, col):
            return col

    # If no columns are available (shouldn't happen), just return column 0
    return 0



# Given Functions ##############################################

# play interactively -- this code is complete -- no changes needed
def play_console_control(block, board):
    num_cols = len(board[0])
    col = int(input("Drop " + str(block) + " in which column: "))

    # ask again if given an invalid column
    while col < 0 or col >= num_cols:
        col = int(input("Drop " + str(block) + " in which column: "))

    return col


# uncomment one line -- this is the strategy used to play the game
def strategy(board):
    #input()  # uncomment to pause the loop between every board update
    #return play_console_control(block, board)    # interactive
    #return play_vertical_matcher(block, board)
    #return play_better_vertical_matcher(block, board)
    return play_super_fast_strategy(board)


if __name__ == "__main__":
    import block_2048
    block_2048.main()
    import big_board
    #big_board.main()
    # import bigger_board
    # bigger_board.main()