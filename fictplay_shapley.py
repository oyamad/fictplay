from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from fictplay import *

SAVEFILE = False
FILNENAME_BASE = 'fictplay_shapley'
# FILEFORMATS = ('png', 'svg', 'pdf')
FILEFORMAT = 'png'

SHAPLEY_GAME = [[(1, 0), (0, 0), (0, 1)],
                [(0, 1), (1, 0), (0, 0)],
                [(0, 0), (0, 1), (1, 0)]]

T = 250
T_0 = 0

g = NormalFormGame_2P(SHAPLEY_GAME)
players = FictitiousPlayUpdatingPlayers(g)
fp = FictitiousPlay(players)

x_vals, y_vals, z_vals = np.empty([2, T]), np.empty([2, T]), np.empty([2, T])
for t, beliefs in enumerate(fp(T)):
    x_vals[:, t] = [beliefs[player][0] for player in players.players]
    y_vals[:, t] = [beliefs[player][1] for player in players.players]
    z_vals[:, t] = [beliefs[player][2] for player in players.players]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)
ax.set_xticks((0, 0.25, 0.5, 0.75, 1))
ax.set_yticks((0.25, 0.5, 0.75))
ax.set_zticks((0, 0.25, 0.5, 0.75, 1))

colors = ['b', 'r']
for player, color in zip(players.players, colors):
    ax.scatter(x_vals[player][T_0:], y_vals[player][T_0:], z_vals[player][T_0:], c=color, s=60)
ax.view_init(ax.elev, ax.azim+90)
if SAVEFILE:
    TRANS = (FILEFORMAT.lower() in ['png', 'svc'])
    plt.savefig(FILNENAME_BASE + '.' + FILEFORMAT.lower(),
                transparent=TRANS, bbox_inches='tight', pad_inches=0)
plt.show()
