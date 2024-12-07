from sys import argv
from python import Python, PythonObject

fn main() raises -> None:
    with open(argv()[1], 'r') as f:
        input = f.read()

    print("Sum:", find_sum(input))


fn find_sum(input: String) raises -> Int:
    var re = Python.import_module('re')
    var sum = Int()
    var enabled: Bool = True

    var lines: List[String] = input.split("\n")
    for line in lines:
        sum += sum_line(enabled, line[], re)

    return sum


fn sum_line(inout enabled: Bool, inout line: String, re: PythonObject) raises -> Int:
    var pattern: String = r"mul\((\d+),(\d+)\)"
    var matches: PythonObject
    var idx = Int()
    var part = String()
    var sum = Int()

    while True:
        if enabled:
            idx = line.find("don't()")
            if idx == -1:
                matches = re.findall(pattern, line)
            else:
                part = line[:idx]
                matches = re.findall(pattern, part)

            sum += mul_matches(matches)
            
            if idx == -1:
                break
            else:
                enabled = False
                line = line[idx:]

        if not enabled:
            idx = line.find("do()")
            if idx == -1:
                break
            else:
                line = line[idx:]
                enabled = True

    return sum


fn mul_matches(matches: PythonObject) raises -> Int:
    #Perform the summation directly in Python
    var py_sum = Python.evaluate("lambda matches: sum(int(x[0]) * int(x[1]) for x in matches)")
    var sum = py_sum(matches)
    return int(sum)


