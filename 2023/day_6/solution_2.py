import sys

def get_records(time, dist):
    num_solutions = 0
    factors = get_factors(time)

    for pair in factors:
        if pair[0] * pair[1] > dist:
            num_solutions += 1
    
    return num_solutions


def get_factors(n):
    factors = []
    low = 1 ; high = n-1
    while high > 0:
        factors.append((low, high))
        high -= 1
        low += 1
    return factors


def formatter(arr):
    str = ''
    for i in arr:
        str += i
    return int(str)


def main():
    with open(sys.argv[1], 'r') as f:
        input = f.read()
    time = formatter(input.split('\n')[0].split()[1:])
    dist = formatter(input.split('\n')[1].split()[1:])
    total = get_records(time, dist)

    print(f"final answer: {total}")


if __name__ == "__main__":
    main()