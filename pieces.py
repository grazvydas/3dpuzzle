from group_elements import create_all_mappings
from tools import shift_cord_to_start
from tools import remove_dublicates

ROTATION_MAPS = create_all_mappings()

# representatives for each piece
EQUIVALENT_CLASS_REPRESENTATIVES = [
    ((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1), (0, 0, 2)),
    ((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1), (0, -1, 0)),
    ((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 1)),
    ((0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 0, 1), (0, -1, 0)),
    ((0, 0, 0), (1, 0, 1), (0, 1, 0), (0, 0, 1), (0, 0, 2)),
    ((0, 0, 0), (1, 0, 2), (0, 1, 0), (0, 0, 1), (0, 0, 2)),
    ((0, 0, 0), (0, -1, 1), (0, 1, 0), (0, 0, 1), (0, 0, 2)),
    ((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 1, 1), (0, 1, 2)),
    ((0, 0, 0), (1, 0, 0), (0, 1, 0), (-1, 0, 0), (0, -1, 0)),
    ((0, 0, 0), (1, 0, 0), (0, 1, 0), (-1, 1, 0), (-1, 2, 0)),
    ((0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 0, 1)),
    ((0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 0, 1), (1, -1, 1)),
    ((0, 0, 0), (1, 0, 0), (0, 1, 0), (1, -1, 0), (1, -1, 1)),
]


def piece_is_connected(piece: list) -> bool:
    for cord in piece:
        found = False
        for cord_2 in piece:
            dist_tuple = tuple(abs(x - y) for x, y in zip(cord, cord_2))
            if max(dist_tuple) != 0 and min(dist_tuple) == 0:
                found = True
        if not found:
            return False
    return True


def rotate_piece(coordinates: list, a_map) -> tuple:
    return tuple(a_map(c) for c in coordinates)


def build_piece(def_coordinates: list) -> list:
    """rotate all possible ways and for each piece rotation
    generate all possible shifts that makes one of the coordinates equalt to
    (0, 0, 0)
     """
    full_piece = [rotate_piece(def_coordinates, a_map) for a_map in ROTATION_MAPS]
    full_piece = remove_dublicates(full_piece)
    final_piece = []
    for piece in full_piece:
        for c in piece:
            final_piece.append(shift_cord_to_start(piece, c))

    final_piece = remove_dublicates(final_piece)
    return final_piece


def all_pieces() -> list:
    return [
        build_piece(piece) for piece in EQUIVALENT_CLASS_REPRESENTATIVES
    ]


if __name__ == "__main__":
    count = [
        piece_is_connected(piece) for piece in EQUIVALENT_CLASS_REPRESENTATIVES
    ]

    print("Conneted piecies: {}/{}".format(sum(count), len(count)))

    piece_equivalent_classes = [
        build_piece(p) for p in EQUIVALENT_CLASS_REPRESENTATIVES
    ]

    for p in piece_equivalent_classes:
        print(len(p))
