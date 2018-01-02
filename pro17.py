a=int(input('Enter the three digit number: \n'))
temp=a
result=0
while(temp!=0):
	remainder=temp%10
	result=result + remainder*remainder*remainder
	temp=temp/10
if(result==a):
	print('The given number is an amstrong number')
else:
	print('The given number is not an amstrong number')
