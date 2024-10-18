nums_dict = {
        "zero": "0", "one": "1",
        "two": "2", "three": "3",
        "four": "4", "five": "5",
        "six": "6", "seven": "7",
        "eight": "8", "nine": "9"
    }

nums_keys = nums_dict.keys()
nums_vals = nums_dict.values()

def main():
    sum = 0

    f = open('input.txt', 'r')
    for line in f:
        sum += int(get_calibration(line))
    print(sum)

def get_calibration(line):
    digits = get_digits(line)
    num_digits = len(digits)
    if num_digits == 1:
        return digits[0] + digits[0]
    elif num_digits >= 3:
        return digits[0] + digits[-1]
    else:
        return digits[0] + digits[1]


def get_digits(line):
    digits = []
    cur_str = ''
    letter = ''

    for letter in line:
        letter = letter.lower()
        if letter in nums_vals:
            digits.append(letter)
            cur_str = ''
        else:
            cur_str += letter

        if cur_str in nums_keys:
            digits.append(nums_dict.get(cur_str))
            cur_str = ''

    return digits




if __name__ == "__main__":
    main()