
l = ['magical unicorns',19,'hello',98.98,'world']
mixed = True
if (all(isinstance(n,int)for n in l)):
    print("The list you entered is of integer type")
    sum=0
    for i in l:
        sum+=i
    print "sum",sum
elif (all(isinstance(n,str)for n in l)):
    print("The list you entered is of string type")
    print "string", l
else:
    print("The list you entered is of mixed type")
    print "String:",
    sum=0
    strin=""
    for i in l:
        if type(i) is str:
            print i,
            continue
        else:
            sum+=i
    print("")
    print "Sum",sum
       
    