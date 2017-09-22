# import pprint.PrettyPrinter

class Card(object):
    def __init__(self, suit,value,string_val):
        self.suit = suit
        self.value = value
        self.string_val = string_val


    def __repr__(self):
        printout = "{} of {}".format(self.string_val,self.suit)
        return printout



class Deck(object):
    def __init__(self):
        self.cards=[]
        self.make_deck()


    def make_deck(self):
        string_val = ["joker","ace","two","three","four", "five", "six", "seven","eight", "nine", "ten", "jack", "queen", "king"]

        suits = ["spades","diamonds","clubs","hearts"]

        for suit in suits:
            for i in range(1,14):
                self.cards.append(Card(suit,i,string_val[i]))

        return self.cards


    def deal(self):
        return self.cards.pop()



class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []


    def draw(self,deck):
        self.hand.append(deck.deal())


    # def show_hand(self):




patrick = Player("Patrick")
dealer = Player("Dealer")
my_deck = Deck()


patrick.draw(my_deck)
dealer.draw(my_deck)
patrick.draw(my_deck)
dealer.draw(my_deck)

print patrick.hand
print dealer.hand
