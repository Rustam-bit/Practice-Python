def second_min(a):
    del a[a.index(max(a))]
    return max(a)
a = list(input())
print(second_min(a))