import sys

def get_points(line):
    point = 0
    #split line into winning numbers / my numbers
    line = line.split("|")
    win_nums = line[0][7:].split()
    my_nums = line[1].split()

    for i in my_nums:
        if i in win_nums:
            point = increment_point(point)

    return point


def increment_point(point):
    if point == 0:
        return 1
    else:
        return point * 2


def main():
    points = 0
    for line in sys.stdin.readlines():
        points += get_points(line)

    print (points)

if __name__ == '__main__':
    main()