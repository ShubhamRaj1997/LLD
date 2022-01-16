import random
from abc import ABC, abstractmethod

from snake_ladder.models.dice import Dice


class DiceRollStrategy(ABC):
    @abstractmethod
    def roll_dice(self):
        pass


class SingleDiceRollStrategy(DiceRollStrategy):
    def roll_dice(self):
        dice = random.choice(list(Dice))
        return dice


class MultiDiceRollStrategy(DiceRollStrategy):
    def roll_dice(self, num_of_dices=2):
        dice_values = list()
        for _ in range(0,num_of_dices):
            dice_values.append(random.choice(list(Dice)))
        return sum(dice_values)


