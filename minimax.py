"""
kboeckx@elec.rma.ac.be
24/04/18

Use minimax to devise strategy for ConnectFour

"""

import copy
import pdb
from game import Game, symbols

def other(player):
    return 1-player

def terminal_test(game, player):
    if game.check(player):
        return 100
    if game.check(other(player)):
        return -100
    else:
        return False

def argmax(results):
    return sorted(zip(results.values(), results.keys()))[-1][1]

def eval_game(game, player):
    total = 0
    # simple eval: sum of lines still open
    lines = game.get_rows()
    lines.extend(game.get_cols())
    lines.extend(game.get_diags())
    for line in lines:
        line_total = 0
        temp = 0
        for item in line:
            if item == symbols[player]:
                temp += 1
            elif item == symbols[other(player)]:
                temp = 0
            elif item == '.':
                line_total += temp
                temp = 0
        
        total += line_total
    return total

def min_value(game, player, depth):
    if depth == 0:
        return eval_game(game, player) - eval_game(game, other(player))
    v = -float('infinity')
    for action in game.moves(player):
        if terminal_test(game, player):
            return -terminal_test(game, player)
        g_new = copy.deepcopy(game)
        g_new.drop(action, player)
        v = max(v, min_value(g_new, other(player), depth-1))
    return v

def max_value(game, player, depth):
    if depth == 0:
        return eval_game(game, player) - eval_game(game, other(player))
    v = float('infinity')
    for action in game.moves(player):
        if terminal_test(game, player):
            return terminal_test(game, player)
        g_new = copy.deepcopy(game)
        g_new.drop(action, player)
        v = max(v, min_value(g_new, other(player), depth-1))
    return v

def minimax(game, player, depth=3):
    results = {}
    for action in game.moves(player):
        g_new = copy.deepcopy(game)
        g_new.drop(action, player)
        results[action] = min_value(g_new, other(player), depth)
    print('player ', symbols[player], '->', results)
    #pdb.set_trace()
    return argmax(results)

if __name__ == '__main__':
    g = Game()    
    
    player = 0
    game = Game()
    for ii in range(10):
        for player in [0, 1]:
            game.drop(minimax(game, player, depth=3), player)
            print(game)
            if terminal_test(game, player):
                print('Game over')
                break
        

