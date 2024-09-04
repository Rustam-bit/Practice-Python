A, B = int(input()), int(input())
if A == 0 and B != 1:
    print("Нет реш")
elif A == 0 and B == 1:
    print("Решение является любое число")
else:
    print((B - 1) / A - 1)
