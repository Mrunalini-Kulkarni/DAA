#Python program to check two strings are anagrams

def check(a, b): 
	if(sorted(a)== sorted(b)):
		print("The strings are anagrams.") 
	else:
		print("The strings aren't anagrams.")		 
		
a = input("Enter the String")
b = input("Enter the String")
check(a, b)
