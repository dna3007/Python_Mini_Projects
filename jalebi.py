size = int(input("enter size:"))
N=size *size
row=0
col=0

num=1
matrix=[[0]* size for i in range(size)]
for index in range(0,N):

    while (col<size- index):
        matrix[row][col]=num
        num+=1
        col +=1
    row+=1

    while (row<size-index):
        matrix[row][col-1]=num
        num += 1
        row += 1
    col-=1
    while(col>index):
        matrix[row-1][col-1]=num
        num+=1
        col-=1
        # if col==0:
        #     break
    row-=1
    while(row>index+1):
        matrix[row-1][col]=num
        num+=1
        row-=1
        # if row==1:
        #     break
    col+=1
    # if num==N:
    #     break
for rows in matrix:
    for i in rows:
        print("%4d"%i,end=" ")
    print('\r')