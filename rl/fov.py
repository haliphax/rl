"Field of view functions"

from . import g


def do_fov():
    """
    Calculate field of vision from the character's current location. Uses
    Bjorn Bergstrom's recursive shadowcasting algorithm.

    http://www.roguebasin.com/index.php?title=Python_shadowcasting_implementation
    """

    # multipliers for transforming coords to other octants
    mult = [
        [1, 0, 0, -1, -1, 0, 0, 1],
        [0, 1, -1, 0, 0, -1, 1, 0],
        [0, 1, 1, 0, 0, -1, -1, 0],
        [1, 0, 0, 1, -1, 0, 0, -1],
    ]

    g.fov = []

    for _ in range(g.view_dist * 2 + 1):
        fovrow = []

        for _ in range(g.view_dist * 2 + 1):
            fovrow.append(0)

        g.fov.append(fovrow)

    def cast_light(cx, cy, row, start, end, xx, xy, yx, yy):
        "Recursive lightcasting function"

        if start < end:
            return

        radius_squared = g.view_dist * g.view_dist

        for j in range(row, g.view_dist + 1):
            dx, dy = -j - 1, -j
            blocked = False

            while dx <= 0:
                dx += 1
                # Translate the dx, dy coordinates into map coordinates:
                X, Y = cx + dx * xx + dy * xy, cy + dx * yx + dy * yy

                if (
                    Y < g.top
                    or Y < 0
                    or Y > g.bottom
                    or Y >= g.map_height
                    or X < g.left
                    or X < 0
                    or X > g.right
                    or X >= g.map_width
                ):
                    continue

                # l_slope and r_slope store the slopes of the left and right
                # extremities of the square we're considering:
                l_slope, r_slope = (
                    (dx - 0.5) / (dy + 0.5),
                    (dx + 0.5) / (dy - 0.5),
                )

                if start < r_slope:
                    continue
                elif end > l_slope:
                    break
                else:
                    # Our light beam is touching this square; light it:
                    if dx * dx + dy * dy < radius_squared:
                        g.fov[Y - g.top][X - g.left] = 1

                    if blocked:
                        # we're scanning a row of blocked squares:
                        if g.terrain[g.maptxt[Y][X]][0] == 1:
                            new_start = r_slope
                            continue
                        else:
                            blocked = False
                            start = new_start
                    elif g.terrain[g.maptxt[Y][X]][0] == 1 and j < g.view_dist:
                        # This is a blocking square, start a child scan:
                        blocked = True
                        cast_light(
                            cx, cy, j + 1, start, l_slope, xx, xy, yx, yy
                        )
                        new_start = r_slope

            # Row is scanned; do next row unless last square was blocked:
            if blocked:
                break

    for octant in range(8):
        cast_light(
            g.charloc[0],
            g.charloc[1],
            1,
            1.0,
            0.0,
            mult[0][octant],
            mult[1][octant],
            mult[2][octant],
            mult[3][octant],
        )
