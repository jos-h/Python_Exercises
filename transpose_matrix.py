arr = [
    [13, 4, 8, 14, 1],
    [9, 6, 3, 7, 21],
    [5, 12, 17, 9, 3]
]
r = 3
c = 5
transpose = []
for j in range(c):
    transpose.append([arr[i][j] for i in range(r)])

print(transpose)
a = [[0 for i in range(c)] for j in range(r)]
print(a)
