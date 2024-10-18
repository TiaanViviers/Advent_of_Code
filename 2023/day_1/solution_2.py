nums_dict = {
        "zero": "0", "one": "1",
        "two": "2", "three": "3",
        "four": "4", "five": "5",
        "six": "6", "seven": "7",
        "eight": "8", "nine": "9"
    }

nums_keys = nums_dict.keys()

def main():
    sum = 0
    with open('input.txt', 'r') as f:
        for line in f:
            sum += get_calibration(line.strip('\n'))
    print(sum)


def get_calibration(line):
    digits = get_digits(line)
    return int(digits[0] + digits[-1])


def get_digits(line):
    digits = []
    cur_str = ''

    for letter in line:
        letter = letter.lower()
        if letter.isdigit():
            digits.append(letter)
            cur_str = ''
        else:
            cur_str += letter

        for key in nums_keys:
            if cur_str.endswith(key):
                digits.append(nums_dict.get(key))
                break

    return digits


if __name__ == "__main__":
    main()