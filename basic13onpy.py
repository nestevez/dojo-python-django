#Prints numbers from 1 to 255
def print_1_to_255():
    for number in range (1,256):
        print number

#Prints odd number from 1 to 255
def print_odds_1_to_255():
    for number in range(1,256,2):
        print number

#Print integers and sum of integers from 1 to 255
def print_ints_and_sum_0_to_255():
    tot = 0
    for number in range(1,256):
        tot += number
        print number, tot

#Iterates through a given array and prints each value
def print_array_vals(array):
    for number in array:
        print number

#Finds and prints max value in an array
def print_max_of_array(array):
    maxi = array[0]
    for number in array:
        if number > maxi:
            maxi = number
    print maxi

#Calculates and prints average of values in an array
def print_average_of_array(array):
    tot = 0
    for number in array:
        tot += number
    aver = tot / len(array)

#Creates an array with odd numbers from 1 to 255
def odd_array():
    array = []
    for number in range(1,256,2):
        array.append(number)
    print array

#Returns an array with the squared values of a given array
def square_array_vals(array):
    for number in range(0, len(array)):
        val = array[number]
        array[number] = val * val
    return array

#Counts numbers greater than Y
def greater_than_y(array,y):
    count = 0
    for number in array:
        if number > y:
            count += 1
    print count

#Returns the given array after setting any negative values to zero
def zero_out_array_negative_vals(array):
    for number in range(0, len(array)):
        if array[number] < 0:
            array[number] = 0
    return array

#Prints maximum, minimum and the average value for a list
def max_min_avg(array):
    maxi = array[0]
    mini = array[0]
    tot = 0
    for number in array:
        if number > maxi:
            maxi = number
        elif number < mini:
            mini = number
        tot += number
    aver = tot / len(array)
    print 'Max value is '+ str(maxi)
    print 'Min value is '+ str(mini)
    print 'Average value is '+str(aver)

#Moves all values in a given array forward by one index. Drops the first value and leaves a zero value at the end of the array.
def shift_array_vals_left(array):
    for number in range(0, len(array)-1):
        array[number] = array[number+1]
    array[len(array)-1] = 0
    return array

#Replaces any negative values in a given array with the string 'Dojo'
def swap_string_for_array_negative_vals(array):
    for number in range(0,len(array)):
        if array[number]<0:
            array[number] = 'Dojo'
    return array

array = [354,753453,75,655,45.546,345.465,-56,-2345,34,55,-4325]
y = 500

print swap_string_for_array_negative_vals(array)
