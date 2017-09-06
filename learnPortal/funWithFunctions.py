def odd_even(start,end):
    ''' Prints each number in the range and indicates if the number is even or odd.'''
    for i in range(start,end+1):
        if i%2 != 0:
            print "Number is", i,". This is an odd number."
        else:
            print "Number is", i,". This is an even number."

start = 0
end = 2
odd_even(start,end)


def multiply(listy,mult):
    '''Returns a list where each value has been multiplied by "mult" '''
    for i in range(0,len(listy)):
        listy[i] *= mult
    return listy

a = [2,4,10,16]
b = 5
print multiply(a,b)
