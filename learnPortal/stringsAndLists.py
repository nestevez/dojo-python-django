''' This program contains multiple functions which manipulate strings and lists. These functions include Find and Replace, Min and Max, First and Last, and New List '''
import string

#Find and Replace
def find_and_replace(str, word, repl):
    pos = string.find(str,word)
    print "The first time", word, "appears in the string is at index", pos
    return string.replace(str, word, repl)

stringy = "It's thanksgiving day. It's my birthday,too!"
lookfor = 'day'
replacewith = 'month'

new_string = find_and_replace(stringy,lookfor,replacewith)
print new_string
