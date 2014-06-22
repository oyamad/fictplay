from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from fictplay import *

# 0: Shapley game, 1: Rock-Paper-Scissors
GAME = 1

MULT_SUBPLOTS = True

SAVEFILE = True
FILNENAME_BASE = ('fictplay_shapley', 'fictplay_RPS')[GAME]
if MULT_SUBPLOTS:
    FILNENAME_BASE = FILNENAME_BASE + '_mult'
# FILEFORMATS = ('png', 'svg', 'pdf')
FILEFORMAT = 'png'

SHAPLEY_GAME = [[(1, 0), (0, 0), (0, 1)],
                [(0, 1), (1, 0), (0, 0)],
                [(0, 0), (0, 1), (1, 0)]]

a, b = 1, 1
RPS = [[ 0, -b,  a],
       [ a,  0, -b],
       [-b,  a,  0]]

games = (SHAPLEY_GAME, RPS)

T = (250, 150)[GAME]
T_0 = 0

g = NormalFormGame_2P(games[GAME])
players = FictitiousPlayUpdatingPlayers(g)
fp = FictitiousPlay(players)

values = np.empty([2, 3, T])
for t, beliefs in enumerate(fp(T)):
    values[:, :, t] = beliefs


def customize_ax(ax):
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_zlim(0, 1)
    ax.set_xticks((0, 0.25, 0.5, 0.75, 1))
    ax.set_yticks((0.25, 0.5, 0.75))
    ax.set_zticks((0, 0.25, 0.5, 0.75, 1))
    ax.set_aspect('equal')
    ax.view_init(ax.elev, ax.azim+90)


fig = plt.figure()
colors = ['b', 'r']

if MULT_SUBPLOTS:
    axes = []
    for player, color in zip(players.players, colors):
        axes.append(fig.add_subplot(1, 2, player+1, projection='3d'))
        axes[player].scatter(values[player][0][T_0:],
                             values[player][1][T_0:],
                             values[player][2][T_0:],
                             c=color, s=60)
        customize_ax(axes[player])
else:
    ax = fig.add_subplot(111, projection='3d')
    for player, color in zip(players.players, colors):
        ax.scatter(values[player][0][T_0:],
                   values[player][1][T_0:],
                   values[player][2][T_0:],
                   c=color, s=60)
    customize_ax(ax)

if SAVEFILE:
    TRANS = (FILEFORMAT.lower() in ['png', 'svc'])
    plt.savefig(FILNENAME_BASE + '.' + FILEFORMAT.lower(),
                transparent=TRANS, bbox_inches='tight', pad_inches=0)
plt.show()
