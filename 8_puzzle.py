


import numpy as np
a=input("Enter numbers from 0-8 seperated by spaces")
b = np.array([int(i) for i in a.split(',')])
olvable=True
inv_count = 0; 

# Checking if the given matrix is solvable

for p in range(8):
	for q in range(p+1,9):
		if(b[p] and b[q] and b[q]>b[p]):
			inv_count+=1

if(inv_count%2):
	print('Unsolvable')
	solvable=False


a=np.reshape(b, (3, 3))
goal=np.array([[1,2,3],[4,5,6],[7,8,0]])  

# Creating text file to write the Node information
Nodes= open("Nodes.txt","w")
nodePath=open("nodePath.txt","w")
info=open("NodesInfo.txt","w")





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

ds=[]
	ds.append([a,own_id,parent_id])
	flag= False
	i=0
	while (not flag):
		parent= ds[i]
		print('i= ',i)
		next_iter= swapping(parent[0],print_blank(parent[0])[0],print_blank(parent[0])[1])
		node_pid= parent[1]
		j=0
		while(j<len(next_iter)):
			unq= True
			for k in range(len(ds)):
				# comparing the possible swaps with already stored values id ds.
				comparison= next_iter[j]== ds[k][0]
				if(comparison.all()==True):
					unq= False
					del next_iter[j]
					j-=1
					break
			if(unq):
				node_oid= len(ds)
				# appending all unique combinations in ds.
				ds.append([next_iter[j],node_oid, node_pid])
				# writing node information in the text file(converting arrays into string)
				nodes=str(next_iter[j][0][0])+" "+str(next_iter[j][1][0])+" "+str(next_iter[j][2][0])+" "
				nodes+=str(next_iter[j][0][1])+" "+str(next_iter[j][1][1])+" "+str(next_iter[j][2][1])+" "
				nodes+=str(next_iter[j][0][2])+" "+str(next_iter[j][1][2])+" "+str(next_iter[j][2][2])+"\n"
				Nodes.write(nodes)
				
				# comparing iterations with goal matrix 
				comparison_g=next_iter[j]==goal
				if(comparison_g.all()==True):
					# ds.append([next_iter[j],node_oid, node_pid])
					print('Goal reached')
					flag = True
					solvable=False
					break 	
			j+=1
		if(i<len(ds)-1):						
			i+=1
		else:
			break
		parent= ds[i]
# Back tracking
# ======================================================================================================================================================================= #

#### creating a list for storing ID's and states of shortest path
	shortest_path=[]	
	node_oid=ds[len(ds)-1][1]
	print(len(ds))
	while(node_oid>=0):
		key=ds[node_oid][0]
		node_pid=ds[node_oid][2]
		shortest_path.append([key,node_oid,node_pid])
		if(node_oid==0):
			break
		node_oid=node_pid
# print(shortest_path)
	i=len(shortest_path)
	for i in range(len(shortest_path)-1,-1,-1):
		info.write(str(shortest_path[i][1])+" "+str(shortest_path[i][2])+"\n")
		for c in range(3):
			for r in range(3):
				nodePath.write(str(shortest_path[i][0][r][c])+" ")
		nodePath.write("\n")
	print(Reverse(shortest_path)) 

		
		
	# print(shortest_path)
	i=len(shortest_path)
	
	print(Reverse(shortest_path)) 

	




