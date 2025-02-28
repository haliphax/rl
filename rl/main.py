"Main loop"

# local
from . import g, t, echo
from .maps import load_map
from .modes import inspect_mode, move_mode
from .paths import path_find

# so ruff won't remove unused imports; these are used dynamically
(inspect_mode, move_mode)


def main():
    # main loop
    mode = "move"
    load_map("map")
    echo(t.clear())
    g.path_found = path_find(g.charloc, (26, 13))
    last_mode = "move"

    with t.hidden_cursor(), t.cbreak():
        while mode:
            # dynamically call next mode
            next_mode = eval("%s_mode" % mode)()

            if next_mode is True:
                next_mode = last_mode

            last_mode = mode
            mode = next_mode
