
def get_sum(input):
    num_map, sym_map = get_maps(input)

    #use sym_map to search for nums in num_map

#TODO fix building maps, switch to int iteration 
def get_maps(input):
    num_map = {}
    sym_map = {}
    cur_num = ''

    for row in input:
        for col in row:
            if col.isdigit():
                while col.isdigit():
                    cur_num += col
                    col += 1          #ERRROR!!! col is str cant add 1
            print(cur_num)



def main():
    f = open('subset.txt', 'r')
    input = f.read().split('\n')
    f.close()
    print(get_sum(input))


if __name__ == "__main__":
    main()