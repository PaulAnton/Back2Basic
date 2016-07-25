## Brute Force Method
## Complexity n*n
'''
def Inversions():
	inp=[]
	f=open('IntegerArray.txt')
	for line in f:
		inp.append(int(line))
	count=0
	for i in range(len(inp)-1):
		for j in range(i+1,len(inp)):
			if inp[i]>inp[j]:
				count+=1
	print count
	#7402905288

Inversions()
'''

## Divide and conquer 
## Complexity n log(n)
import math
def MergeAndCount(A,B):
	i=0
	j=0
	count=0
	output=[]
	while len(A)>0 and len(B)>0 and i<len(A) and j<len(B):
		if A[i]<=B[j]:
			output.append(A[i])
			i+=1
		else:
			output.append(B[j])
			count+=len(A)-i
			j+=1
	if len(A)==0 or i==len(A):
		for x in B[j:]:
			output.append(x)
	if len(B)==0 or j==len(B):
		for x in A[i:]:
			output.append(x)
	return (count,output)

def SortAndCount(L):
	if len(L)==1:
		return (0,L)
	else:
		a=int(math.ceil(len(L)/2))
		b=int(math.floor(len(L)/2))
		(cA,A)=SortAndCount(L[:a])
		(cB,B)=SortAndCount(L[b:])
		(c,L)=MergeAndCount(A,B)
	return (cA+cB+c,L)

L=[]
f=open('IntegerArray.txt')
for line in f:
	L.append(int(line))
print SortAndCount(L)[0]