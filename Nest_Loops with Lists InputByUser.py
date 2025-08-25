matrix=[]

row = int(input('Enter number of rows'))
col = int(input('Enter number of columns'))

for i in range (row):
    rowList=[]
    for j in range(col):
        data = int(input('Enter data value: '))
        rowList.append(data)
    matrix.append(rowList)


for i in range (len(matrix)):
    for j in range (len(matrix[i])):
        print(matrix[i][j], end='\t')
    print()


                    

