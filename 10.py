#Python program to check if an input year is a leap year

def check_year(year):
	if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
		return True 
	else:
		return False 

year = int(input("Enter the year:"))

if check_year(year):
	print("Leap Year")
else:
	print("Not a Leap Year")
