from sys import argv
from python import Python, PythonObject

fn main() raises -> None:
    with open(argv()[1], 'r') as f:
        input = f.read()
    
    print("Sum:", find_sum(input))


fn find_sum(input: String) raises -> Int:
    re = Python.import_module('re')

    var lines: List[String] = input.split('\n')
    var pattern: String = r"mul\((\d+),(\d+)\)"
    var matches: PythonObject
    var sum: Int = 0

    for line in lines:
        #Find all matches
        matches = re.findall(pattern, line[])
        sum += sum_matches(matches)
         
    return sum

fn sum_matches(matches: PythonObject) raises -> Int:
    #Perform the summation directly in Python
    var py_sum = Python.evaluate("lambda matches: sum(int(x[0]) * int(x[1]) for x in matches)")
    var sum = py_sum(matches)
    return int(sum)
