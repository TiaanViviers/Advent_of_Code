from sys import argv

fn main() raises:
    var f_name: StringRef = argv()[1]

    with open(f_name, 'r') as f:
        input = f.read()

    print("Number of Safe Reports: ", find_safe(input))


fn find_safe(input: String) raises -> UInt16:
    #split strings by newline char
    var lines: List[String] = input.split("\n")

    #split whitespaces in each line
    var reports = List[List[String]]()
    for line in lines:
        reports.append(line[].split())

    #find number of safe reports
    var safe: UInt16
    for report in reports:
        if is_monotonic(report[]) and is_safe_diff(report[]):
            safe += 1
    
    return safe

fn is_monotonic(report: List[String]) -> Bool:
    var max_idx: Int = len(report)

    #look for decreasing


    #look for increasing


fn is_safe_diff(report: List[String]) -> Bool:
    #get abs diff of each elem
    #check that   1 < abs diff > 3