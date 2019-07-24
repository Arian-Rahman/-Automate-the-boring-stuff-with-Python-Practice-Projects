
grid = [[' .',' .',' .',' .',' .',' .'],
        [' .',' 0',' 0',' .',' .',' .'],
        [' 0',' 0',' 0',' 0',' .',' .'],
        [' 0',' 0',' 0',' 0',' 0',' .'],
        [' .',' 0',' 0',' 0',' 0', ' 0'],
        [' 0',' 0',' 0',' 0',' 0',' .'],
        [' 0',' 0',' 0',' 0',' .',' .'],
        [' .',' 0',' 0',' .',' .',' .'],
        [' .',' .',' .',' .',' .',' .']]

#normal print
for row in range (len(grid)):
    for col in range (len(grid[row])):
        print(grid [row][col] , end=" ")
    print()

print()

#right rotate

for col in range (len(grid[0])):    # accessed the col in row[0] manually , as row can't be declared here
                                    #and all the rows have same number of columns ,it works
    for row in range(len((grid))):      #row = 9     #col = 6
        print(grid[row][col], end=" ")
    print()



"""











inf = float('inf')
A = [[0,1,4,4,3],
     [1,0,2,4,4],
     [4,2,0,1,5],
     [4,5,1,0,3],
     [3,4,5,3,0]]

print('\n'.join([''.join(['{:2}'.format(item) for item in row])
      for row in A]))
"""
'''
a = [[1, 2, 3, 4], [5, 5, 5, 6], [3,7, 8, 9]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()
'''

