a=int(input('Enter the number to check: \n'))
count=0
for i in range (2,a):
	if(a%i==0):
		count = count+1
if(count==0):
	print('Yes, It is a prime number')
else:
	print('No, It is not a prime number')
