import random
import farkle_core

class Player:

    def __init__(self, minimum_threshold, risk_threshold, lucky_die):
        self.minimum_threshold = minimum_threshold
        self.risk_threshold = risk_threshold
        self.lucky_die = lucky_die
        self.farkle_count = 0

    def reset(self):
        self.farkle_count = 0

    @staticmethod
    def score(nums,lucky_die=0,custom_rules=False):
        counts = farkle_core.counts(nums)
        ones = counts[0]
        fives = counts[4]

        # Straight?
        if (len(set(nums)) == 6):
            return [150, 6]
        
        # 4 of a kind and a pair
        if (any(count == 4 for count in counts) and any(count == 2 for count in counts)):
            return [250,6]
        
        # 2 Triplets
        if (counts.count(3) == 2):
            return [150,6]
        
        # 3 Doubles
        if (counts.count(2) == 3):
            return [150,6]

        # 6 of a kind
        if (any(count == 6 for count in counts)):
            return [300, 6]
        
        # 5 of a kind
        if (any(count == 5 for count in counts)):
            leftovers = [num for num in nums if counts[num - 1] != 5]
            leftover_score = Player.score(leftovers,lucky_die=lucky_die,custom_rules=custom_rules)
            return [200 + leftover_score[0], 5 + leftover_score[1]]
        
        # CUSTOM RULES

        # Small Straight
        if (custom_rules):
            if (any(a - b == 1 for a,b in zip(nums[1:], nums[:-1])) and len(nums) >= 5):
                if (ones - 1 == 1):
                    return [85,6]
                elif (fives - 1 == 1):
                    return [80,6]
                return [75,5]
            
        # Full House
        if (custom_rules):
            if (counts.count(3) == 1 and counts.count(2) == 1):
                if (ones == 1):
                    return [85,6]
                elif (fives == 1):
                    return [80,6]
                return [75,5]

        
        # Custom Rules for 4 dice
        if (custom_rules and len(nums) == 4):
            # 2 Doubles
            if (counts.count(2) == 2):
                return [50,4]
            # Tiny Straight
            if (any(a - b == 1 for a,b in zip(nums[1:], nums[:-1])) and len(nums) == 4):
                return [50,4]
        
        # Custom Rules for 2 dice
        if (custom_rules and len(nums) == 2):
            # A Pair
            if (counts.count(2) == 1):
                return [25,2]
            
        if (custom_rules and len(nums) == 1):
            # Lucky die
            if (nums[0] == lucky_die):
                return [0,1]

        # END CUSTOM RULES

        # 4 of a kind
        if (any(count == 4 for count in counts)):
            leftovers = [num for num in nums if counts[num - 1] != 4]
            leftover_score = Player.score(leftovers,lucky_die=lucky_die,custom_rules=custom_rules)
            return [100 + leftover_score[0], 4 + leftover_score[1]]

        # 3 of a kind
        if (any(count == 3 for count in counts)):
            triple_score = (counts.index(3) + 1) * 10
            if triple_score == 10:
                triple_score = 30
            leftovers = [num for num in nums if counts[num - 1] != 3]
            leftover_score = Player.score(leftovers,lucky_die=lucky_die,custom_rules=custom_rules)
            return [triple_score + leftover_score[0], 3 + leftover_score[1]]


        # Ones and Fives only

        return [(ones * 10 + fives * 5), ones + fives]


    def roll(self,pts,dice,custom_rules=False):
        if (dice != 6):
            if dice == 0:
                return self.roll(pts, 6)
            if pts >= self.minimum_threshold:
                return pts
        nums = [random.randint(1,6) for _ in range(dice)]
        nums.sort()
        [rollScore, rollUsed] = Player.score(nums,lucky_die=self.lucky_die,custom_rules=custom_rules)
        if (rollScore == 0 and rollUsed == 0):
            self.farkle_count += 1
            return 0
        return self.roll(rollScore + pts, dice - rollUsed)

    def turn(self):
        dice = 6
        pts = 0
        return self.roll(pts, dice)