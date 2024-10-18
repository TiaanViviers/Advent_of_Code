import re

nums_dict = {
        "zero": "0", "one": "1",
        "two": "2", "three": "3",
        "four": "4", "five": "5",
        "six": "6", "seven": "7",
        "eight": "8", "nine": "9"
    }

nums_keys = ['nine', 'eight', 'seven', 'six', 'five', 'four', 'three', 'two', 'one', 'zero']

def main():
    sum = 0
    with open('input.txt', 'r') as f:
        for line in f:
            print(line.strip('\n'))
            sum += get_calibration(line.strip('\n'))
    print(sum)

def get_calibration(line):
    digits = get_digits(line)
    print(digits)
    return int(digits[0] + digits[-1])


def get_digits(line):
    digits = []

    #8shoneight
    broken_arr = re.split(r'(\d)', line)
    #[8, shoneight]
    for i in broken_arr:
        if i.isdigit():
            digits.append(i)
        elif i in nums_keys:
            digits.append(nums_dict.get(i))

        else:
            j = 0
            while i:
                if nums_keys[j] in i:
                    digits.append(nums_dict.get(nums_keys[j]))
                    i = i.replace(nums_keys[j], "")
                
                j += 1
                
                if j > 9:
                    break



    

        

    return digits




if __name__ == "__main__":
    main()