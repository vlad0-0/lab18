m = int(input())
while m%2 == 0 or m < 0:
    m = int(input())
a = []
b = []
for i in range(m):
    for j in range(m):
        b.append(input())
    a.append(b)
    b = []
del(b)
del(j)
x1 = 0
x = 0
x2 = m-1
y1 = 0
y = 0
y2 = m-1
while x1!=x2 and y1!=y2:
    for i in range(y1, y2+1):
        print(a[i][x])
    y = i
    x1 += 1
    for i in range(x1, x2+1):
        print(a[y][i])
    x = i
    y2 -= 1
    for i in range(y2, y1-1, -1):
        print(a[i][x])
    y = i
    x2 -= 1
    for i in range(x2, x1-1, -1):
        print(a[y][i])
    x = i
    y1 += 1
print(a[x1][y1])
