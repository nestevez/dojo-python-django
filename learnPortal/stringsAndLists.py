''' This program contains multiple functions which manipulate strings and lists. These functions include Find and Replace, Min and Max, First and Last, and New List '''
import string

#Find and Replace
def find_and_replace(str, word, repl):
    ''' Finds the given word (word) within the string (str) and replaces it with the second word (repl). Prints the index for the first appearance of the word and returns the new string with the replaced words '''
    pos = string.find(str,word) #finds first position of word in the string
    print "The first time", word, "appears in the string is at index", pos
    return string.replace(str, word, repl) #creates new string, replacing the word with the substitute

# stringy = "It's thanksgiving day. It's my birthday,too!"
# lookfor = 'day'
# replacewith = 'month'
#
# new_string = find_and_replace(stringy,lookfor,replacewith)
# print new_string


#Min and Max
def min_and_max(list):
    '''Prints the max and min values of a given list'''
    maxi = max(list) #finds max value
    mini = min(list) #finds min value
    print "The maximum value in the list is", maxi,"and the minimum value is", mini
    return

some = ['a',24,True,'rock',743]
# x = [2,54,-2,7,12,98]
# min_and_max(x)


#First and Last
def first_and_last(list):
    '''Prints the first and last values of a list and returns a list holding only the first and last values of the given list '''
    firsty = list[0] #first value in the list
    lasty = list[len(list)-1] #last value in the list
    print "The first and last values in the list are", firsty, "&", lasty
    return [firsty, lasty] #returns array of just the first and last values

# x = ["hello",2,54,-2,7,12,98,"world"]
# first_and_last(x)


#New list
def new_list(listy):
    '''Sorts the given list into ascending order, then creates a new list consisting of a list of half of the original list as the first value, and each remaining value in the original list as the other values in the list '''
    new_list = []
    listy.sort() #sorts list into ascending order
    half = len(listy)/2 #finds the halfway point of the original list
    new_list.append(listy[0:half]) #adds the first half of the list to the new list as a single value
    for i in range(half,len(listy)): #iterates through the rest of the original list values
        new_list.append(listy[i])
    return new_list

# x = [19,2,54,-2,7,12,98,32,10,-3,6]
# print new_list(x)
