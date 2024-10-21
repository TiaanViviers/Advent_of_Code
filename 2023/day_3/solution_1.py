
def get_sum(input):
    pass



def main():
    f = open('subset.txt', 'r')
    input = f.read().split('\n')
    f.close()
    print(get_sum(input))


class Numbers:
    def __init__(self, num, row, end_col, row_len):
        self.number = num
        self.row = row
        self.end_col = end_col
        self.start_col = end_col - len(num)
        self.row_len = row_len
        self.neighbors = self.get_neighbors()

    def get_neighbors(self):
        n = []
        #get top neighbors

        #get inline neighbors
        if self.start_col > 0 and self.end_col < self.row_len:
            n.append((self))
        #get bottom neighbors


if __name__ == "__main__":
    main()