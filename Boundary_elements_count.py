def boundary_count(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == 0 or j == 0 or i == len(matrix)-1 or j == len(matrix)-1:
                count = count + matrix[i][j]
    return count        

matrix = eval(input())
print(boundary_count(matrix))