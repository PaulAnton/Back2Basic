def longestRun(L):
	#print L
	maxstring=[]
	for i in range(len(L)):
		localstring=[L[0]]
		for j in range(len(L)-i-1):
			if L[i+j]<=L[i+j+1]:
				localstring=L[i:i+j+2]
			else:
				break
		if len(localstring)>len(maxstring):
			maxstring=localstring
	return len(maxstring)

L = [1, 0, 0, 0, 4, 5, 1, 2, 9, 4, -1, 0]
print longestRun(L)