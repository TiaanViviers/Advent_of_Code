from sys import argv
from collections import Dict

fn main() raises:
    var f_name: StringRef = argv()[1]
    with open(f_name, 'r') as f:
        data = f.read()

    print("Similarity Score: ", get_sim_score(data))

fn get_sim_score(data: String) raises -> Int:
    var lines: List[String] = data.split('\n')

    var left: List[Int] = List[Int]()
    var right: List[Int] = List[Int]()
    for line in lines:
        var parts: List[String] = line[].split()
        left.append(atol(parts[0]))
        right.append(atol(parts[1]))

    var sim_dict = Dict[Int, Int]()
    var sim_score: Int = 0
    var num_occurences = Int()
    for i in range(len(left)):
        if left[i] in sim_dict:
            sim_score += sim_dict[left[i]]
        else:
            num_occurences = right.count(left[i])
            sim_dict[left[i]] = left[i] * num_occurences
            sim_score += left[i] * num_occurences
    
    return sim_score

