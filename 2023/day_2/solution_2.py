import re

def get_power(line):
    #format input
    sets = line.split(';')
    sets = [sets[0].split(':')[1]] + sets

    r_max = 0 ; g_max = 0 ; b_max = 0
    for i in sets:
        r_num, g_num, b_num = parse_set(i)
        r_max = r_num if r_num > r_max else r_max
        g_max = g_num if g_num > g_max else g_max
        b_max = b_num if b_num > b_max else b_max
    return r_max * g_max * b_max

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


def main():
    sum = 0
    f = open('input.txt', 'r')
    for line in f:
        sum += get_power(line.strip('\n'))
    print(sum)


if __name__ == "__main__":
    main()