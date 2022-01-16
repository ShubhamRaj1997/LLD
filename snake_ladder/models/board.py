from typing import List

from snake_ladder.models.player import Player
from snake_ladder.singleton import SingletonMeta


class Board(metaclass=SingletonMeta):
    _board = [[]]

    def __init__(self, board_size: int):
        self._board_size = board_size

    def make_piece(self, player: Player, start: int, end: int) -> bool:
        if not self.__is_move_possible(player.id, start, end):
            """
            You can raise from here also
            """
            return False
        self._board[start].remove(player.id)
        self._board[end].append(player.id)
        return True

    def __is_move_possible(self, player_id: int, start: int, end: int):
        if player_id in self._board[start] and player_id not in self._board[end]:
            return False
        return True

    def get_pieces(self, position: int) -> List[int]:
        return self._board[position]
