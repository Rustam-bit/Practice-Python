data = input().split()
print(round(sum(len(word) for word in data) / len(data), 2))
