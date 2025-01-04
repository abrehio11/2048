#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Block-2048 Simulator (run lots of games)

Students: No changes are necessary in this file.

author: J. Hollingsworth
last updated: Nov 09 2020
"""

import block_2048_expo
import time

how_many = int(input('How many simulations? '))

sum_scores = 0
sum_moves = 0
best_score = 0
best_moves = 0
total_simulation_time = 0

for x in range(how_many):
    start_time = time.time()
    block_2048_expo.main(True)
    end_time = time.time()

    elapsed_time = end_time - start_time  # Calculate the elapsed time for the current simulation
    total_simulation_time += elapsed_time
    print(f'Simulation {x + 1} took {elapsed_time:.2f} seconds')

    sum_scores += block_2048_expo.score
    sum_moves += block_2048_expo.moves
    if block_2048_expo.score > best_score:
        best_score = block_2048_expo.score
    if block_2048_expo.moves > best_moves:
        best_moves = block_2048_expo.moves
    block_2048_expo.reset_game()

print('-' * 30)
print('avg score: {:,.2f}'.format(sum_scores / how_many))
print('avg moves: {:,.2f}'.format(sum_moves / how_many))
print('best score: {:,}'.format(best_score))
print('best moves: {:,}'.format(best_moves))
print('board size:', block_2048_expo.rows, ',', block_2048_expo.cols)

print(f'Total time for {how_many} simulations: {total_simulation_time:.2f} seconds')