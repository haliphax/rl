"Main loop"

# local
from . import t, echo
from .modes import *  # pylint: disable=W0614
from .maps import load_map

# main loop
mode = 'move'
load_map('map')
echo(t.clear())
#path_found = path_find(charloc, (57, 5))
charloc = (0, 0)

with t.hidden_cursor(), t.cbreak():
    while mode:
        # dynamically call next mode
        next_mode = eval('%s_mode' % mode)()  # pylint: disable=W0123

        if next_mode is True:
            next_mode = last_mode

        last_mode = mode
        mode = next_mode
