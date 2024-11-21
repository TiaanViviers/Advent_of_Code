import sys

def expand(arr):
    # Expand columns
    transpose = [''.join(col) for col in zip(*arr)]
    new_transpose = []
    for i, row in enumerate(transpose):
        new_transpose.append(row)
        if len(set(row)) == 1:
            new_transpose.append('.' * len(row))
    arr = [''.join(col) for col in zip(*new_transpose)]

    # Expand rows
    new_arr = []
    for i, row in enumerate(arr):
        new_arr.append(row)
        if len(set(row)) == 1:
            new_arr.append('.' * len(row))

    return new_arr


def get_galaxy_pos(arr):
    galaxies = []
    id = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == '#':
                galaxies.append(Galaxy(i, j, id))
                id += 1

    return galaxies


def get_distance(galaxies):
    considered = []
    dist = 0
    for i in galaxies:
        for j in galaxies:
            if i.id == j.id:
                continue
            elif (i.id, j.id) in considered or (j.id, i.id) in considered:
                continue
            else:
                dist += (abs(i.col - j.col) + abs(i.row - j.row))
                considered.append((i.id, j.id))
    
    return dist


def main():
    with open(sys.argv[1], 'r') as f:
        input = f.read()

    univ = expand(input.split('\n'))
    galaxies = get_galaxy_pos(univ)

    print(f"total distance: {get_distance(galaxies)}")
        

class Galaxy():
    def __init__(self, row, col, id) -> None:
        self.row = row
        self.col = col
        self.id = id


if __name__ == '__main__':
    main()