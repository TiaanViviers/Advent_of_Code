from sys import argv

fn main() raises:
    var f_name: StringRef = argv()[1]

    var input = String()
    with open(f_name, 'r') as file:
        input = file.read()

    var diffs: Int = get_diffs(input)
    print("Total differences: ", diffs)


fn get_diffs(input: String) raises -> Int:
    #split string on newline chars
    var temp: List[String] = input.split("\n")

    #split strings on whitespaces
    var formatted: List[List[String]] = List[List[String]]()
    for i in temp:
        formatted.append(i[].split())

    #create left and right lists to sort values
    var left: List[Int] = List[Int]()
    var right: List[Int] = List[Int]()
    for i in range(len(formatted)):
        left.append(atol(formatted[i][0]))
        right.append(atol(formatted[i][1]))
    
    #sort left and right lists
    sort(left)
    sort(right)

    #get diffs between left and right sorted lists
    var diffs = Int()
    for i in range(len(left)):
        diffs += abs(left[i] - right[i])

    return diffs