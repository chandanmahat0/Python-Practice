"""
Let's learn about list comprehensions! You are given three integers x, y and z representing the dimensions of a
cuboid along with an integer n. Print a list of all possible coordinates given by (2, 7, k) on a 3D grid where the
sum of i + j + k is not equal to n. Here, 0 <= i < z;0 <= j < y;0 <= k < z. Please use list comprehensions
rather than multiple loops, as a learning exercise.

Example

z=1

y=1

z=2

n=3

All permutations of [z, 4, k] are:

[[o, 0, 0], 0, 0, 1], 0, 0, 2], 0, 1, 0], 0, 1, 1], [o, 1, 2], 1, 0, 0], 11, 0, 1], 1, 0, 2], 11, 1, 0], 1, 1, 1], 11, 1, 2].
Print an array of the elements that do not sumton = 3.

([0,0,0], [0,0,1],[0,0,2],[0,1,0],[0,1,1],1,0,0], 1,0,1], [1,1,0], [1,1,2]]

Input Format

Four integers x, y, 2 and n, each on a separate line.

Constraints

Print the list in lexicographic increasing order.
"""

x = int(input())
y = int(input())
z = int(input())
n = int(input())
    
result = [[i, j, k] 
  for i in range(x + 1) 
  for j in range(y + 1) 
  for k in range(z + 1) 
  if (i + j + k) != n]
print(result)
