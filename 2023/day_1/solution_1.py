from re import findall

def main():
    sum = 0
    f = open('input_1.txt', 'r')
    for line in f:
        sum += int(get_calibration(line))
    print(sum)

def get_calibration(line):
    digits = findall(r"\d", line)
    num_digits = len(digits)
    if num_digits == 1:
        return digits[0] + digits[0]
    elif num_digits >= 3:
        return digits[0] + digits[-1]
    else:
        return digits[0] + digits[1]


if __name__ == "__main__":
    main()