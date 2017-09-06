def odd_even(start,end):
    for i in range(start,end+1):
        if i%2 != 0:
            print "Number is", i,". This is an odd number."
        else:
            print "Number is", i,". This is an even number."

start = 1
end = 2000
odd_even(start,end)
