import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score_card = ScoreCard()

    def __str__(self):
        return f"{self.name}'s ScoreCard: {self.score_card}"


class Dice:
    def __init__(self) -> None:
        self.value = random.choice([1, 2, 3, 4, 5, 6])
    
    def roll(self):
        self.value = random.choice([1, 2, 3, 4, 5, 6])

    def __repr__(self):
        return str(self.value)
    
    def __str__(self):
        return str(self.value)

class DiceSet:
    def __init__(self) -> None:
        self.set = [Dice() for _ in range(5)]

    def roll(self, keep=[]):
        for i, dice in enumerate(self.set):
            if i+1 not in keep:
                dice.roll()
    
    def __str__(self) -> str:
        dice_values = [f'Dice {i+1} : {str(d)}' for i,d in enumerate(self.set)]
        return '\n'.join(dice_values)
    
    def __repr__(self):
        dice_values = [f'Dice {i+1} : {str(d)}' for i,d in enumerate(self.set)]
        return '\n'.join(dice_values)
    
class ScoreCard:
    def __init__(self) -> None:
        self.scores = {
                'ones': None, 
                'twos': None, 
                'threes': None, 
                'fours': None, 
                'fives': None, 
                'sixes': None,
                'bonus': None,
                'three_of_a_kind': None, 
                'four_of_a_kind': None, 
                'full_house': None, 
                'small_straight': None,
                'large_straight': None, 
                'yahtzee': None, 
                'chance': None
            }
        
    def calculate_score(self, category, dice_set):
        dices = [dice.value for dice in dice_set]
        counts = [dices.count(x) for x in set(dices)]
        
        if category == 'ones':
            return dices.count(1)*1
        elif category == 'twos':
            return dices.count(2)*2
        elif category == 'threes':
            return dices.count(3)*3
        elif category == 'fours':
            return dices.count(4)*4
        elif category == 'fives':
            return dices.count(5)*5
        elif category == 'sixes':
            return dices.count(6)*6
        elif category == 'three_of_a_kind' and max(counts) >= 3:
            return sum(dices)
        elif category == 'four_of_a_kind' and max(counts) >= 4:
            return sum(dices)
        elif category == 'full_house' and sorted(counts) == [2, 3]:
            return 25
        elif category == 'small_straight' and (set([1, 2, 3, 4]).issubset(set(dices)) or
                                              set([2, 3, 4, 5]).issubset(set(dices)) or
                                              set([3, 4, 5, 6]).issubset(set(dices))):
            return 30
        elif category == 'large_straight' and (set([1, 2, 3, 4, 5]).issubset(set(dices)) or
                                               set([2, 3, 4, 5, 6]).issubset(set(dices))):
            return 40
        elif category == 'yahtzee' and max(counts) == 5:
            return 50
        elif category == 'chance':
            return sum(dices)
        
    def project_scores(self, dice_set):
        projected_scores = {}
        for category in self.scores.keys():
            projected_scores[category] = self.calculate_score(category, dice_set)
        return projected_scores
    
    def __str__(self):
        return str(self.scores)
        
class Game:
    def __init__(self, player_names):
        self.players = [Player(name) for name in player_names]
        self.current_player_index = 0
        self.dice_set = DiceSet()

    def play_turn(self):
        player = self.players
        print(f"\n{player.name}'s turn:")
        print("Initial roll:")
        print(self.dice_set)

        keep = input("Enter dice positions to keep (comma-separated, e.g., 0,1): ")
        keep = list(map(int, keep.split(',')))

        self.dice_set.roll(keep)
        print("After roll:")
        print(self.dice_set)

        category = input("Enter the category to score (e.g., 'ones', 'three_of_a_kind'): ")
        score = player.score_card.calculate_score(category, self.dice_set.dice)
        player.score_card.scores[category] = score
        print(f"Score for {category}: {score}")

        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def __str__(self):
        return '\n'.join(str(player) for player in self.players)