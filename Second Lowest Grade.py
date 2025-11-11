"""
Problem: Find the Students with the Second Lowest Grade
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example
records = [[“chi”, 20.0], [“beta”, 50.0], [“alpha”, 50.0]]
The ordered list of scores is [20.0, 50.0], so the second lowest score is 50.0.
There are two students with that score: [“beta”, “alpha”].
Ordered alphabetically, the names are printed as:
alpha
beta

Input Format
The first line contains an integer, N, the number of students.
The next 2N lines describe each student over two lines:
	•	The first line contains a student’s name.
	•	The second line contains their grade.

Constraints
2 < N < 5H
There will always be one or more students having the second lowest grade.

Output Format
Print the name(s) of any student(s) having the second lowest grade.
If there are multiple students, order their names alphabetically and print each name on a new line.

"""


records = []
n = int(input())

for _ in range(n):
    name = input()
    score = float(input())
    records.append([name, score])

# Find the second lowest grade
scores = sorted({s for _, s in records})
second_lowest = scores[1]

# Get all students with the second lowest grade
names = sorted([name for name, score in records if score == second_lowest])

# Print each name on a new line
for name in names:
    print(name)