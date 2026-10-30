def read_input():
    with open("day_3.txt", 'r') as f:
        data = f.read().split()
    return data

def max_joltage(bank):
    left, idx = get_max(bank[:-1])
    right, _ = get_max(bank[idx+1:])
    joltage = str(left) + str(right)
    print(f"bank: {bank}, left: {left}, idx: {idx}, right: {right}, joltage: {joltage}")
    
    return int(joltage)
    
    


def get_max(bank):
    cur_max = 0
    idx = 0
    
    for i, num in enumerate(bank):
        if int(num) > cur_max:
            cur_max = int(num)
            idx = i
    return cur_max, idx


if __name__ == "__main__":
    data = read_input()
    total = 0
    for bank in data:
        total += max_joltage(bank)
    
    print(total)