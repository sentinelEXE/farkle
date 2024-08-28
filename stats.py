from player import Player
from farkle_core import random_lucky_die
import matplotlib.pyplot as plt

mins = []
turns = []
farks = []

def game(p: Player):
    turnCount = 1
    ptCount = 0
    while(ptCount < 1000):
        ptCount += p.turn()
        turnCount += 1
    return turnCount

def run_turns(p: Player, turn_count=10):
    total_farkles = 0
    turn = 0
    while(turn < turn_count):
        p.turn()
        total_farkles = p.farkle_count
        p.reset()
        turn += 1
    return total_farkles

def run_one_min_turns(p: Player, game_count=100,turn_count=10):
    total_farkles = 0
    for _ in range(game_count):
        p.lucky_die = random_lucky_die()
        total_farkles += run_turns(p,turn_count)
        p.reset()
    mins.append(p.minimum_threshold)
    farks.append(total_farkles / game_count)
    return total_farkles

def run_one_min_game(p: Player, game_count=100):
    total_turns = 0
    total_farkles = 0
    for _ in range(game_count):
        p.lucky_die = random_lucky_die()
        total_turns += game(p)
        total_farkles += p.farkle_count
        p.reset()
    mins.append(p.minimum_threshold)
    turns.append(total_turns / game_count)
    farks.append(total_farkles / game_count)
    return total_turns / game_count

def stats_for_range(low_threshold,high_threshold,game_count=100,turn_count=None):
    stats = []
    for i in range(low_threshold,high_threshold,5):
        p = Player(i, 0, random_lucky_die())
        if turn_count != None:
            stats += [run_one_min_turns(p,game_count,turn_count)]
        else:
            stats += [run_one_min_game(p,game_count)]
    
    return stats

def graph_turns_and_farkles(low_threshold, high_threshold, game_count):
    avgs = stats_for_range(low_threshold,high_threshold,game_count)
    x = zip(range(low_threshold,high_threshold,5),avgs)

    plt.plot(mins, turns, label='Average Turns')
    plt.plot(mins, farks, label='Average Farkles')
    plt.xlabel('Minimum Threshold')
    plt.ylabel('Averages')

    plt.legend()
    plt.show()

def graph_farkles(low_threshold, high_threshold, game_count, turn_count):
    avgs = stats_for_range(low_threshold,high_threshold,game_count,turn_count)
    x = zip(range(low_threshold,high_threshold,5),avgs)

    plt.plot(mins, farks, label='Average Farkles')
    plt.xlabel('Minimum Threshold')
    plt.ylabel('Averages')

    plt.legend()
    plt.show()
graph_farkles(5,205,100,10)
#for a,b in x:
    #print(str(a) +  " : " + str(b) + "\n")
