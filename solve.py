import pieces
from board import generate_the_board
from board import where_fits_dict
from board import number_of_neighboars
from tools import fits_in
import time

the_board = generate_the_board()
all_pieces = pieces.all_pieces()
where_could_fit = where_fits_dict(the_board, all_pieces)


def greedy_search_in_the_graph(board: set, unused_pieces: list, answer: list) -> list:

    if len(board) == 0:
        return answer

    # TODO add here some simple heuristic branch check in case it takes too much
    # time

    # choose most demanding cell in the board
    sorted_board_cells = sorted(
        [(number_of_neighboars(board, cell), cell) for cell in board]
    )
    cell = sorted_board_cells[0][1]

    # for piece in unused pieces:
    for piece in unused_pieces:
        # for each piece position in space that could fit in the board (empty)
        for possible_piece_position in where_could_fit[(cell, piece)]:
            # if piece position in space fits current board then
            if fits_in(possible_piece_position, board):
                # update
                updated_board = board.difference(set(possible_piece_position))
                updated_unused_pieces = unused_pieces[:]
                updated_unused_pieces.remove(piece)
                updated_answer = answer + [possible_piece_position]

                # go in further in the branch
                result = greedy_search_in_the_graph(
                    updated_board,
                    updated_unused_pieces,
                    updated_answer
                )
                if result:
                    return result

    return []


if __name__ == '__main__':
    print("Solving puzzle...")
    start_time = time.time()
    A = greedy_search_in_the_graph(the_board, all_pieces, [])
    it_took = time.time() - start_time
    print(f"Solving is done. It took {it_took:0.1f} seconds")
    if A != []:
        print('Solution found:')
        for piece in A:
            print(piece)
