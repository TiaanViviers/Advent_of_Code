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


def main():
    with open(sys.argv[1], 'r') as f:
        input = f.read()

    univ = expand(input.split('\n'))
    g_pos = get_galaxy_pos(univ)

    sum = 0
    for galaxy in g_pos:
        


if __name__ == '__main__':
    main()