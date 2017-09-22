def odd_even(start,end):
    ''' Prints each number in the range and indicates if the number is even or odd.'''
    for i in range(start,end+1):
        if i%2 != 0:
            print "Number is", i,". This is an odd number."
        else:
            print "Number is", i,". This is an even number."

# start = 0
# end = 2
# odd_even(start,end)


def multiply(listy,mult):
    '''Returns a list where each value has been multiplied by "mult" '''
    for i in range(0,len(listy)):
        listy[i] *= mult
    return listy

# a = [2,4,10,16]
# b = 5
# print multiply(a,b)


def layered_multiples(listy):
    '''Returns a two-dimensional list where each value is a list of 1's times the number in the original list. i.e., inputting [1,2,3] returns [[1],[1,1],[1,1,1]] '''
    new_array = []
    for val in listy:
        #creates a new list for each value in the original list
        internal = []
        for i in range(0,val):
            #adds 1s based on the value amount
            internal.append(1)
        new_array.append(internal) #adds the list to the final list
    return new_array

x = layered_multiples(multiply([2,4,5],3))
print x
