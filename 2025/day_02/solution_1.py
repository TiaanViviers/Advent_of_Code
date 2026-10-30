def read_input():
    with open("day_2.txt", 'r') as f:
        data = f.read().split(",")
    return data

def invalid_ids(id_range):
    invalids = []
    
    left, right = id_range.split("-")
    ids = [i for i in range(int(left), int(right)+1)]
    
    for id in ids:
        if first_eq_sec(id):    # check if first half of id equal second half
            invalids.append(id)
    
    return sum(invalids)


def first_eq_sec(id):
    str_id = str(id)
    
    if len(str_id) % 2 != 0: 
        return False
    
    if str_id[0:int(len(str_id)/2)] == str_id[int(len(str_id)/2):]:
        return True
    
    return False
    



if __name__ == "__main__":
    data = read_input()
    total = 0
    for id_range in data:
        total += invalid_ids(id_range)
    
    print(total)