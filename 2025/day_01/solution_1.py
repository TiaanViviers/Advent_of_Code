
def main():
    data = read_input()
    n_start = 50
    num_zeros = count_zeros(n_start, data)
    print(num_zeros)
    
    
def count_zeros(n, data):
    num_zeros = 0 
    for line in data:
        if line.startswith("L"):
            n = apply_left(n, line[1:])
        else:
            n = apply_right(n, line[1:])
        if n == 0: 
            num_zeros += 1
    
    return num_zeros


def apply_left(n, num):
    tmp = n - int(num)
    
    while tmp < 0:
        tmp += 100
    n = tmp
    
    return n


def apply_right(n, num):
    tmp = n + int(num)
    
    while tmp > 99:
        tmp -= 100
    n = tmp
    
    return n

def read_input():
    with open("day_1.txt") as f:  # eg, day_1
        data = f.read()
        
    return data.split()


if __name__ == "__main__":
    main()
