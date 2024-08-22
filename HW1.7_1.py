str = input()
x = sorted(set(str.lower()))
for i in x:
    if i != ' ':
        print(i,end=" ")

