import sys
from collections import Counter

CARD_RANKS = {'2': 2, '3': 3, '4': 4, '5': 5,
              '6': 6, '7': 7, '8': 8, '9': 9,
              'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}


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
    final.extend(sorted(high_cs))
    final.extend(sorted(one_ps))
    final.extend(sorted(two_ps))
    final.extend(sorted(three_ks))
    final.extend(sorted(f_houses))
    final.extend(sorted(four_ks))
    final.extend(sorted(five_ks))
    print(f"total winnings: {get_win(final)}")


class Camel_Card:
    def __init__(self, hand) -> None:
        self.cards = hand.split()[0]
        self.bid = int(hand.split()[1])
        self.hand_class = self.set_class()

    def set_class(self):
        counts = Counter(self.cards).values()
        counts = sorted(counts, reverse=True)

        if counts == [5]:
            return 'five_k'
        elif counts == [4, 1]:
            return 'four_k'
        elif counts == [3, 2]:
            return 'f_house'
        elif counts == [3, 1, 1]:
            return 'three_k'
        elif counts == [2, 2, 1]:
            return 'two_p'
        elif counts == [2, 1, 1, 1]:
            return 'one_p'
        elif counts == [1, 1, 1, 1, 1]:
            return 'high_c'
        else:
            print("Class set error")
    
    def __lt__(self, other):
        if self.hand_class != other.hand_class:
            raise ValueError("Different classes")

        self_ranks = [CARD_RANKS[card] for card in self.cards]
        other_ranks = [CARD_RANKS[card] for card in other.cards]

        # Compare the ranks one by one according to original order
        for self_rank, other_rank in zip(self_ranks, other_ranks):
            if self_rank != other_rank:
                return self_rank < other_rank
        return False
            
        
if __name__ == "__main__":
    main()