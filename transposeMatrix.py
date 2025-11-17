# 5. Write a program to transpose a matrix.
mat = eval(input("Enter a matrix: "))
transposed = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
print(transposed)
