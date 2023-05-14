from __future__ import annotations
from enum import Enum
from typing import List

from board import Piece, Board, Move


class TTTPiece(Piece, Enum):
    X = "X"
    O = "O"
    E = " "

    @property
    def opposite(self) -> TTTPiece:
        if self == TTTPiece.X:
            return TTTPiece.O
        elif self == TTTPiece.O:
            return TTTPiece.X
        else:
            return TTTPiece.E

    def __str__(self) -> str:
        return self.value


class TTTBoard(Board):
    def __init__(self, position: List[TTTPiece] = [TTTPiece.E] * 9, turn: TTTPiece = TTTPiece.X):
        self.postion: List[TTTPiece] = position
        self._turn: TTTPiece = turn

    @property
    def turn(self) -> Piece:
        return self._turn

    def move(self, location: Move) -> Board:
        temp_position: List[TTTPiece] = self.postion.copy()
        temp_position[location] = self._turn
        return TTTBoard(temp_position, self._turn.opposite)

    @property
    def legal_moves(self) -> List[Move]:
        return [Move(l) for l in range(len(self.postion)) if self.postion[l] == TTTPiece.E]

    @property
    def is_win(self) -> bool:
        return self.postion[0] == self.postion[1] and self.postion[0] == self.postion[2] and self.postion[0] != TTTPiece.E or \
            self.postion[3] == self.postion[4] and self.postion[3] == self.postion[5] and self.postion[3] != TTTPiece.E or \
            self.postion[6] == self.postion[7] and self.postion[6] == self.postion[8] and self.postion[6] != TTTPiece.E or \
            self.postion[0] == self.postion[3] and self.postion[0] == self.postion[6] and self.postion[0] != TTTPiece.E or \
            self.postion[1] == self.postion[4] and self.postion[1] == self.postion[7] and self.postion[1] != TTTPiece.E or \
            self.postion[2] == self.postion[5] and self.postion[2] == self.postion[8] and self.postion[2] != TTTPiece.E or \
            self.postion[0] == self.postion[4] and self.postion[0] == self.postion[8] and self.postion[0] != TTTPiece.E or \
            self.postion[2] == self.postion[4] and self.postion[2] == self.postion[6] and self.postion[2] != TTTPiece.E

    def evaluate(self, player: Piece) -> float:
        if self.is_win and self.turn == player:
            return -1
        elif self.is_win and self.turn != player:
            return 1
        else:
            return 0

    def __repr__(self) -> str:
        return f"""{self.postion[0]}|{self.postion[1]}|{self.postion[2]}
-----
{self.postion[3]}|{self.postion[4]}|{self.postion[5]}
-----
{self.postion[6]}|{self.postion[7]}|{self.postion[8]}"""