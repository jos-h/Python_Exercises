s = 'kunal'
s1 = 'unalkk'

d = {}

for i in s:
    if i not in d:
        d[i] = 1
print(d)

for i in s1:
    d[i] -= 1
print(d)

for i , v in enumerate(s):
    print(i,v)