def get_sum(input):
    sum = 0
    
    #find position of all '*'
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == '*':
                sum += get_gear_ratio(i, j, input)
                
    return sum

def get_gear_ratio(row, col, input):
    nums = []

    #find top neighboring nums
    if row > 0:
        top_nums = get_outline_nums(row-1, col, input)
        for t in top_nums:
            nums.append(t)
    #find bottom neighboring nums
    if row < len(input) - 1:
        bottom_nums = get_outline_nums(row+1, col, input)
        for b in bottom_nums:
            nums.append(b)
    #find inline neigbors
    inline_nums = get_inline_nums(row, col, input)
    for i in inline_nums:
        nums.append(i)

    #check that its a gear
    if len(nums) == 2:
        return nums[0] * nums[1]
    else: return 0


def get_outline_nums(row, col, input):
    nums = []
    row_str = input[row]
    col_len = len(row_str)

    # Helper function to expand left and right from a given starting index
    def expand_number(start):
        left = start
        right = start

        # Expand to the left as long as there are digits
        while left > 0 and row_str[left - 1].isdigit():
            left -= 1
        # Expand to the right as long as there are digits
        while right < col_len - 1 and row_str[right + 1].isdigit():
            right += 1
        return row_str[left:right + 1], right

    # Check if the current position is part of a number
    if row_str[col].isdigit():
        num, end = expand_number(col)
        nums.append(int(num))
        col = end

    # Check left and right neighbors for additional numbers if the center isn't a digit
    else:
        if col > 0 and row_str[col - 1].isdigit():
            num, _ = expand_number(col - 1)
            nums.append(int(num))
        if col < col_len - 1 and row_str[col + 1].isdigit():
            num, _ = expand_number(col + 1)
            nums.append(int(num))

    return nums

def get_inline_nums(row, col, input):
    nums = []
    cur_num = ''
    #look left
    l = 1
    while input[row][col-l].isdigit() and col >= 0:
        cur_num = input[row][col-l] + cur_num
        l += 1
    if cur_num:
        nums.append(int(cur_num))
        cur_num = ''

    #look right
    r = 1
    while input[row][col+r].isdigit() and col <= len(input[row])-1:
        cur_num += input[row][col+r]
        r += 1
    if cur_num:
        nums.append(int(cur_num))

    return nums


def main():
    f = open('input.txt', 'r')
    input = f.read().split('\n')
    f.close()
    print(get_sum(input))

if __name__ == "__main__":
    main()
    """input = [
        '..234..',
        '.123...',
        '...345.',
        '012....',
        '612.456'
    ]

    print(get_outline_nums(0, 3, input))  # Output: [234]
    print(get_outline_nums(1, 3, input))  # Output: [123]
    print(get_outline_nums(2, 3, input))  # Output: [345]
    print(get_outline_nums(3, 4, input))  # Output: []
    print(get_outline_nums(4, 3, input))  # Output: [12, 456]"""