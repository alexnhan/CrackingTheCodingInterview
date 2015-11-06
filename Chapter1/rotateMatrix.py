#!/usr/bin/python

# Question 1.7
# ith row becomes N-1-ith column

def rotateMatrix(mat,N):
	# create an empty matrix to hold rotated matrix
	newMat=[]
	for i in range(N):
		newMat.append(range(N))
	for i in range(N):
		for j in range(N):
			newMat[j][N-1-i]=mat[i][j]
	return newMat

if __name__=="__main__":
	mat=[[1,2,3,4],[4,5,6,7],[7,8,9,10],[10,11,12,13]]
	N=4
	print mat,rotateMatrix(mat,N)
