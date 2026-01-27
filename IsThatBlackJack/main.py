class GameManager:
    def __init__(self):
        self.score = 0
        self.hand = []

    def calc_score(self):
        self.score = 0
        for i in range(len(self.hand)):
            self.score += 00
GM = GameManager()

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        suit = ""
        rank = ""

        if self.suit == 0:
            suit = "Spades"
        elif self.suit == 1:
            suit = "Clubs"
        elif self.suit == 2:
            suit = "Hearts"
        else:
            suit = "Diamonds"

        if self.rank == 11:
            rank = "Jack"
        elif self.rank == 12:
            rank = "Queen"
        elif self.rank == 13:
            rank = "King"
        elif self.rank == 0:
            rank = "Ace"
        else:
            rank = self.rank

        return f"{rank} of {suit}"

    def __add__(self, other):
        if self.rank == 0 and not other.rank == 0:
            if GM.score + 11 > 21:
                return 1 + clamp(other.rank, 10)
            else:
                return 11 + clamp(other.rank, 10)

        elif other.rank == 0 and not self.rank == 0:
            if GM.score + 11 > 21:
                return 1 + clamp(self.rank, 10)
            else:
                return 11 + clamp(self.rank, 10)

        elif self.rank == 0 and other.rank == 0:
            if GM.score + 12 > 21:
                return 2
            else:
                return 12
        return clamp(self.rank, 10) + clamp(other.rank, 10)



class CustomerService:
    def __init__(self):
        pass

def clamp(n, mmax):
    if n > mmax:
        return mmax
    return n

deck = []

if __name__ == "__main__":
    for s in range(4):
        for r in range(14):
            deck.append(Card(s, r))



