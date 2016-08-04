def Karatsuba(num1,num2):
	if num1<10 or num2<10:
		return num1*num2

	# Calculate the size of the numbers
	m=max(len(str(num1)),len(str(num2)))
	m2=m/2

	# Split the digit sequence about the middle
	low1 = num1 / 10**(m2)
	high1 = num1 % 10**(m2)
	low2 = num2 / 10**(m2)
	high2 = num2 % 10**(m2)

	# 2 calls made to numbers approximately half the size
	z0=Karatsuba(low1,low2)
	z2=Karatsuba(high1,high2)
	z1=Karatsuba((low1+high1),(low2+high2))-z0-z2

	return z0*10**(2*m2)+z1*10**m2+z2

num1=12345
num2=6789
print Karatsuba(num1,num2)
