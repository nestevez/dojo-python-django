''' This program identifies the types of objects within a given list and prints a string identifying the types and some value or values associated with that type '''
#define the input
# l = ['magical unicorns',19,'hello',98.98,'world']
# l = [2,3,1,7,4,12]
# l = ['magical','unicorns']
# l = [True, False, False, True, True, True]
l = [[1,2],[3,4,5,6],[7,8,9,10]]

#initializing variables
num = False #check for number type
numsum = 0 #sum of number values
stri = False #check for string types
concatstr = '' #string concat holder
boolean = False #check for bool type
truct = 0 #count for true
falct = 0 #count for false
lists = False #check for list type

for val in l:
    #checks type of each value in the list and changes checks as necessary
    #performs whatever function is called for each type
    if isinstance(val, bool):
        boolean = True
        if val is True:
            truct += 1
        else:
            falct += 1
    elif isinstance(val,int) or isinstance(val, float):
        num = True
        numsum += val
    elif isinstance(val,str):
        stri = True
        concatstr += val+" "
    elif isinstance(val, list):
        lists = True

#counts how many types were found on the list and selects the proper type for the whole list
typect = 0
if num is True:
    typect +=1
    valtype = 'number'
if stri is True:
    typect +=1
    valtype = 'string'
if boolean is True:
    typect +=1
    valtype = 'bool'
if lists is True:
    typect +=1
    valtype = 'list'
if typect > 1:
    valtype = 'mixed'

#returns object holds the appropriate string to return based on the type of list
returns = {'number': "Sum: "+str(numsum),
'string': "String: "+concatstr,
'bool':"True count: "+str(truct)+", False count: "+str(falct),
'list': "Values count: "+str(len(l)),
'mixed': "Sum: "+str(numsum)+", String: "+concatstr+", True count: "+str(truct)+", False count: "+str(falct)+", Total Count: "+str(len(l))}

print "The list you entered is of", valtype, "type"
print returns[valtype]
