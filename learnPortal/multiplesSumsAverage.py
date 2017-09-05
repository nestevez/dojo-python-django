''' This file contains four programs which print specific multiples, the sum of all values in a list and the average of values in a list'''

def print_odds(start,end):
    '''Prints all odd numbers within a given range '''
    for i in range(start,end+1):
        if(i%2 != 0):
            #checks if number is a multiple of 2 - if not, number is odd, and therefore printed
            print i

start = 1
end = 1000

# print_odds(start,end)


def print_multiples(start,end,multiple):
    '''Prints numbers within a given range which are a multiple of the given number '''
    for i in range(start,end+1):
        if (i%multiple is 0): #checks if number is multiple and if true, prints
            print i

multiple = 5
# print_multiples (start,end,multiple)


def sum_list(listy):
    '''Prints the sum of all values in the given list'''
    valsum = 0
    for val in listy: #iterates through list, adding to the sum
        valsum += val
    print "The sum of all values in this list is",valsum

a = [1, 2, 5, 10, 255, 3]
sum_list(a)


def avg_list(listy):
    '''Prints the average of values in the given list'''
    #sums all values as per sum_list function
    valsum=0
    for val in listy:
        valsum += val
        #finds average by dividing sum by number of items in list
        avg=valsum/len(listy)
    print "The average of the values in this list is",avg

avg_list(a)
