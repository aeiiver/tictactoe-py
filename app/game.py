from enum import Enum


class Player(Enum):
    PLAYER_X = 0
    PLAYER_O = 1


class Square(Enum):
    NOBODY = 0
    PLAYER_X = 1
    PLAYER_O = 2


class GameState(Enum):
    NOBODY_WON_YET = 0
    PLAYER_X_WON = 1
    PLAYER_O_WON = 2
    TIE = 3


class GameIsOverException(Exception):
    ...


class BadPositionError(Exception):
    ...


class SquareNotFreeError(Exception):
    ...


class Game:
    def __init__(self):
        self._board = [[Square.NOBODY, Square.NOBODY, Square.NOBODY],
                       [Square.NOBODY, Square.NOBODY, Square.NOBODY],
                       [Square.NOBODY, Square.NOBODY, Square.NOBODY]]
        self._next_player = Player.PLAYER_X
        self._is_over = False

    def player(self) -> Player:
        return self._next_player

    def is_over(self) -> bool:
        return self.state() != GameState.NOBODY_WON_YET

    def board(self) -> [[Square, Square, Square],
                        [Square, Square, Square],
                        [Square, Square, Square]]:
        return self._board

    def play(self, pos_xy: (int, int)):
        if self.is_over():
            raise GameIsOverException('Game is over')

        if pos_xy[0] < 0 or pos_xy[0] > 2:
            raise BadPositionError('Bad position')
        if pos_xy[1] < 0 or pos_xy[1] > 2:
            raise BadPositionError('Bad position')

        if self._board[pos_xy[1]][pos_xy[0]] != Square.NOBODY:
            raise SquareNotFreeError('A player already filled the square')

        self._board[pos_xy[1]][pos_xy[0]] = Square.PLAYER_X \
            if self._next_player == Player.PLAYER_X else Square.PLAYER_O
        self._rotate_player()

    def _rotate_player(self):
        if self._next_player == Player.PLAYER_X:
            self._next_player = Player.PLAYER_O
        else:
            self._next_player = Player.PLAYER_X

    def state(self) -> GameState:
        # Horizontals
        for row in self._board:
            if row[0] != Square.NOBODY and row[0] == row[1] == row[2]:
                if row[0] == Square.PLAYER_X:
                    return GameState.PLAYER_X_WON
                if row[0] == Square.PLAYER_O:
                    return GameState.PLAYER_O_WON

        # Verticals
        for col in range(3):
            if self._board[0][col] != Square.NOBODY and self._board[0][col] == self._board[1][col] == self._board[2][col]:
                if self._board[0][col] == Square.PLAYER_X:
                    return GameState.PLAYER_X_WON
                if self._board[0][col] == Square.PLAYER_O:
                    return GameState.PLAYER_O_WON

        # Top-left bottow-right diagonal
        if self._board[0][0] != Square.NOBODY and self._board[0][0] == self._board[1][1] == self._board[2][2]:
            if self._board[0][0] == Square.PLAYER_X:
                return GameState.PLAYER_X_WON
            if self._board[0][0] == Square.PLAYER_O:
                return GameState.PLAYER_O_WON

        # Top-right bottow-left diagonal
        if self._board[0][2] != Square.NOBODY and self._board[0][2] == self._board[1][1] == self._board[2][0]:
            if self._board[0][2] == Square.PLAYER_X:
                return GameState.PLAYER_X_WON
            if self._board[0][2] == Square.PLAYER_O:
                return GameState.PLAYER_O_WON

        # Nobody won yet
        for row in self._board:
            for square in row:
                if square == Square.NOBODY:
                    return GameState.NOBODY_WON_YET

        # No winner and no empty square, so the board is fully filled
        return GameState.TIE


if __name__ == "__main__":
    g = Game()

    g.play((0, 0))
    g.play((1, 0))
    g.play((0, 1))
    g.play((1, 1))
    g.play((0, 2))

    print(g.board())
    print(g.state())

    # This should error
    g.play((1, 2))
