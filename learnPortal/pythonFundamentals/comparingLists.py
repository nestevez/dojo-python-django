''' This program compares two lists and prints a message based on whether or not the two lists are the same'''

def compare_lists(list_one, list_two):
    msg1 = "The lists are"
    if len(list_one) != len(list_two):
        #if two lists are not the same length they cannot be the same
        msg2 = "not the same"
    else:
        for i in range(0, len(list_one)):
            #checks each item in the list for equality
            if list_one[i] != list_two[i]:
                #if a single item in the lists don't match, the lists are not the same, so break out of the loop
                msg2 = "not the same"
                break
            else:
                msg2 = "the same"
    print msg1, msg2

# list_one = [1,2,5,6,2]
# list_two = [1,2,5,6,2]

# list_one = [1,2,5,6,5]
# list_two = [1,2,5,6,5,3]

# list_one = [1,2,5,6,5,16]
# list_two = [1,2,5,6,5]

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']

compare_lists(list_one,list_two)
