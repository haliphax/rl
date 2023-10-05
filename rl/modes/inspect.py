"Inspection mode"

# local
from rl import g, t, echo


def inspect_mode():
    """
    Inspection mode.

    :rtype: str
    :returns: The next mode
    """

    iloc = g.charloc

    while True:
        last = tuple(iloc)
        transposed = (1 + g.view_dist + iloc[1] - g.charloc[1],
                      g.view_dist + iloc[0] - g.charloc[0])
        ichar = g.maptxt[iloc[1]][iloc[0]]
        iterr = g.terrain[ichar]
        iname = iterr[1]
        icolor = iterr[2]

        if iloc == g.charloc:
            # show character instead of terrain character is standing on
            ichar = '@'
            icolor = 'bold_white'
        elif g.fov[iloc[1] - g.top][iloc[0] - g.left] == 0:
            # don't show inspection data for spaces player can't see
            ichar = ' '
            iname = 'unseen'
            icolor = 'black'

        output = t.move(0, 0)
        output += '%s, %s Inspecting: %s%s' % (iloc[0], iloc[1], iname,
                                               t.clear_eol)
        output += t.move(transposed[0], transposed[1])
        output += getattr(t, '%s_on_red' % icolor)(ichar)
        echo(output)
        k = t.inkey()
        output = t.move(transposed[0], transposed[1])
        output += getattr(t, icolor)(ichar)
        echo(output)

        if k.code == t.KEY_ESCAPE or k == 'q':
            return True
        elif ((k.code == t.KEY_LEFT or k in ('4', 'h'))
                and iloc[0] - g.left > 0
                and abs(iloc[0] - g.charloc[0]) < g.view_dist):
            iloc = (iloc[0] - 1, iloc[1])
        elif ((k.code == t.KEY_RIGHT or k in ('6', 'l'))
                and iloc[0] < g.map_width - 1
                and g.right - iloc[0] > 1
                and abs(iloc[0] - g.charloc[0]) < g.view_dist):
            iloc = (iloc[0] + 1, iloc[1])
        elif ((k.code == t.KEY_UP or k in ('8', 'k'))
                and iloc[1] - g.top > 0
                and abs(iloc[1] - g.charloc[1]) < g.view_dist):
            iloc = (iloc[0], iloc[1] - 1)
        elif ((k.code == t.KEY_DOWN or k in ('2', 'j'))
                and iloc[1] < g.map_height - 1
                and g.bottom - iloc[1] > 1
                and abs(iloc[1] - g.charloc[1]) < g.view_dist):
            iloc = (iloc[0], iloc[1] + 1)

        # if they've moved beyond the view distance, move back
        if (abs(iloc[0] - g.charloc[0]) >= g.view_dist
                or abs(iloc[1] - g.charloc[1]) >= g.view_dist):
            iloc = tuple(last)
