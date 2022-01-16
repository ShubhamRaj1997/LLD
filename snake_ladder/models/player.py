import itertools

from snake_ladder.constants.board_constants import BoardConstants
from snake_ladder.models.dice import Dice
from snake_ladder.strategy.strategy import DiceRollStrategy


class Player(object):
    itr = itertools.count()

    def __init__(self, name: str, dice: Dice):
        self.id = next(self.itr)
        self.name = name
        self.__cur_position = None
        self.dice = dice


    @property
    def cur_position(self):
        return self.__cur_position

    @cur_position.setter
    def cur_position(self, pos):
        assert BoardConstants.BOARD_SIZE >= pos >= 0
        self.__cur_position = value

    def roll_dice(self, dice_strategy: DiceRollStrategy):
        pos = self.cur_position
        turn = 1
        dice_val = dice_strategy.roll_dice()
        pos += dice_val
        while turn <= 3 and dice_val == 6:
            dice_val = dice_strategy.roll_dice()
            pos += dice_val
            turn += 1
        pos = max(pos, BoardConstants.BOARD_SIZE)
        self.cur_position = pos if turn < 4 else self.cur_position
