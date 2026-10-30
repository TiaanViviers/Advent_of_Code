from sys import argv

fn main() raises -> None:
    with open(argv()[1], 'r') as f:
        input = f.read()
    
    print("Xmas count: ", find_x_mas(input))


fn find_x_mas(input: String) raises -> Int:
    var lines: List[String] = input.split("\n")
    var row_max: Int = len(lines)
    var col_max: Int = len(lines[0])
    var count = Int()

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == 'A' and is_x_mas(lines, i, j, row_max, col_max):
                count += 1

    return count

fn is_x_mas(ls:List[String], row:Int, col:Int, row_max:Int, col_max:Int) -> Int:
    var pos: Bool = False  #represents positive slope X leg (/)
    var neg: Bool = False  #represents negative slope X leg (\)

    if (row > 0) and (row < row_max-1) and (col > 0) and (col < col_max-1):
        #look for pos leg
        if ls[row+1][col-1] == "M" and ls[row-1][col+1] == "S":
            pos = True
        elif ls[row+1][col-1] == "S" and ls[row-1][col+1] == "M":
            pos = True

        #look for neg leg
        if ls[row+1][col+1] == "M" and ls[row-1][col-1] == "S":
            neg = True
        if ls[row+1][col+1] == "S" and ls[row-1][col-1] == "M":
            neg = True

    return neg and pos