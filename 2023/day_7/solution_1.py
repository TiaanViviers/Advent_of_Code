import sys

def sort(arr):
    pass


def get_win(arr):
    winnings = 0
    for i in range(len(arr)):
        winnings += arr[i].bid * (i+1)
    return winnings


def main():
    with open(sys.argv[1], 'r') as f:
        input = f.read()
    input = input.split('\n')

    five_ks = [] ; four_ks = [] ; f_houses = []
    three_ks = [] ; two_ps = [] ; one_ps = [] ; high_cs = []
    for hand in input:
        temp = Camel_Card(hand)
        if temp.hand_class == 'five_k':
            five_ks.append(temp)
        elif temp.hand_class == 'four_k':
            four_ks.append(temp)
        elif temp.hand_class == 'f_house':
            f_houses.append(temp)
        elif temp.hand_class == 'three_k':
            three_ks.append(temp)
        elif temp.hand_class == 'two_p':
            two_ps.append(temp)
        elif temp.hand_class == 'one_p':
            one_ps.append(temp)
        else:
            high_cs.append(temp)

    final = []
    final.extend(sort(high_cs))
    final.extend(sort(one_ps))
    final.extend(sort(two_ps))
    final.extend(sort(three_ks))
    final.extend(sort(f_houses))
    final.extend(sort(four_ks))
    final.extend(sort(five_ks))
    print(f"total winnings: {get_win(final)}")



class Camel_Card:
    def __init__(self, hand) -> None:
        self.cards = hand.split()[0]
        self.bid = int(hand.split()[1])
        self.hand_class = self.set_class()

    def set_class(self):
        c = self.cards
        if len(set(c)) == 1:
            return 'five_k'
        elif
        






if __name__ == "__main__":
    main()