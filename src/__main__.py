import game as g
import pygame as pg
import sys as sys

WIDTH = 600
HEIGHT = 600
tile_width = WIDTH // 3
tile_height = HEIGHT // 3

BOARD = pg.image.load("static/board.png")
X_ = pg.image.load("static/player_x.png")
O_ = pg.image.load("static/player_o.png")
CURSOR_X_ = pg.transform.scale(X_, (tile_width // 2, tile_height // 2))
CURSOR_O_ = pg.transform.scale(O_, (tile_width // 2, tile_height // 2))


def as_board_pos(cursor_xy: (int, int)) -> (int, int):
    (cursor_x, cursor_y) = cursor_xy
    tile_width = WIDTH // 3
    tile_height = HEIGHT // 3

    for i in range(1, 4):
        if cursor_x < i * tile_width:
            x = i - 1
            break
    for i in range(1, 4):
        if cursor_y < i * tile_height:
            y = i - 1
            break

    return (x, y)


def as_pixel_pos(board_xy: (int, int)) -> (int, int):
    (x, y) = board_xy

    return (x * tile_width, y * tile_height)


def update_board(window: pg.Surface, game: g.Game):
    window.blit(BOARD, (0, 0))

    for idx_row, row in enumerate(game.board()):
        for idx_square, square in enumerate(row):
            match square:
                case g.Square.NOBODY:
                    continue
                case g.Square.PLAYER_X:
                    window.blit(X_, as_pixel_pos((idx_square, idx_row)))
                case g.Square.PLAYER_O:
                    window.blit(O_, as_pixel_pos((idx_square, idx_row)))


def update_cursor(window: pg.Surface, game: g.Game, cursor_xy: (int, int)):
    tile_width = WIDTH // 3
    tile_height = HEIGHT // 3

    match game.player():
        case g.Player.PLAYER_X:
            window.blit(CURSOR_X_, (cursor_xy[0] - tile_width // 4,
                                    cursor_xy[1] - tile_height // 4))
        case g.Player.PLAYER_O:
            window.blit(CURSOR_O_, (cursor_xy[0] - tile_width // 4,
                                    cursor_xy[1] - tile_height // 4))


def main():
    pg.init()
    pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption('Tic-Tac-Toe')

    game = g.Game()
    window = pg.display.get_surface()
    running = True

    while running:
        cursor_xy = pg.mouse.get_pos()

        for event in pg.event.get():
            match event.type:
                case pg.QUIT:
                    print('Exiting...')
                    running = False

                case pg.MOUSEBUTTONDOWN:
                    try:
                        game.play(as_board_pos(cursor_xy))

                    except g.GameIsOverException as e:
                        # This shouldn't happen unless we failed in this file
                        print(f'Internal error: {e}')

                    except g.BadPositionError as e:
                        # This shouldn't happen unless we failed in this file
                        print(f'Internal error: {e}')

                    except g.SquareNotFreeError:
                        # Do nothing
                        ...

            match game.state():
                case g.GameState.NOBODY_WON_YET:
                    continue

                case g.GameState.PLAYER_X_WON:
                    print('Player X won.')
                    running = False

                case g.GameState.PLAYER_O_WON:
                    print('Player O won.')
                    running = False

                case g.GameState.TIE:
                    print('Tie')
                    running = False

        update_board(window, game)
        update_cursor(window, game, cursor_xy)
        pg.display.update()

    pg.display.quit()
    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()
