import random

class GameManager:
    def __init__(self):
        self.score = 0
        self.money = 5000
        self.bet = 0
        self.hand = []

    def calc_score(self):
        self.score = 0
        aces = 0

        ##For every card in hand
        for i in range(len(self.hand)):
            #Add rank to score
            self.score += clamp(self.hand[i].rank, 10)

            #Deal with aces later
            if self.hand[i].rank == 0:
                aces += 1
        #Dealing with aces
        for i in range(aces):
            if self.score + 11 > 21: #If Bust
                self.score += 1 #Only one
            else:
                self.score += 11 #11 if goated

    def draw(self, deck):
        self.hand.append(deck.pop( random.randint(0, len(deck))) ) # Pop a random entry from deck and add to hand.

    def print_hand(self):
        for i in self.hand:
            print(str(i), end= ", ")
        print("")


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


class CustomerService:
    def __init__(self):
        pass

def clamp(n, mmax):
    if n > mmax:
        return mmax
    return n

deck = []
GM = GameManager()

if __name__ == "__main__":
    for s in range(4):
        for r in range(14):
            deck.append(Card(s, r))

    GM.draw(deck)
    GM.draw(deck)
    GM.calc_score()
    GM.print_hand()
    print(GM.score)
