'''
Algo1 uses Weight - Length
Algo2 uses Weight/Length
'''
f=open('ScheduleInput.txt','r')
n=int(f.readline().strip())
wl=list()
for i in range(n):
	x,y=map(int,f.readline().strip().split())
	wl.append((x,y))
def Algo1():
	z=sorted(wl,key=lambda x:x[0],reverse=True)
	dif=list()

	for i in z:
		dif.append(i[0]-i[1])

	s=0
	le=0
	for i in range(n):
		x=max(dif)
		y=dif.index(x)
		le+=z[y][1]
		s+=z[y][0]*le
		del z[y]
		del dif[y]
	return s

def Algo2():
	rat=list()
	for i in wl:
		rat.append(i[0]/i[1])

	s=0
	le=0
	for i in range(n):
		x=max(rat)
		y=rat.index(x)
		le+=wl[y][1]
		s+=wl[y][0]*le
		del wl[y]
		del rat[y]
	return s
	
print(Algo1())
print(Algo2())

