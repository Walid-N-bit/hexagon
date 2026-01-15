STATE = dict(position=(0, 0), direction="north", normal_mode=True)
PATH = []


def update_path(state: dict):
    pos = state.get("position")
    PATH.append(pos)
    return PATH


def update_mode(state: dict):
    is_normal = state.get("normal_mode")
    pos = state.get("position")
    is_visited = pos in PATH
    if is_visited:
        is_normal = not is_normal

    state.update({"normal_mode": is_normal})
    return state


def update_pos(state: dict):
    x, y = state.get("position")
    dir = state.get("direction")
    match dir:
        case "north":
            y += 1
        case "south":
            y -= 1
        case "east":
            x += 1
        case "west":
            x -= 1
    state.update({"position": (x, y)})
    return state


def turn_right(dir: str):
    match dir:
        case "north":
            dir = "east"
        case "south":
            dir = "west"
        case "east":
            dir = "south"
        case "west":
            dir = "north"
    return dir


def turn_left(dir: str):
    match dir:
        case "north":
            dir = "west"
        case "south":
            dir = "east"
        case "east":
            dir = "north"
        case "west":
            dir = "south"
    return dir


def change_dir(state: dict, direction: str):
    is_normal = state.get("normal_mode")
    dir = state.get("direction")
    if is_normal:
        if direction == "R":
            dir = turn_right(dir)
        elif direction == "L":
            dir = turn_left(dir)
    else:
        if direction == "R":
            dir = turn_left(dir)
        elif direction == "L":
            dir = turn_right(dir)
    state.update({"direction": dir})
    return state


def input_as_list(input: str | list):
    return [inp for inp in input]
    

def main():
    state = STATE
    print(STATE)
    input = "FFRFFRFFRFFFFRFFRFFRFFFFRFFRFFRFFFFRFFRFFRFFFFRFFRFFRFFFFRFFRFFRFFFFRFFRFFRFFFFRFFRFFRFFFFRFFRFFRFFFFRFFRFFRFFLFFL"
    input = input_as_list(input)
    for command in input:
        if command.upper() == "F":
            state = update_pos(state)
            PATH = update_path(state)
            state = update_mode(state)
        elif command.upper() in ["R", "L"]:
            state = change_dir(state, command.upper())
    print(PATH)


if __name__ == "__main__":
    main()
