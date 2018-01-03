a=int(input('Enter the lower limit: \n'))
b=int(input('Enter the upper limit: \n'))
for n in range (a,b):
	h=len(str(n))
	temp=n
	result=0
	while n>0:
		r=r%10
		result=result+r**h
		n=n/10
	if(temp==result):
		print(temp)
