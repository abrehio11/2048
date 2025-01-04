#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Artificial Intelligence for Block-2048

Students: Work in this file for the Final Project

author: CSC 1300 Professors and  Ashlee    <-- Your name here
last updated: April 19 2022
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

#my logic is awesome because it will see if block and next_block match so they can be played
#in the same column and add up while block is already placed on top of
#a bigger number in the table
def play_my_awesome_logic(block, next_block, board):
    for c in range(len(board[0])):
        top = top_block(board, c)
        if top == block:
            return c
    for c in range(len(board[0])):
        top = top_block(board, c)
        if top > block:
            return c
    for c in range(len(board[0])):
        top = top_block(board, c)
        if block == next_block and block < top:
            return c
    return random_column(board)



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
def strategy(block, next_block, board):
    #input()  # uncomment to pause the loop between every board update
    #return play_console_control(block, board)    # interactive
    #return play_vertical_matcher(block, board)
    #return play_better_vertical_matcher(block, board)
    return play_my_awesome_logic(block, next_block, board)


if __name__ == "__main__":
    import block_2048
    #block_2048.main()
    import big_board
    #big_board.main()
    import bigger_board
    bigger_board.main()





