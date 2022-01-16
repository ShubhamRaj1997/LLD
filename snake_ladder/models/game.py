from typing import List

from snake_ladder.models.player import Player
from snake_ladder.models.snake import Snake, Ladder
from snake_ladder.strategy.strategy import DiceRollStrategy


class Game(object):
    def __init__(self, size: int, players: List[Player], snakes: List[Snake], ladders: List[Ladder],
                 dice_roll_strategy: DiceRollStrategy):
        self.size = size
        self.players = players
        self.snakes = snakes
        self.ladders = ladders
        self.dice_roll_strategy = dice_roll_strategy


    def make_move(self, player: Player):
        player.roll_dice(self.dice_roll_strategy)
        player.cur_position = self.update_with_props(player.cur_position)

    def get_winner(self, board):
        return board.is_occupied(self.size)

    def update_with_props(self, position):
        new_position = self.update_with_snake(position)
        new_position = self.update_with_ladder(new_position)
        return new_position

    def update_with_snake(self, position):
        final_position = position
        for snake in self.snakes:
            final_position = snake.end if snake.start == final_position else final_position
        return final_position

    def update_with_ladder(self, position):
        final_position = position
        for ladder in self.ladders:
            final_position = ladder.start if ladder.end == final_position else final_position
        return final_position
