#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
this implements the expo time 2048 strategy
"""

import random
import copy

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

def find_first_empty_row(board, col):
    for row in range(len(board)):
        if board[row][col] == 0:
            return row
    return -1  # Column is full

def impose_gravity(board, col):
    last_empty_row = -1
    for row in range(len(board)):
        if board[row][col] == 0:
            if last_empty_row == -1:
                last_empty_row = row
        else:
            if last_empty_row != -1:
                board[last_empty_row][col] = board[row][col]
                board[row][col] = 0
                last_empty_row += 1


def check_column(board, col):
    row = len(board) - 1
    score = 0  # Initialize score for the column

    while row >= 0:
        this_block = board[row][col]
        if isinstance(this_block, int):  # Ensure it's an integer, not a function
            if this_block > 0:
                matches = 0
                if col > 0 and board[row][col - 1] == this_block:
                    matches += 2  # Reward for matching left block
                if col + 1 < len(board[0]) and board[row][col + 1] == this_block:
                    matches += 4  # Reward for matching right block
                if row > 0 and board[row - 1][col] == this_block:
                    matches += 1  # Reward for matching above block

                if matches > 0:
                    combine_blocks(board, row, col, matches)  # Combine blocks and update score
                    score += matches  # Add matches to the score

        row -= 1

    return score  # Return the score change



def combine_blocks(board, row, col, matches):
    """ Combine blocks based on matches """
    this_block = board[row][col]

    if matches == 7:
        board[row - 1][col] = 8 * this_block
        board[row][col] = 0
        board[row][col - 1] = 0
        board[row][col + 1] = 0
    elif matches == 6:
        board[row][col] = 4 * this_block
        board[row][col - 1] = 0
        board[row][col + 1] = 0
    elif matches == 5:
        board[row - 1][col] = 4 * this_block
        board[row][col] = 0
        board[row][col + 1] = 0
    elif matches == 4:
        board[row][col] = 2 * this_block
        board[row][col + 1] = 0
    elif matches == 3:
        board[row - 1][col] = 4 * this_block
        board[row][col] = 0
        board[row][col - 1] = 0
    elif matches == 2:
        board[row][col] = 2 * this_block
        board[row][col - 1] = 0
    elif matches == 1:
        board[row - 1][col] = 2 * this_block
        board[row][col] = 0


def get_block_random():
    """ Generate a random block value """
    return 2 ** random.randint(1, 6)



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

#this is the weighted column strategy logic
import random
import copy


# Function to simulate a single move and return the resulting board and score
def simulate_move(board, block, col):
    sim_board = copy.deepcopy(board)

    # Find the first empty row in the column
    row = find_first_empty_row(sim_board, col)

    # Place the block on the board
    if row >= 0:
        sim_board[row][col] = block
    else:
        return sim_board, 0  # No valid move

    # After placing the block, check if any merges happen
    score = 0
    changed_cols = [col]
    while len(changed_cols) > 0:
        score += check_column(sim_board, changed_cols.pop(0))

    # After checking for merges, apply gravity
    for c in range(len(sim_board[0])):
        impose_gravity(sim_board, c)

    return sim_board, score


# Function to simulate the game for a certain depth (exponentially)
def simulate_game(board, block, next_block, depth):
    if depth == 0:
        return 0  # Base case: no further moves

    best_score = 0
    # Try all possible moves in each column
    for col in range(len(board[0])):
        # Simulate the move for the current block in the column
        sim_board, score = simulate_move(board, block, col)

        # Recursively simulate the next depth with the new board and the next block
        future_score = score + simulate_game(sim_board, next_block, get_block_random(), depth - 1)

        # Track the best score from all possible moves
        best_score = max(best_score, future_score)

    return best_score

# Exponential Time Complexity Strategy for 2048
def strategy_exponential(block, next_block, board, depth=3):
    best_score = -float('inf')
    best_col = None

    # Try all possible moves in each column and simulate the game recursively
    for col in range(len(board[0])):
        sim_board, score = simulate_move(board, block, col)

        # Calculate the score of the entire game after this move
        future_score = score + simulate_game(sim_board, next_block, get_block_random(), depth - 1)

        if future_score > best_score:
            best_score = future_score
            best_col = col

    return best_col



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
def strategy(block, next_block, board, depth):
    #input()  # uncomment to pause the loop between every board update
    #return play_console_control(block, board)    # interactive
    #return play_vertical_matcher(block, board)
    #return play_better_vertical_matcher(block, board)
    return strategy_exponential(block, next_block, board, depth=3)


if __name__ == "__main__":
    import block_2048_expo
    block_2048_expo.main()
    import big_board
    #big_board.main()
    # import bigger_board
    # bigger_board.main()
