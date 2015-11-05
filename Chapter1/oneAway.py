#!/usr/bin/python

# Question 1.5

def isOneAway(str1,str2):
	# if string lengths differ by more than 1, automatic false
	if(abs(len(str1)-len(str2))>1):
		return False

	# store larger string in str1
	if(len(str2)>len(str1)):
		temp=str1
		str1=str2
		str2=temp
	diff=0 # keeps track of differences
	i=0 # iterate larger string
	j=0 # iterate smaller string
	while(i<len(str1) and j<len(str2)):
		if(str1[i]!=str2[j] and len(str1)==len(str2)):
			diff+=1
			i+=1
			j+=1
		elif(str1[i]!=str2[j]):
			diff+=1
			i+=1
		else:
			i+=1
			j+=1
		if (diff > 1):
			return False

	return True
			
if __name__=="__main__":
	print isOneAway('pale','ple')
	print isOneAway('pales','pale')
	print isOneAway('pale','bale')
	print isOneAway('pale','bake')
