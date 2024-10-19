import re

#possible if 12 red, 13 green, 14 blue


def valid_game_num(line):
    if is_valid_game(line):
        return int(get_num(line))
    return 0

def is_valid_game(line):
    #format input
    sets = line.split(';')
    sets = [sets[0].split(':')[1]] + sets
    #sets = [' 3 blue, 4 red',   ' 1 red, 2 green, 6 blue']

    for i in sets:
        r_num, g_num, b_num = parse_set(i)
        if r_num > 12 or g_num > 13 or b_num >14:
            return False
    return True

def parse_set(set):
    #red search
    red_pattern = rf'(\d+)\s+{'red'}'
    red_match = re.search(red_pattern, set)
    if red_match:
        red_num = int(red_match.group(1))
    else: red_num = 0

    #green search
    green_pattern = rf'(\d+)\s+{'green'}'
    green_match = re.search(green_pattern, set)
    if green_match:
        green_num = int(green_match.group(1))
    else: green_num = 0
    
    #blue search
    blue_pattern = rf'(\d+)\s+{'blue'}'
    blue_match = re.search(blue_pattern, set)
    if blue_match:
        blue_num = int(blue_match.group(1))
    else: blue_num = 0

    return red_num, green_num, blue_num



def get_num(line):
    num = ''
    game_info = line.split(':')[0]
    print(game_info)
    nums = re.findall(r'\d', game_info)
    while nums:
        num += nums.pop(0)
    return num

def main():
    sum = 0
    f = open('input.txt', 'r')
    for line in f:
        sum += valid_game_num(line.strip('\n'))
    print(sum)


if __name__ == "__main__":
    main()