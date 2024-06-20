#Python  program to check if an input string is a palindrome

def isPalindrome(s):
	return s == s[::-1]

s = input("Enter the String")
ans = isPalindrome(s)

if ans:
	print("Yes")
else:
	print("No")
