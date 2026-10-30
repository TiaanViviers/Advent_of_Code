from collections import Set

fn main() raises -> None:
    with open("input.txt", "r") as f:
        var data: String = f.read()
        (rules, orderings) = split_data(data)
        valid_orderings = verify_orderings(orderings, rules)
        result = calc_median_sum(valid_orderings)
        print(result)


fn calc_median_sum(orders: List[List[Int]]) -> Int:
    var med_sum = 0
    for order in orders:
        med_sum += median(order)
    
    return med_sum


fn median(arr: List[Int]) -> Int:
    if len(arr) % 2 == 0:
        print("Unexpected trouble in median")
    idx = len(arr) // 2
    return arr[idx]


fn verify_orderings(orderings: List[String], rules: List[String]) raises -> List[List[Int]]:
    var valid_orders = List[List[Int]]()
    var (unique_rules, rule_map) = build_rule_map(rules)
    var orders = format_orderings(orderings)

    for order in orders:
        valid_order = True
        for i in range(len(order)):
            if i == 0: continue
            idx = unique_rules.index(order[i])
            if not rule_map[idx].__contains__(order[i-1]):
                valid_order = False
                break
        if valid_order: valid_orders.append(order)

    return valid_orders


fn build_rule_map(rules: List[String]) raises -> (List[Int], List[Set[Int]]):
    rule_map = List[Set[Int]]()
    unique_rules = List[Int]()

    for rule in rules:
        left = Int(rule.split("|")[0])
        right = Int(rule.split("|")[1])
        if not left in unique_rules:
            unique_rules.append(left)
            rule_map.append({})
        if not right in unique_rules:
            unique_rules.append(right)
            rule_map.append({})

        right_idx = unique_rules.index(right)
        rule_map[right_idx].add(left)

    return unique_rules, rule_map


fn format_orderings(orderings: List[String]) raises -> List[List[Int]]:
    formatted_orderings = List[List[Int]]()

    for order in orderings:
        var str_temp = order.split(",")
        var int_order = List[Int]()
        for i in str_temp:
            int_order.append(Int(i))
        formatted_orderings.append(int_order)

    return formatted_orderings

    

fn split_data(data: String) raises -> (List[String], List[String]):
    var rules = List[String]()
    var orderings = List[String]()
    var lines = data.splitlines()

    var found_sep = False
    for line in lines:
        if line == "":
            found_sep = True
            continue
        if found_sep:
            orderings.append(String(line))
        else:
            rules.append(String(line))

    return (rules, orderings)
