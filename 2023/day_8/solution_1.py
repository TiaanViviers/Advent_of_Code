import sys

def get_map(input):
    map = {}
    for i in input:
        location = i[:3]
        left = i[7:10]
        right = i[12:15]
        map.update({location: [left, right]})

    return map


def get_steps(dirs, maps):
    steps = 1
    next_loc = 'AAA'

    while True:
        dir = 0 if dirs[0] == "L" else 1
        next_loc = maps.get(next_loc)[dir]

        if next_loc == "ZZZ":
            return steps
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