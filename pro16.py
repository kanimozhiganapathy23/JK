a=int(input('Enter the value of lower limit: \n'))
b=int(input('Enter the value of higher limit: \n'))
count = 0
for i in range (a,b):
	for j in range (2,i):
		if(i%j==0):
			break
	else:
		print i
