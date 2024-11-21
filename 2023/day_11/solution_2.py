import sys
from itertools import combinations

def get_weight(arr):
    weight = 1_000_000
    #get row weights
    row_w = {}
    for i in range(len(arr)):
        if len(set(arr[i])) == 1:
            row_w.update({i: weight})
        else:
            row_w.update({i: 1})

    #get col weights
    col_w = {}
    transpose = [''.join(col) for col in zip(*arr)]
    for j in range(len(transpose)):
        if len(set(transpose[j])) == 1:
            col_w.update({j: weight})
        else:
            col_w.update({j: 1})
    
    return row_w, col_w


def get_galaxy_pos(arr):
    galaxies = []
    id = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == '#':
                galaxies.append(Galaxy(i, j, id))
                id += 1

    return galaxies


def get_distance(galaxies, row_w, col_w):
    dist = 0
    for g1, g2 in combinations(galaxies, 2):
        d = weighted_dist((g1.row, g2.row), (g1.col, g2.col), row_w, col_w)
        dist += d
    return dist


def weighted_dist(rows, cols, row_w, col_w):
    r1, r2 = rows
    c1, c2 = cols
    dist = 0

    #step direction
    r_step = 1 if r2 > r1 else -1
    c_step = 1 if c2 > c1 else -1

    #along rows
    current_row = r1
    while current_row != r2:
        next_row = current_row + r_step
        dist += row_w[next_row]
        current_row = next_row

    #along columns
    current_col = c1
    while current_col != c2:
        next_col = current_col + c_step
        dist += col_w[next_col]
        current_col = next_col

    return dist


def main():
    with open(sys.argv[1], 'r') as f:
        input = f.read()

    input = input.split('\n')
    row_w, col_w = get_weight(input)
    galaxies = get_galaxy_pos(input)

    print(f"total distance: {get_distance(galaxies, row_w, col_w)}")
        

class Galaxy():
    def __init__(self, row, col, id) -> None:
        self.row = row
        self.col = col
        self.id = id


if __name__ == '__main__':
    main()