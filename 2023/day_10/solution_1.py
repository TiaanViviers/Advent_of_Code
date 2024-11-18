import sys

def get_steps(arr):
    steps = 0
    dir_1, dir_2, start_pos = get_start(arr)
    pos_1 = start_pos; pos_2 = start_pos[::]

    while True:
        #update positions
        pos_1[0], pos_1[1] = update_pos(dir_1, pos_1[0], pos_1[1])
        pos_2[0], pos_2[1] = update_pos(dir_2, pos_2[0], pos_2[1])

        steps += 1

        if pos_1 == pos_2:
            return steps
    
        #update dirs
        dir_1 = update_dir(arr, pos_1[0], pos_1[1], dir_1)
        dir_2 = update_dir(arr, pos_2[0], pos_2[1], dir_2)


def update_pos(dir, old_row, old_col):
    row = 0 ; col = 0
    if "N" in dir:
        row = -1
    elif "S" in dir: 
        row = 1
    if "E" in dir:
        col = 1
    elif "W" in dir:
        col = -1

    return old_row + row, old_col + col
        

def update_dir(arr, row, col, last_dir):
    last_dir = invert_dir(last_dir) #this is now direction we are coming from

    if arr[row][col] == '|':
        if "S" in last_dir: return 'N'
        elif "N" in last_dir: return 'S'
        else: print(f"update dir error in '|' for {last_dir}")

    elif arr[row][col] == '-':
        if "E" in last_dir: return 'W'
        elif "W" in last_dir: return "E"
        else: print(f"update dir error in '-' for {last_dir}")

    elif arr[row][col] == 'L':
        if 'N' in last_dir: return 'E'
        elif 'E' in last_dir: return 'N'
        else: print(f"update dir error in 'L' for {last_dir}")

    elif arr[row][col] == 'J':
        if 'N' in last_dir: return 'W'
        elif 'W' in last_dir: return 'N'
        else: print(f"update dir error in 'J' for {last_dir}")

    elif arr[row][col] == '7':
        if 'S' in last_dir: return 'W'
        elif 'W' in last_dir: return 'S'
        else: print(f"update dir error in '7' for {last_dir}")

    elif arr[row][col] == 'F':
        if 'S' in last_dir: return 'E'
        elif 'E' in last_dir: return 'S'
        else: print(f"update dir error in 'F' for {last_dir}")

    else:
        print(f"error in update_dir for element{arr[row][col]}")


def invert_dir(dir):
    if dir == 'N': return 'S'
    elif dir == 'E': return 'W'
    elif dir == 'S': return 'N'
    elif dir == 'W': return 'E'
    elif dir == 'NE': return 'SW'
    elif dir == 'NW': return 'SE'
    elif dir == 'SE': return 'NW'
    elif dir == 'SW': return 'NE'
    else: print(f"Inversion error for {dir}")


def get_start(arr):
    for i in range(len(arr)):
        col = arr[i].find("S")
        if col != -1:
            row = i
            break

    dirs = []
    if row > 0 and arr[row-1][col] in ('|', '7', 'F'):
        dirs.append("N")
    if row < len(arr) and arr[row+1][col] in ('|', 'L', 'J'):
        dirs.append('S')
    if col > 0 and arr[row][col-1] in ('-', 'L', 'F'):
        dirs.append('W')
    if col < len(arr[row]) and arr[row][col+1] in ('-', 'J', '7'):
        dirs.append('E')
    
    return dirs[0], dirs[1], [row, col]
    

def main():
    with open(sys.argv[1], 'r') as f:
        input = f.read()
    input = input.split('\n')

    print(f"steps to furthest point: {get_steps(input)}")


if __name__ == "__main__":
    main()