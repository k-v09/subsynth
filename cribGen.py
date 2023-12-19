import random

def SetDeck():
    sts = ['spades', 'clubs', 'hearts', 'diamonds']
    fcs = ['Jack', 'Queen', 'King']
    deck = []

    for card in range(10):
        for suit in sts:
            if card + 1 == 1:
                cname = "Ace of " + suit
            else:
                cname = str(card + 1) + " of " + suit
            deck.append(cname)
    for card in fcs:
        for suit in sts:
            fname = card + " of " + suit
            deck.append(fname)  
    return deck

# takes the deck as an argument
def Hands(d: list):
    h1 = []
    h2 = []
    for i in range(12):
        rcard = random.choice(d)
        d.remove(rcard)
        if i % 2 == 0:
            h1.append(rcard)
        elif i % 2 == 1:
            h2.append(rcard)
    return h1, h2

def GameLoop():
    p1, p2 = 0
    run = True
    while run:
        h1, h2 = Hands(SetDeck())
        run = False

if __name__ == "__main__":
    GameLoop()

