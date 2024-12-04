from sys import argv

fn main() raises -> None:
    if not argv()[1]:
        print("Provide input file as command line argument")
        return

    with open(argv()[1], 'r') as f:
        input = f.read()
    
    print("Number of Safe Reports: ", find_safe(input))


fn find_safe(input: String) raises -> UInt16:
    #split strings by newline char
    var lines: List[String] = input.split("\n")

    #split whitespaces in each line
    var reports = List[List[Int]]()
    for line in lines:
        var nums = List[Int]()
        for part in line[].split():
            nums.append(atol(part[]))  # Convert to integer
        reports.append(nums)

    #find number of safe reports
    var safe: UInt16 = 0
    for report in reports:
        if is_safe_series(report[]) or dapener_safe(report[]):
            safe += 1

    return safe


fn dapener_safe(inout report: List[Int]) -> Bool:
    var temp = Int()
    for level in range(len(report)):
        temp = report.pop(level)
        if is_safe_series(report):
            return True
        report.insert(level, temp)
    
    return False


fn is_safe_series(report: List[Int]) -> Bool:
    var max_idx: Int = len(report) - 1

    var inc_safe = List[Int](1, 2, 3)
    var is_inc: Bool = True
    var i: Int = 1
    while i <= max_idx:
        if (report[i] - report[i-1]) not in inc_safe:
            is_inc = False
            break
        i += 1

    var is_dec: Bool = True
    var dec_safe = List[Int](-1, -2, -3)
    i = 1
    while i <= max_idx:
        if (report[i] - report[i-1]) not in dec_safe:
            is_dec = False
            break
        i += 1

    return is_dec or is_inc
    