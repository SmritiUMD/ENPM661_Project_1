


import numpy as np
a=input("Enter numbers from 0-8 seperated by spaces")
b = np.array([int(i) for i in a.split(',')])






def print_blank(a):
	for i,j in enumerate(a):
		for k,l in enumerate(j):
			if l==0:
				return i,k
def swapping(data,i,k):
	keys={(0,0):[(0,1),(1,0)],
		  (0,1):[(0,0),(0,2),(1,1)],
		  (0,2):[(0,1),(1,2)],
		  (1,0):[(0,0),(1,1),(2,0)],
		  (1,1):[(0,1),(1,0),(1,2),(2,1)],
		  (1,2):[(0,2),(1,1),(2,2)],
		  (2,0):[(1,0),(2,1)],
		  (2,1):[(1,1),(2,0),(2,2)],
		  (2,2):[(1,2),(2,1)]}
	possible=[]
	for set_ in keys.get((i,k)):
		temp_data = np.copy(data)
		temp=temp_data[set_]
		temp_data[set_]=temp_data[i,k]
		temp_data[i,k]=temp  
		possible.append(temp_data)    
	return possible




