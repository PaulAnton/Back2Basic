def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a==0:
        return b
    elif b==0:
        return a
    elif a==b:
        return a
    elif a<b:
        return gcdRecur(a,b%a)
    else:
        return gcdRecur(b,a%b)