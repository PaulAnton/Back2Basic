def isPalindrome(aString):
    '''
    aString: a string
    '''
    # Your code here
    n=len(aString)
    if (n<=1):
        return True
    else:
        for i in range((n+1)/2):
            if aString[i]!=aString[n-i-1]:
                return False
        return True
        
