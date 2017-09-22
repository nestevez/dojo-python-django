import random

def coin_toss(amt):
    ''' Simulates coin tosses for the given number of times and keeps cound of how many heads or tails have occured '''
    print "Starting the program..."
    heads = 0
    tails = 0
    for i in range(0,amt):
        coin = random.randint(0,1)
        if coin is 0:
            heads += 1
            print "Attempt #"+str(i+1)+": Throwing a coin... It's a head! ... Got",heads,"head(s) so far and",tails,"tail(s) so far"
        elif coin is 1:
            tails += 1
            print "Attempt #"+str(i+1)+": Throwing a coin... It's a tail! ... Got",heads,"head(s) so far and",tails,"tail(s) so far"
    print "Ending the program, thank you!"

amt = 5000
coin_toss(amt)
