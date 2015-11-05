#!/usr/bin/python

# Question 1.3

def memmove(str, dest, src):
	for i in range(abs(dest-src)):
		str.append(' ');
	if dest > src: # memmove implementation when dest > src
		for i in range(len(str)-1,dest-1,-1):
			str[i]=str[i-(abs(dest-src))]

def urlify(str):
	s=list(str)
	for i in xrange(len(s)):
		if s[i]==' ':
			s[i]='%'
			memmove(s,i+3,i+1)
			s[i+1]='2'
			s[i+2]='0'
	return "".join(s)
		
if __name__=="__main__":
	s = "Mr John Smith"
	# Long way to do it
	a=urlify(s)
	# Quick and dirty way to do it
	s1=list(s)
	for i in xrange(len(s1)):
		if s1[i]==' ':
			s1[i]="%20"
	urlified = "".join(s1)
	# printing both solutions
	print a,urlified
	
