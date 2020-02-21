


import numpy as np
a=input("Enter numbers from 0-8 seperated by spaces")
b = np.array([int(i) for i in a.split(',')])






def print_blank(a):
	for i,j in enumerate(a):
		for k,l in enumerate(j):
			if l==0:
				return i,k





