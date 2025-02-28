"Pathfinding functions"

# stdlib
from heapq import heappush, heappop

# local
from . import g


def path_heuristic(a, b):
    "Heuristic for pathfinding algorithm"

    return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2


def path_find(start, goal):
    """
    A* pathfinding algorithm.

    https://code.activestate.com/recipes/578919-python-a-pathfinding-with-binary-heap/

    :param tuple start: The starting coordinates
    :param tuple goal: The coordinates of the goal
    :rtype: set
    :returns: A set of coordinates that make up the path
    """

    g.path_dest = goal

    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # (1, 1), (1, -1), (-1, 1), (-1, -1)] if we allowed moving diagonally...
    close_set = set()
    came_from = {}
    gscore = {start: 0}
    fscore = {start: path_heuristic(start, goal)}
    oheap = []
    heappush(oheap, (fscore[start], start))

    while oheap:
        current = heappop(oheap)[1]

        if current == goal:
            data = set([])

            while current in came_from:
                data.add(current)
                current = came_from[current]

            return data

        close_set.add(current)

        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j
            tentative_g_score = gscore[current] + path_heuristic(
                current, neighbor
            )

            if 0 <= neighbor[0] < g.map_width:
                if 0 <= neighbor[1] < g.map_height:
                    if g.terrain[g.maptxt[neighbor[1]][neighbor[0]]][0] > 0:
                        continue
                else:
                    # array bound y walls
                    continue
            else:
                # array bound x walls
                continue

            if neighbor in close_set and tentative_g_score >= gscore.get(
                neighbor, 0
            ):
                continue

            if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [
                i[1] for i in oheap
            ]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + path_heuristic(
                    neighbor, goal
                )
                heappush(oheap, (fscore[neighbor], neighbor))

    return set([])
