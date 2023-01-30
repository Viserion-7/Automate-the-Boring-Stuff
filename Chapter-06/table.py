tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
l = tableData[0][0]
for i in tableData:
    for j in i:
        if len(j) > len(l):
            l = j
for j in range(len(tableData[0])):
    for i in range(len(tableData)):
        print(tableData[i][j].rjust(len(l)), end = ' ')
    print()