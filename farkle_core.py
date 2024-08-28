import random

def random_lucky_die():
    return [2,3,4,6][random.randint(0,3)]

def counts(nums: list):
    ones = nums.count(1)
    twos = nums.count(2)
    threes = nums.count(3)
    fours = nums.count(4)
    fives = nums.count(5)
    sixes = nums.count(6)
    return [ones,twos,threes,fours,fives,sixes]