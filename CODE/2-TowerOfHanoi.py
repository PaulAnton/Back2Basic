def printMove(f,t):
	print("from location",f,"move to",t)

def Towers(n,a,b,c):
	if n==1:
		printMove(a,b)
	else:
		Towers(n-1,a,c,b)
		Towers(1,a,b,c)
		Towers(n-1,c,b,a)

a="TowerA"
b="TowerB"
c="TowerC"
n=int(input("Enter the number of rings"))
Towers(n,a,b,c)
