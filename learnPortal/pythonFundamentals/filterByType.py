'''This program checks what type of object is the value given and performs different actions based on the type '''

def type_of_num(num):
    '''prints a message based on how large the number is'''
    if (num >= 100):
        print "That's a big number!"
    else:
        print "That's a small number"

def type_of_str(string):
    '''prints a message based on how long the string is'''
    if(len(string) >= 50):
        print "Long sentence"
    else:
        print "Short sentence"

def type_of_list(listy):
    '''prints a message based on how many values are in the list'''
    if(len(listy) >= 10):
        print "Big list!"
    else:
        print "Short list"


def type_check(item):
    '''Checks for the value's type and calls the appropriate function'''
    #lists all type options and their respective function names
    options = {'int':type_of_num,
    'float':type_of_num,
    'str':type_of_str,
    'list':type_of_list}
    #calls on the function based on the name of the type of the item
    options[type(item).__name__](item)

sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

type_check(spL)
