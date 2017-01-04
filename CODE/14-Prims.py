def Prims():
	f=open('PrimsInput.txt','r')
	nodes,edges=map(int,f.readline().strip().split())

	l=list()
	for i in range(edges):
		s,t,c=map(int,f.readline().strip().split())
		l.append((s,t,c))
	explored=[l[0][0]]

	s=0
	for i in range(nodes-1):
		next=list(filter(lambda x: (x[0] in explored and not x[1] in explored) or (not x[0] in explored and x[1] in explored),l))
		z=min(next,key=lambda t:t[2])
		s+=z[2]
		if z[0] in explored:
			explored.append(z[1])
		else:
			explored.append(z[0])
	print(s)

Prims()