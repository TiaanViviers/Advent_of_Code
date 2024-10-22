def main():
    f = open('input.txt', 'r')
    input = f.read().split('\n')
    f.close()
    print(get_sum(input))


def get_sum(input):
    parts = []
    new_line_flag = False
    
    i = 0
    row_max = len(input) - 1
    col_max = len(input[i]) - 1
    while i < len(input):
        j = 0
        while j < len(input[i]):
            cur_num = ''
            new_line_flag = False
            while ord(input[i][j]) in range(48, 58):
                cur_num += input[i][j]
                #new row
                if j == col_max and i < row_max:
                    i += 1
                    j = 0
                    new_line_flag = True
                    break
                #middle of row
                elif j < col_max:
                    j += 1
                if i >= row_max and j >= col_max:
                    break

            if cur_num and new_line_flag:
                if search_hit(i-1, col_max-len(cur_num)+1, col_max, input, col_max):
                    parts.append(int(cur_num))
            elif cur_num:
                if search_hit(i, j-len(cur_num), j-1, input, col_max):
                    parts.append(int(cur_num))
            
            j = j + 1 if not new_line_flag else 0
        i += 1

    return sum(parts)

def search_hit(row, col_start, col_end, input, col_max):
    #first row
    if row == 0:
        #first element in matrix
        if col_start == 0:
            #check right
            if is_sym(row, col_end+1, input): return True
            #check bottom
            while col_start <= col_end + 1:
                if is_sym(row+1, col_start, input): return True
                col_start += 1
        #last element in first row
        elif col_end == col_max:
            #check left
            if is_sym(row, col_start-1, input): return True
            #check bottom
            col_start -= 1
            while col_start <= col_end:
                if is_sym(row+1, col_start, input): return True
                col_start += 1
        #middle of first row
        else:
            #check left
            if is_sym(row, col_start-1, input): return True
            #check right
            if is_sym(row, col_end+1, input): return True
            #check bottom
            col_start -= 1
            while col_start <= col_end + 1:
                if is_sym(row+1, col_start, input): return True
                col_start += 1

    #last row
    elif row == len(input) - 1:
        #first element of last row
        if col_start == 0:
            #check right
            if is_sym(row, col_end+1, input): return True
            #check top
            while col_start <= col_end + 1:
                if is_sym(row-1, col_start, input): return True
                col_start += 1
        #last element in last row
        elif col_end == col_max:
            #check left
            if is_sym(row, col_start-1, input): return True
            #check top
            col_start -= 1
            while col_start <= col_end+1:
                if is_sym(row-1, col_start, input): return True
                col_start += 1
        #middle of last row
        else:
            #check left
            if is_sym(row, col_start-1, input): return True
            #check right
            if is_sym(row, col_end+1, input): return True
            #check top
            col_start -= 1
            while col_start <= col_end + 1:
                if is_sym(row-1, col_start, input): return True
                col_start += 1

    #middle of matrix
    else:
        #left side of middle
        if col_start == 0:
            #check right
            if is_sym(row, col_end+1, input): return True
            while col_start <= col_end + 1:
                #check top
                if is_sym(row-1, col_start, input): return True
                #check bottom
                if is_sym(row+1, col_start, input): return True
                col_start += 1
        #right side of middle
        elif col_end == col_max:
            #check left
            if is_sym(row, col_start-1, input): return True
            col_start -= 1
            while col_start <= col_end:
                #check top
                if is_sym(row-1, col_start, input): return True
                #check bottom
                if is_sym(row+1, col_start, input): return True
                col_start += 1
        #middle of middle:
        else:
            #check left
            if is_sym(row, col_start-1, input): return True
            #check right
            if is_sym(row, col_end+1, input): return True
            col_start -= 1
            while col_start <= col_end+1:
                #check top
                if is_sym(row-1, col_start, input): return True
                #check bottom
                if is_sym(row+1, col_start, input): return True
                col_start += 1
    
    return False


def is_sym(row, col, input):
    if input[row][col] != '.' and not input[row][col].isdigit():
        return True
    return False

if __name__ == "__main__":
    main()