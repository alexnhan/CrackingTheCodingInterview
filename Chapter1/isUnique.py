#!/usr/bin/python

# Question 1.1
def isUnique(str):
	s=sorted(str);
	for i in range(1,len(s)):
		if(s[i]==s[i-1]):
			return False
	return True

if __name__ == "__main__":
	str = "hello"
	print isUnique(str)
