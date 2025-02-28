"Map functions"

# stdlib
from os.path import dirname, realpath, join

# local
from . import g


def load_map(name):
    """
    Load and parse a map. Map files are divided into two sections. First is
    the terrain definitions, and second is the map content. Terrain definitions
    use the following syntax::

        <char><solid><name>|<color>

    Where "solid" is 0 for open, 1 for solid, and 2 for transparent solid
    (does not block light, but cannot be occupied by the player).

    The terrain definitions and the map content are divided by a single blank
    line.

    :param str name: The name of the map to load
    """

    # parse the map file
    done_reading_terrain = False
    g.maptxt = []

    with open(
        join(dirname(realpath(__file__)), "mapfiles/%s.txt" % name)
    ) as mapfile:
        for line in mapfile.readlines():
            stripped = line.rstrip()

            # blank line separates terrain definitions from actual map contents
            if stripped == "" and not done_reading_terrain:
                done_reading_terrain = True
                continue

            if not done_reading_terrain:
                # read terrian definitions
                terrain_name, terrain_color = stripped[2:].split("|")
                g.terrain[stripped[0]] = (
                    int(stripped[1]),
                    terrain_name,
                    terrain_color,
                )
            else:
                # read map contents
                g.maptxt.append(stripped)

    g.map_height = len(g.maptxt)
    g.map_width = len(g.maptxt[0])
