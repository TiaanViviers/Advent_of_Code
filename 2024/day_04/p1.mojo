from sys import argv

fn main() raises -> None:
    with open(argv()[1], 'r') as f:
        input = f.read()
    
    print("Xmas count: ", find_xmas(input))


fn find_xmas(input: String) raises -> Int:
    var lines: List[String] = input.split("\n")
    var row_max: Int = len(lines)
    var col_max: Int = len(lines[0])
    var count = Int()

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == 'X':
                count += count_xmas(lines, i, j, row_max, col_max)

    return count


fn count_xmas(ls: List[String], row: Int, col: Int, row_max: Int, col_max: Int) -> Int:
    var count = Int()
    var word = String()

    #up
    if row >= 3:
        word = ls[row-1][col] + ls[row-2][col] + ls[row-3][col]
        if word == "MAS": count += 1

    #down
    if row + 3 < row_max:
        word = ls[row+1][col] + ls[row+2][col] + ls[row+3][col]
        if word == "MAS": count += 1

    #left
    if col >= 3:
        word = ls[row][col-1] + ls[row][col-2] + ls[row][col-3]
        if word == "MAS": count += 1

    #right
    if col + 3 < col_max:
        word = ls[row][col+1] + ls[row][col+2] + ls[row][col+3]
        if word == "MAS": count += 1

    #up-left
    if (row >= 3) and (col >= 3):
        word = ls[row-1][col-1] + ls[row-2][col-2] + ls[row-3][col-3]
        if word == "MAS": count += 1

    #up-right
    if (row >= 3) and (col + 3 < col_max):
        word = ls[row-1][col+1] + ls[row-2][col+2] + ls[row-3][col+3]
        if word == "MAS": count += 1

    #down-left
    if (row + 3 < row_max) and (col >= 3):
        word = ls[row+1][col-1] + ls[row+2][col-2] + ls[row+3][col-3]
        if word == "MAS": count += 1

    #down-right
    if (row + 3 < row_max) and (col + 3 < col_max):
        word = ls[row+1][col+1] + ls[row+2][col+2] + ls[row+3][col+3]
        if word == "MAS": count += 1

    return count
