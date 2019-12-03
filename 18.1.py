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
x1 = 0
x = 0
x2 = m-1
y1 = 0
y = 0
y2 = m-1
print(a[0][0])
while x1!=x2 and y1!=y2:
    while y < y2:
        y += 1
        print(a[y][x])
    while x < x2:
        x += 1
        print(a[y][x])
    while y > y1:
        y -= 1
        print(a[y][x])
    while x > x1:
        x -= 1
        print(a[y][x])
        
