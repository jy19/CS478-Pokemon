#!/usr/bin/python

import random

import type

# Not sure if this the best place for this function, but I put it here anyway
'''Dispatches the MLP program which is waiting on another process
Outputs a dictionary of each move and its weights'''
def dispatch_mlp(gamestate):
    pass

'''Chooses the move to use'''
def choose_move(available_moves, move_weights):
    action_weights = {move: move_weights[move] for move in available_moves}
    total_weight = sum(action_weights.values())
    choice = random.uniform(0, total_weight)
    
    for move, w in action_weights.items():
        choice -= w
        if choice < 0:
            return move

'''Switch to the pokemon with the best type matchup
Expects Pokemon objects'''
def greedy_switch(opponent, options):
    return max(options, key = lambda opt: type.get_matchup(opt.typing, opponent.typing))