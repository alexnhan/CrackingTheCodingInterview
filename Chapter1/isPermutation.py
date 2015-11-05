#!/usr/bin/python

#Question 1.2

def isPermutation(str1,str2):
	s1=sorted(str1)
	s2=sorted(str2)
	if(s1==s2):
		return True
	else:
		return False

if __name__=="__main__":
	str1 = "fast"
	str2 = "tasf"
	print isPermutation(str1,str2)
