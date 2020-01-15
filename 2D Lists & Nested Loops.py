
#2D lists

#list with other lists inside:
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
#I would like the first element of the first list
#remember order is: 0, 1, 2, 3
print(number_grid[1][1])


#Nested for loop = for loop inside of a for loop
for row in number_grid:
    for col in row:
        print col
