m = int(input())
n = int(input())
a = []
b = []
c = 0
d = 0
for i in range(m):
    for j in range(n):
        b.append(float(input()))
    a.append(b)
    b = []
for i in range(m):
    c = sum(a[i])/m
    for j in range(n):
        if a[i][j] > c:
            d += 1
    b.append(d)
    d = 0
print(b)
