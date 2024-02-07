##FOR LOOPS:
nums=[1,2,3,4,5]
for i in nums:
	print(i)

##break statements:break and continue
#break:if condition satisfies it breaks out of loops upto that point

nums=[1,2,3,4,5]
for i in nums:
	if i==3:
		print('Found:') 
		break
	print(i)
##result
#1
#2
#Found:

#continue:if condition satisfies it continues the loop but ignore the condition value
nums=[1,2,3,4,5]
for i in nums:
	if i==3:
		print('Found:') 
		continue
	print(i)
##result
#1
#2
#Found:
#4
#5
##
nums=[1,2,3,4,5]
for i in nums:
	for letter in 'abc': #it give 1a,1b,1c,2a,2b,2c etc
		print(i,letter)

##Range

for i in range(10):
	print(i)#it gives upto 10 from 1 but not 10

for i in range(2,10):#ranges from 2 to 9
	print(i)
print('WHILE')
#WHILE LOOPS:
x=0
while x<10:
	print(x)#IT INCREMENTS FROM 0 UNTILL IT SATISFIES THE CONDITION I.E 9
	x+=1
#BREAK
x=0
while x<10:
	if x==5:
		break
	print(x)
	x+=1

##infinite loop
x=0
while True:
	if x==5:
		break
		print(x)
		x+=1