def fits_in(a_piece: tuple, board: set) -> bool:
    return all(p in board for p in a_piece)


def add_tup(a: tuple, b: tuple) -> tuple:
    return tuple(x + y for x, y in zip(a, b))


def shift_to_point(piece: list, point: tuple) -> list:
    return tuple(add_tup(c, point) for c in piece)


def minus_tup(a: tuple, b: tuple) -> tuple:
    return tuple(x - y for x, y in zip(a, b))


def shift_cord_to_start(coordinates: list, start_c: tuple) -> list:
    return [minus_tup(c, start_c) for c in coordinates]


def remove_dublicates(piece: list) -> tuple:
    newpiece = []
    piece = [set(p) for p in piece]
    for p in piece:
        if p not in newpiece:
            newpiece.append(p)

    return tuple(tuple(p) for p in newpiece)
