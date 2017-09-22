
import string

def find_character(listy, char):
    ''' Takes a list of strings and a character and returns a new list of strings containing the character '''
    new_list = []
    for val in listy:
        #checks each value in the list for the character
        pos = string.find(val, char)
        if pos != -1:
            #if the character is in any position in the string, add the string to the new list
            new_list.append(val)
    print "new_list =", new_list
    return new_list

word_list = ['hello','world','my','name','is','Anna']
char = 'o'

find_character(word_list, char)
