def getSublists(L, n):
	#print L,n
	newL=list()
	for i in range(len(L)-n+1):
		newL.append(L[i:i+n])
	return newL

L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
n=4
print getSublists(L,n)
L = [1, 1, 1, 1, 4]
n=2
print getSublists(L,n)