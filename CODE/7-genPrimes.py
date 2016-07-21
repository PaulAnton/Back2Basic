def genPrimes():
	n=2
	pList=[]
	flag=False
	while True:
		if n==2:
			yield n
			pList.append(n)
		for x in pList:
			if n%x==0:
				flag=False
				break
			else:
				flag=True
		if flag:
			yield n
			pList.append(n)
		n+=1

y=genPrimes()
for i in range(10):
	print y.next()	
