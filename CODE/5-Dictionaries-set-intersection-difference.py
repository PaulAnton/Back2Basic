def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here
    keys1=set(d1.keys())
    keys2=set(d2.keys())
    inter=list(keys1 & keys2)
    diff=list((keys1 | keys2) - (keys1 & keys2))
    res1={}
    res2={}
    for i in inter:
        res1[i]=f(d1[i],d2[i])
    for i in diff:
        if i in list(d1.keys()):
            res2[i]=d1[i]
        else:
            res2[i]=d2[i]
    return (res1,res2)