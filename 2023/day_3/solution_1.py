
def get_sum(input):
    parts = []

    i = 0 
    while i < len(input):
        j = 0
        while j < len(input[i]):
            cur_num = ''
            while ord(input[i][j]) in range(48, 58):
                cur_num += input[i][j]
                #last element
                if (i == len(input)-1) and (j == len(input[i])-1):
                    break
                #increment row
                if i < len(input) - 1 and j == len(input[i]) - 1:
                    i += 1
                    j = 0
                #increment col
                if j < len(input[i]) - 1:
                    j += 1

            if cur_num:
                possible_part = Numbers(cur_num, i, j, len(input)-1, len(input[i])-1)
                neighbors = possible_part.get_neighbors()
                if valid_part(neighbors, input):
                    parts.append(int(cur_num))
            
        #increment iterators
            if j == len(input[i]) - 1:
                break
            else: j += 1
        if i == len(input)-1:
            break
        else: i += 1

    print(parts)
    return sum(parts)


def valid_part(neighbors, input):
    for row, col in neighbors:
        print(f"{row},  {col}")
        print(f"element: {input[row][col]}")
        if input[row][col] != '.':
            return True
        
    return False


def main():
    f = open('subset.txt', 'r')
    input = f.read().split('\n')
    f.close()
    print(get_sum(input))


class Numbers:
    def __init__(self, num, row, end_col, row_len, col_len):
        self.number = num
        self.row = row
        self.end_col = end_col
        self.start_col = end_col - len(num) + 1
        self.row_len = row_len
        self.col_len = col_len
        self.neighbors = self.get_neighbors()

    def get_neighbors(self):
        n = []
        print(f"start_col:{self.start_col}, end_col:{self.end_col}")
        #get top neighbors
        if self.row > 0:
            print(68)
            #top left corner
            if self.start_col > 0:
                n.append((self.row - 1, self.start_col - 1))
            #directly above
            j = self.start_col
            while j <= self.end_col:
                n.append((self.row - 1, j))
                j += 1
            #top right corner
            if self.end_col < self.row_len:
                n.append((self.row - 1, self.end_col + 1))

        #get inline neighbors
        if self.start_col > 0 and self.end_col < self.col_len:
            print(83)
            
            n.append((self.row, self.start_col - 1))
            n.append((self.row, self.end_col + 1))
        elif self.start_col > 0:
            print(87)
            n.append((self.row, self.start_col - 1))
        elif self.end_col < self.col_len:
            print(90)
            n.append((self.row, self.end_col + 1))
        
        #get bottom neighbors
        if self.row < self.row_len:
            print(f"self.row: {self.row}, self.row_len: {self.row_len}")
            print(95)
            #bottom left corner
            if self.start_col > 0:
                n.append((self.row + 1, self.start_col - 1))
            #directly below
            j = self.start_col
            while j <= self.end_col:
                n.append((self.row + 1, j))
                j += 1
            #bottom right corner
            if self.end_col < self.row_len:
                n.append((self.row + 1, self.end_col + 1))
        
        return n



if __name__ == "__main__":
    main()