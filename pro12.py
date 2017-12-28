a=int(input('Enter a number to check: \n'))
sum=0
n=a
while a!=0:
	remainder=a%10
	sum=sum*10+remainder
	a=a/10
if(sum==n):
	print('YES,It is a palindrome')
else:
	print('NO,It is not a palindrome')
