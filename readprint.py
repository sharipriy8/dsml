matrix=[]
r=int(input("enter number of rows"))
c=int(input("enter number of rows"))
for i in range (r):
	a=[]
	for j in range (c):
		a.append(int(input()))
	matrix.append(a)
for i in range (r):
	for j in range (c):
		
		print(matrix [i][j],end="\t")
	print("\t")
	print()

