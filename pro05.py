number1=int(input('Enter the first number: \n'))
number2=int(input('Enter the second number: \n'))
number3=int(input('Enter the third number: \n'))
if(number1>number2) and (number1>number3):
	print('The first number is largest')
elif(number2>number1) and (number2>number3):
	print('The second number is largest')
else:
	print('The third number is largest')
