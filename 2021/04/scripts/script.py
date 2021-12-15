from aoc import aoc
import numpy as np

input = aoc.read_data('../input/in.txt')
bingo_numbers = list(map(int, input[:1][0][0].split(',')))
bingo_boards = input[1:]

BOARD_LENGTH, BOARD_WIDTH = 5, 5


class BingoBoard:
    def __init__(self, board_definition: list[str]):
        board_numbers = [int(num) for num in board_definition]
        self._board = np.array(board_numbers).reshape(BOARD_LENGTH, BOARD_WIDTH)
        self._board_value = self._board.sum()
        self._score = 0
        self._has_won = False
        self._rank = 0

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, value):
        self._board = value

    @property
    def score(self) -> int:
        return self._score

    @score.setter
    def score(self, value: int):
        self._score = value

    @property
    def has_won(self) -> bool:
        return self._has_won

    @has_won.setter
    def has_won(self, value: bool):
        self._has_won = value

    def mark(self, call) -> None:
        self._board = np.where(self._board == call, -1, self._board)
        self._board_value = self._board[(self._board > -1)].sum()
        self._score = self._board_value * call

    def check_bingo(self) -> bool:
        row_sums = self._board.sum(axis=1)
        col_sums = self._board.sum(axis=0)
        return True if -5 in row_sums or -5 in col_sums else False


class Bingo:
    def __init__(self, boards: list[list[str]], calls: list[int]):
        self._boards = [BingoBoard(b) for b in boards]
        self._calls = calls

    @property
    def boards(self) -> list[BingoBoard]:
        return self._boards

    @boards.setter
    def boards(self, value: list[BingoBoard]) -> None:
        self._boards = value

    def play_round(self, rnd: int, call: int) -> None:
        for board in self._boards:
            if not board.has_won:
                board.mark(call)
                if board.check_bingo():
                    board.has_won = True
                    print(f"Round {rnd}: New board has won! Score = {board.score}")

    def play(self) -> None:
        for i, c in enumerate(self._calls):
            self.play_round(i, c)


bingo_game = Bingo(bingo_boards, bingo_numbers)
bingo_game.play()


