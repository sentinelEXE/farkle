from player import Player

def test_score():
    straight = [1,2,3,4,5,6]
    four_and_pair = [6] * 4 + [2] * 2
    two_trips = [2] * 3 + [3] * 3
    three_pairs = [2,2,3,3,4,4]
    six = [4] * 6
    five = [2] * 5 + [6]
    five_and_one = [2] * 5 + [1]
    four = [3] * 4
    four_five_one = [3] * 4 + [5,1]
    triple_six = [6] * 3 + [1,2,3]
    triple_five = [5] * 3 + [2,4,6]
    triple_one = [1] * 3 + [5,4,6]
    ones_and_fives = [1] * 2 + [5] * 2 + [3,4]
    rolls = [straight,four_and_pair,two_trips,three_pairs,six,five,five_and_one,four,four_five_one,triple_six,triple_five,triple_one,ones_and_fives]
    scores = [150,250,150,150,300,200,210,100,115,70,50,35,30]
    for score1,roll in zip(scores,rolls):
        if (Player.score(roll)[0] == score1):
            print("Correct score")
            print([score1,roll])
            print("\n")
        else:
            print("Incorrect score: \n")
            print([score1,roll])
            print("\n")

def test_custom():
    small_straight = [1,2,3,4,4,5]
    small_straight_and_one = [1,1,2,3,4,5]
    full_house = [2] * 3 + [3] * 2
    doubles = [2]* 2 + [6] * 2
    tiny_straight = [2,3,4,5]
    pair = [4] * 2
    lucky = [3]
    rolls = [small_straight,small_straight_and_one,full_house,doubles,tiny_straight,pair,lucky]
    scores = [75,85,75,50,50,25,0]
    for score1,roll in zip(scores,rolls):
        if (Player.score(roll)[0] == score1):
            print("Correct score")
            print([score1,roll])
            print("\n")
        else:
            print("Incorrect score: \n")
            print([score1,roll])
            print("\n")

test_score()