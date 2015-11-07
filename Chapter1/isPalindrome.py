#!/usr/bin/python

# Question 1.4

# Palindrome has even character counts except one character that can be odd

def isPalindrome(str):
	s=sorted(str.lower())
	oddCount=0
	charCount=1
	for i in xrange(1,len(s)):
		if(s[i]==s[i-1]):
			charCount+=1
		else:
			if(charCount%2==1 and s[i-1] != ' ' and s[i]!=' '):
				oddCount+=1
			charCount=1
	if(charCount%2==1): #take care of checking last letter
		oddCount+=1
	if oddCount > 1:
		return False
	else:
		return True

if __name__=="__main__":
	str = "Tact       C   o  a"
	str2="aabbcddd"
	print isPalindrome(str)
	print isPalindrome(str2)
