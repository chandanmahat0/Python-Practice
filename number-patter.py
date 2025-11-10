"""
The included code stub will read an integer,n , from STDIN.
Without using any string methods, try to print the following:
123...n

expample: if n = 5, then the output should be 12345.

Note that "..." represents the consecutive values in between.
"""
n = int(input())
if 1 <= n <= 150:
  for i in range(1, n + 1):
    print(i, end="")