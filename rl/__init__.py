"Main module"

# std
from sys import stdout

#: Blessed Terminal
t = None
#: Is x/84?
x84 = None

try:
    x84 = __import__(
        "x84.bbs",
        fromlist=(
            "getterminal",
            "echo",
        ),
    )
    t = x84.getterminal()
except ImportError:
    blessed = __import__("blessed", fromlist=("Terminal",))
    t = blessed.Terminal()


class g(object):
    "Global variables"

    #: map contents
    maptxt = []
    #: map height
    map_height = 0
    #: map width
    map_width = 0
    #: terrain definitions
    terrain = {}
    #: character location
    charloc = (42, 11)
    #: viewport top
    top = 0
    #: viewport left
    left = 0
    #: viewport bottom
    bottom = 0
    #: viewport right
    right = 0
    #: view distance from character's position
    view_dist = 35
    #: viewport height
    viewport_height = 23
    #: viewport width
    viewport_width = 80
    #: field of view
    fov = []
    #: pathfinding result
    path_found = set([])
    #: path destination
    path_dest = []
    #: viewport horizontal offset
    offset_x = min(view_dist, viewport_width // 2)
    #: viewport vertical offset
    offset_y = min(view_dist, viewport_height // 2)


def echo(txt):
    if x84:
        x84.echo(txt)
    else:
        stdout.write(txt)
        stdout.flush()
