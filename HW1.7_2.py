str = input().lower().split()
max = 0
l = ''
for i in str:
    if str.count(i) > max:
        max = str.count(i)
        l = i
print(l, max)
