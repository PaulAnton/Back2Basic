def dict_invert(d):
	'''
	d: dict
	Returns an inverted dictionary according to the values mapping to list of keys
	'''
	newD=dict()
	for x in list(d.keys()):
		#print x,d[x]
		if d[x] in list(newD.keys()):
			newD[d[x]].append(x)
		else:
			newD[d[x]]=[x]
	for y in list(newD.keys()):
		newD[y]=sorted(newD[y])
	return newD

d = {1:10, 2:20, 3:30}
print dict_invert(d)
d = {1:10, 2:20, 3:30, 4:30}
print dict_invert(d)
d = {4:True, 2:True, 0:True}
print dict_invert(d)
print dict_invert({8: 6, 2: 6, 4: 6, 6: 6})
print dict_invert({30000: 30, 600: 30, 2: 10})
print dict_invert({0: 9, 9: 9, 5: 9})