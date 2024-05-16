def unlimitedParams(*arg):
    print(type(arg))
    print(arg)


unlimitedParams(1,2,3,4,5)
unlimitedParams()
#

def unlimitedNameParams(**arg):
    print(type(arg))
    print(arg)


unlimitedNameParams(a=1, b=90, c="apple")
unlimitedParams()
