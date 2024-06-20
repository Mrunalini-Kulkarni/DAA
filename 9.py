#Python program to check if an input number is an Armstrong number

n=int(input("Enter the number")) 
s = n 
b = len(str(n))
sum = 0
while n != 0:
	r = n % 10
	sum = sum+(r**b)
	n = n//10
if s == sum:
	print("The given number", s, "is armstrong number")
else:
	print("The given number", s, "is not armstrong number")

