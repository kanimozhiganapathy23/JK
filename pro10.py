input=int(input('Enter an integer\n'))
count=0
while(input>0):
	input = input//10
	count = count+1
print(count)
