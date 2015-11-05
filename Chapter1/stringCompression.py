#!/usr/bin/python

# Question 1.6

def stringCompress(s):
	cs=[] #compressed string
	count=1
	for i in range(1,len(s)):
		if(s[i]==s[i-1]):
			count+=1
		else:
			cs.append(s[i-1])
			cs.append(str(count))
			count=1
		if(i==len(s)-1): # last character
			cs.append(s[i])
			cs.append(str(count))
	cs="".join(cs)
	if(len(cs)>len(s)):
		return s
	else:
		return cs

if __name__=="__main__":
	s = "aabcccccaaa"
	compressStr = stringCompress(s)
	print compressStr
