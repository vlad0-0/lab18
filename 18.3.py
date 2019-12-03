m = int(input())
n = int(input())
a = []
b = []
for i in range(m):
    for j in range(n):
        b.append(float(input()))
    a.append(b)
    b = []
k = 0
p = 1
mnp = ''
mn = ''
for j in range(1, m):
    for i in range(n):
        p *= a[j][i]
    if mnp == '' or mnp > p:
        mnp = p
        mn = j
print(mnp)
print(mn)
