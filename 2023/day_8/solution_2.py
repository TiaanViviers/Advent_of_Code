import sys

def get_map(input):
    map = {}
    for i in input:
        location = i[:3]
        left = i[7:10]
        right = i[12:15]
        map.update({location: [left, right]})

    return map


def get_start_nodes(maps):
    start_nodes = []
    for key in maps.keys():
        if key[2] == 'A':
            start_nodes.append(key)
    return start_nodes


def ends_Z(nodes):
    for node in nodes:
        if node[2] != 'Z':
            return False
    return True


def get_steps(dirs, maps):
    steps = 1
    nodes = get_start_nodes(maps)

    while True:
        dir = 0 if dirs[0] == "L" else 1
        
        for node in range(len(nodes)):
            nodes[node] = maps.get(nodes[node])[dir]

        if ends_Z(nodes): return steps
        steps += 1
        dirs = dirs[1:] + dirs[0]


def main():
    with open(sys.argv[1], 'r') as f:
        input = f.read()
    input = input.split('\n')

    dirs = input[0]
    map = get_map(input[2:])

    print(f"number of steps: {get_steps(dirs, map)}")


if __name__ == '__main__':
    main()