import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
import numpy as np

# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import


def make_ax(grid=False):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.grid(grid)
    return ax


def piece_fill(piece):
    filled_piece = np.zeros((4, 4, 4))
    for c in piece:
        filled_piece[c] = 1
    return filled_piece


def show_solution(solution):
    cmap = plt.get_cmap('tab20')
    ax = make_ax(True)

    for i, piece in enumerate(solution):
        filled_piece = piece_fill(piece)
        color = cmap(i)[:-1] + (0.7,)
        ax.voxels(filled_piece, facecolors=color, edgecolors='gray')

    plt.show()
