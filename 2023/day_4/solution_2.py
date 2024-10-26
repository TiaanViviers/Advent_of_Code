import sys

def get_cards(input):
    #set up initial cardcount array
    card_counts = [1 for _ in range(len(input))]

    #dynamically update array of card counts
    for i in range(len(input)):
        matches = get_matches(input[i])
        card_counts = update_card_counts(card_counts, matches, i, i+1)

    return sum(card_counts)


def update_card_counts(counts_arr, num_matches, cur_idx, next_idx):
    while num_matches > 0:
        counts_arr[next_idx] += counts_arr[cur_idx]
        next_idx += 1
        num_matches -= 1

    return counts_arr


def get_matches(line):
    matches = 0
    #split line into winning numbers / my numbers
    line = line.split("|")
    win_nums = line[0][7:].split()
    my_nums = line[1].split()

    #determine if number is a winning number
    for i in my_nums:
        if i in win_nums:
            matches += 1

    return matches


def main():
    f = open(sys.argv[1])
    input = f.read()
    f.close()
    input = input.split('\n')
    print(get_cards(input))
    

if __name__ == '__main__':
    main()