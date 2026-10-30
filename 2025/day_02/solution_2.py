def read_input():
    with open("day_2.txt", 'r') as f:
        data = f.read().split(",")
    return data


def invalid_ids(id_range):
    invalids = []
    
    left, right = id_range.split("-")
    ids = [i for i in range(int(left), int(right)+1)]
    
    for id in ids:
        if is_repeater(id):
            invalids.append(id)
    
    #print(f"invalid ids: {invalids}")
    return sum(invalids)
   

def is_repeater(id):
    str_id = str(id)
    factors = get_factors(len(str_id))
    
    for i in factors:
        if i == factors[0]: continue
        
        groups = split_id(i, str_id)
        if len(set(groups)) == 1:
            return True
    
    return False


def split_id(factor, str_id):
    part_length = len(str_id) // factor
    split_groups = [str_id[i : i + part_length] for i in range(0, len(str_id), part_length)]
    #print(f"id: {str_id}, factor: {factor}, split_group: {split_groups}")
    return split_groups
       

def get_factors(n: int) -> list[int]:
    if n <= 0:
        return []
        
    factors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)  # Add the matching factor pair
                    
    return sorted(list(factors))


if __name__ == "__main__":
    data = read_input()
    total = 0
    for id_range in data:
        total += invalid_ids(id_range)
    
    print(total)