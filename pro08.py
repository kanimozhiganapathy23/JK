num = int(input('Enter a number: \n'))
if(num<0):
	print('Please Enter a positive number')
else:
	sum=0
	while(num>0):
		sum+=num
		num-=1
	print(sum)
