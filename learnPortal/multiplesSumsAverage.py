''' This file contains four programs which print specific multiples, the sum of all values in a list and the average of values in a list'''

def print_odds(start,end):
    '''Prints all odd numbers within a given range '''
    for i in range(start,end+1):
        if(i%2 != 0):
            #checks if number is a multiple of 2 - if not, number is odd, and therefore printed
            print i

start = 1
end = 1000
multiple = 5

# print_odds(start,end)


def print_multiples(start,end,multiple):
    '''Prints numbers within a given range which are a multiple of the given number '''
    for i in range(start,end+1):
        if (i%multiple is 0): #checks if number is multiple and if true, prints
            print i

print_multiples (start,end,multiple)
