import sys
import math
from functools import reduce

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def lcm_multiple(numbers):
    return reduce(lcm, numbers)


def get_map(input):
    map = {}
    for i in input:
        location = i[:3]
        left = i[7:10]
        right = i[12:15]
        map.update({location: [left, right]})

    return map


def find_cycle_length(start_node, directions, nodes_map):
    visited_states = {}
    current_node = start_node
    direction_index = 0
    steps = 0
    
    while True:
        state = (current_node, direction_index)
        if state in visited_states:
            # Cycle detected
            cycle_length = steps - visited_states[state]
            return cycle_length
        else:
            visited_states[state] = steps
        
        # Move to the next node
        dir = directions[direction_index]
        next_node = nodes_map[current_node][0 if dir == 'L' else 1]
        
        current_node = next_node
        direction_index = (direction_index + 1) % len(directions)
        steps += 1


def get_steps(dirs, maps):
    start_nodes = [node for node in maps.keys() if node.endswith('A')]
    cycle_lengths = []

    for node in start_nodes:
        cycle_length = find_cycle_length(node, dirs, maps)
        cycle_lengths.append(cycle_length)

    return lcm_multiple(cycle_lengths)


def main():
    with open(sys.argv[1], 'r') as f:
        input = f.read()
    input = input.split('\n')

    dirs = input[0]
    map = get_map(input[2:])

    print(f"number of steps: {get_steps(dirs, map)}")


if __name__ == '__main__':
    main()