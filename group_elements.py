def sgnf(x: str) -> int:
    return -2 * int(x.startswith('-')) + 1


index = {
    'x': 0,
    '-x': 0,
    'y': 1,
    '-y': 1,
    'z': 2,
    '-z': 2
}


def build_map(maps_to: str):
    val = maps_to.split(',')

    def a_function(t):
        return tuple(sgnf(v) * t[index[v]] for v in val)

    return a_function


MAP_TO_LIST = [
    "x,z,-y",
    "z,-x,-y",
    "-y,-x,-z",
    "z,y,-x",
    "y,z,x",
    "-z,-x,y",
    "-y,x,z",
    "y,-x,z",
    "z,x,y",
    "-z,x,-y",
    "-z,y,x",
    "-y,-z,x",
    "z,-y,x",
    "-z,-y,-x",
    "-x,-y,z",
    "y,-z,-x",
    "-y,z,-x",
    "x,-y,-z",
    "-x,z,y",
    "-x,-z,-y",
    "x,-z,y",
    "y,x,-z",
    "-x,y,-z",
    "x,y,z"
]


def create_all_mappings(map_to_list: list = MAP_TO_LIST) -> list:
    all_maps = []
    for map_to in map_to_list:
        all_maps.append(build_map(map_to))

    return all_maps
