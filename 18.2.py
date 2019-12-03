m = int(input())
n = int(input())
k = int(input())
a = []
b = []
for i in range(m):
    for j in range(n):
        b.append(float(input()))
    a.append(b)
    b = []
s = 0
p = 1
while not 1 < k < m:
    k = int(input())
for i in range(n):
    s += a[k][i]
    p *= a[k][i]
print(s)
print(p)
