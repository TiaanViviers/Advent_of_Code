
def main():
    data = read_input()
    n_start = 50
    num_zeros = count_zeros(n_start, data)
    print(num_zeros)
    
    
def count_zeros(n, data):
    num_zeros = 0
    
    for line in data:
        if line.startswith("L"):
            n, num_zeros = apply_left(n, num_zeros, line[1:])
        else:
            n, num_zeros = apply_right(n, num_zeros, line[1:])
            
    return num_zeros


def apply_left(n, num_zeroes, str_clicks):
    clicks = int(str_clicks)
    
    while clicks > 0:
        if n > 0: n -= 1
        else: n = 99 
        clicks -= 1
        
        if n == 0:
            num_zeroes += 1
    
    return n, num_zeroes


def apply_right(n, num_zeroes, str_clicks):
    clicks = int(str_clicks)
    
    while clicks > 0:
        if n < 99: n += 1
        else: n = 0
        clicks -= 1
        
        if n == 0:
            num_zeroes += 1
    
    return n, num_zeroes
        

def read_input():
    with open("day_1.txt") as f:  # eg, day_1
        data = f.read()
        
    return data.split()


if __name__ == "__main__":
    main()
