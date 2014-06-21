from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from fictplay import *

SAVEFILE = True
FILNENAME_BASE = 'fictplay_RSP'
# FILEFORMATS = ('png', 'svg', 'pdf')
FILEFORMAT = 'png'

a, b = 1, 1
RSP = [[( 0,  0), (-b,  a), ( a, -b)],
       [( a, -b), ( 0,  0), (-b,  a)],
       [(-b,  a), ( a, -b), ( 0,  0)]]

T = 250
T_0 = 0

g = NormalFormGame_2P(RSP)
players = FictitiousPlayUpdatingPlayers(g)
fp = FictitiousPlay(players)

values = np.empty([2, 3, T])
for t, beliefs in enumerate(fp(T)):
    values[:, :, t] = beliefs

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
    ax.scatter(values[player][0][T_0:],
               values[player][1][T_0:],
               values[player][2][T_0:],
               c=color, s=60)
ax.view_init(ax.elev, ax.azim+90)
if SAVEFILE:
    TRANS = (FILEFORMAT.lower() in ['png', 'svc'])
    plt.savefig(FILNENAME_BASE + '.' + FILEFORMAT.lower(),
                transparent=TRANS, bbox_inches='tight', pad_inches=0)
plt.show()
