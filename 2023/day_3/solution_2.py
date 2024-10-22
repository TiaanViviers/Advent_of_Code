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
        if top_nums:
            nums.append(top_nums)
    #find bottom neighboring nums
    if row < len(input) - 1:
        bottom_nums = get_outline_nums(row+1, col, input)
        if bottom_nums:
            nums.append(bottom_nums)
    #find inline neigbors
    inline_nums = get_inline_nums(row, col, input)
    for i in inline_nums:
        nums.append(i)

    #check that its a gear
    if len(nums) == 2:
        return nums[0] * nums[1]
    else: return 0


def get_outline_nums(row, col, input):
    cur_num = ''

    #num is directly above
    pass

    #num to left
    pass

    #num to right
    pass




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

    print(nums)
    return nums


def main():
    f = open('subset.txt', 'r')
    input = f.read().split('\n')
    f.close()
    print(get_sum(input))

if __name__ == "__main__":
    main()