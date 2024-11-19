import sys

def expand(arr):
    #expand cols


    #expand rows
    for i, row in enumerate(arr):
        if len(set(row)) == 1:
            arr.insert(i+1, ['.' for _ in range(len(row))])



def main():
    with open(sys.argv[1], 'r') as f:
        input = f.read()

    univ = expand(input.split('\n'))


if __name__ == '__main__':
    main()