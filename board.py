import itertools
from collections import defaultdict
from tools import shift_to_point
from tools import add_tup


def fit_in_start_board_filter(piece_loc: list) -> bool:
    for point in piece_loc:
        if (max(point) > 3) or (min(point) < 0):
            return False
    return True


def neighboars(cell: tuple) -> set:
    return set(
        add_tup(cell, i) for i in [
            (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)
        ]
    )


def number_of_neighboars(board: set, cell: tuple) -> int:
    return len(neighboars(cell).intersection(board))


def generate_the_board(n: int = 4) -> set:
    board_base = 3*(list(range(n)), )
    return set(itertools.product(*board_base))


def piece_fit_in_starting_board(point: tuple, piece: list) -> list:
    shifted_pieces = [
        shift_to_point(piece_loc, point) for piece_loc in piece
    ]
    return list(filter(fit_in_start_board_filter, shifted_pieces))


def where_fits_dict(board: set, all_pieces: list) -> dict:
    where_fits = defaultdict(list)

    for point in board:
        for piece in all_pieces:
            where_fits[(point, piece)] = piece_fit_in_starting_board(point, piece)

    return where_fits
