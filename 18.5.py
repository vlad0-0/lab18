m = int(input())
n = int(input())
a = []
b = []
for i in range(m):
    for j in range(n):
        b.append(float(input()))
    a.append(b)
    b = []
for i in range(m):
    for j in range(n):
        if a[i][j] % 2 != 1:
            break
    if j == n-1:
        b.append(i)
print(b[0])
