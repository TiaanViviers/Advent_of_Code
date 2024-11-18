import sys

def const_diff(seq):
    for num in seq:
        if (seq[0] - num) != 0:
            return False
    return True


def get_new_seq(seq):
    new_seq = []
    for i in range(len(seq)):
        if i != 0:
            new_seq.append(seq[i] - seq[i-1])

    return new_seq


def get_next(sequence, diff=None):
    if const_diff(sequence):
        return sequence, sequence[0]
    
    else:
        new_sequence = get_new_seq(sequence)
        adjusted_sequence, diff = get_next(new_sequence)

    return adjusted_sequence, sequence[0] - diff


def main():
    with open(sys.argv[1], 'r') as f:
        input = f.read()
    input = input.split('\n')
    
    sum = 0
    for i in input:
        sequence = [int(j) for j in i.split()]
        _, next_pred = get_next(sequence)
        sum += next_pred
    
    print(f"total sum: {sum}")


if __name__ == "__main__":
    main()