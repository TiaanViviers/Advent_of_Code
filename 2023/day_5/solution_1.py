import sys

def apply_mapping(seeds, mapping):
    mapping = mapping[1:]
    adjusted = [-1 for _ in range(len(seeds))]

    for line in mapping:
        line = line.split()
        line = [int(i) for i in line]
        
        destination_min = line[0]
        source_min = line[1]
        source_max = line[2] + source_min
        
        for i in range(len(seeds)):
            if adjusted[i] == -1:
                if seeds[i]>= source_min and seeds[i]<source_max:
                    adjusted[i] = destination_min + (seeds[i] - source_min)

    #unmapped elements
    for i in range(len(adjusted)):
        if adjusted[i] == -1:
            adjusted[i] = seeds[i]

    return adjusted


def main():
    seeds, maps = get_input()
    #apply all the mappings
    for mapping in maps:
        seeds = apply_mapping(seeds, mapping)
    
    #answer: seed that corresponds to smallest location number
    print(f"min location: {min(seeds)}")


def get_input():
    with open(sys.argv[1], 'r') as file:
        input = file.read()

    input = input.split('\n')
    seeds = input[0][7:].split(' ')
    seeds = [int(i) for i in seeds]
    maps = get_maps(input[2:])

    return seeds, maps


def get_maps(input):
    maps = []
    cur_map =[]

    for i in input:
        if i == '':
            if cur_map:
                maps.append(cur_map)
                cur_map = []
        else:
            cur_map.append(i)
    if cur_map:
        maps.append(cur_map)

    return maps


if __name__ == "__main__":
    main()