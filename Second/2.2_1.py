for x in map(lambda i: i * i if i % 2 == 1 else -i, range(int(input().split()[0]), int(input().split()[1]), int(input().split()[2]))):
    print(x)
