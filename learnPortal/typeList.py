
#define the input
# l = ['magical unicorns',19,'hello',98.98,'world']
# l = [2,3,1,7,4,12]
l = ['magical','unicorns']

num = False
numsum = 0
stri = False
concatstr = ''
boolean = False
truct = 0
falct = 0
lists = False

for val in l:
    if isinstance(val,int) or isinstance(val, float):
        num = True
        numsum += val
    elif isinstance(val,str):
        stri = True
        concatstr += val+" "
    elif isinstance(val, bool):
        boolean = True
        if val is True:
            truct += 1
        else:
            falct += 1
    elif isinstance(val, list):
        lists = True

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

returns = {'number': "Sum: "+str(numsum),
'string': "String: "+concatstr,
'bool':"True count: "+str(truct)+", False count: "+str(falct),
'list': "Values count: "+str(len(l)),
'mixed': "Sum: "+str(numsum)+", String: "+concatstr+", True count: "+str(truct)+", False count: "+str(falct)+", Total Count: "+str(len(l))}

print "The list you entered is of", valtype, "type"
print returns[valtype]
