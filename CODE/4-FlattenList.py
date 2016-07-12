def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    result=[]
    n=len(aList)
    for i in range(n):
        if type(aList[i])==type([]):
            result.extend(flatten(aList[i]))
        else:
            result.extend([aList[i]])
    return result