import sys

def get_records(time, dist):
    num_solutions = 0
    factors = get_factors(time)

    for pair in factors:
        if pair[0] * pair[1] > dist:
            num_solutions += 1
    
    print(f"num solutions: {num_solutions}")
    return num_solutions


def get_factors(n):
    factors = []
    low = 1 ; high = n-1
    while high > 0:
        factors.append((low, high))
        high -= 1
        low += 1
    return factors


def main():
    with open(sys.argv[1], 'r') as f:
        input = f.read()
    times = [int(i) for i in input.split('\n')[0].split()[1:]]
    dists = [int(i) for i in input.split('\n')[1].split()[1:]]

    total = 1
    for i in range(len(times)):
        total *= get_records(times[i], dists[i])

    print(f"final answer: {total}")


if __name__ == "__main__":
    main()