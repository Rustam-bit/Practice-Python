a = list(input())
n = int(input())
print(sum(i for i in range(n+1) if i not in a))