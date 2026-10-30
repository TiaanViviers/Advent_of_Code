def read_input():
    with open("day_2.txt", 'r') as f:
        data = f.read().split(",")
    return data

def invalid_ids(id_range):
   pass
    



if __name__ == "__main__":
    data = read_input()
    total = 0
    for id_range in data:
        total += invalid_ids(id_range)
    
    print(total)