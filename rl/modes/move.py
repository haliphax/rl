"Character movement mode"

# local
from rl import g, t, echo
from rl.fov import do_fov


def move_mode():
    """
    Character movement mode.

    :rtype: str
    :returns: The next mode
    """

    while True:
        output = t.move(0, 0)
        # display coords and current terrain
        output += '%s, %s %s%s\r\n' % (
            g.charloc[0], g.charloc[1],
            g.terrain[g.maptxt[g.charloc[1]][g.charloc[0]]][1],
            t.clear_eol)
        # viewport
        g.top = max(0, g.charloc[1] - g.view_dist)
        g.left = max(0, g.charloc[0] - g.view_dist)
        g.bottom = min(g.map_height - 1, g.charloc[1] + g.view_dist + 1)
        g.right = min(g.map_width - 1, g.charloc[0] + g.view_dist + 1)
        # leading vertical whitespace
        output += t.move(2, 0)
        output += (t.clear_eol + '\r\n') * (g.view_dist - g.charloc[1])
        # calculate field of vision
        do_fov()

        # draw the map in the viewport
        for y, line in enumerate(g.maptxt[g.top:g.bottom], start=g.top):
            output += t.clear_eol
            # leading horizontal whitespace
            output += ' ' * (g.view_dist - g.charloc[0])

            for x, char in enumerate(line[g.left:g.right], start=g.left):
                if (x, y) == g.charloc:
                    # character's position
                    output += t.bold_white('@')
                elif (x, y) in g.path_found:
                    output += t.bold_red('*')
                elif g.fov[y - g.top][x - g.left] == 1:
                    # visible
                    output += getattr(t, g.terrain[char][2])(char)
                else:
                    # not visible
                    output += ' '

            output += '\r\n'

        # trailing vertical whitespace
        output += \
            (t.clear_eol + '\r\n') * (g.charloc[1] + g.view_dist - g.map_height
                                      + 1)
        echo(output)

        # user input (move, etc.)
        k = t.inkey()
        k_low = k.lower()
        lastloc = g.charloc

        if k.code == t.KEY_ESCAPE or k_low == 'q':
            return False
        elif ((k.code == t.KEY_LEFT or k_low in ('4', 'h'))
              and g.charloc[0] > 0):
            g.charloc = (g.charloc[0] - 1, g.charloc[1])
        elif ((k.code == t.KEY_RIGHT or k_low in ('6', 'l'))
              and g.charloc[0] < g.map_width - 2):
            g.charloc = (g.charloc[0] + 1, g.charloc[1])
        elif ((k.code == t.KEY_DOWN or k_low in ('2', 'j'))
              and g.charloc[1] < g.map_height - 2):
            g.charloc = (g.charloc[0], g.charloc[1] + 1)
        elif ((k.code == t.KEY_UP or k_low in ('8', 'k'))
              and g.charloc[1] > 0):
            g.charloc = (g.charloc[0], g.charloc[1] - 1)
        elif k_low == 'i':
            return 'inspect'

        terrain = g.terrain[g.maptxt[g.charloc[1]][g.charloc[0]]]

        # if we've moved to a solid block, move back
        if terrain[0] > 0:
            terrain_name = terrain[1]
            output = t.move(1, 0)
            output += 'Your way is blocked by a(n) %s.%s' % (
                t.bold_white(terrain_name),
                t.clear_eol,
            )
            echo(output)
            g.charloc = lastloc
