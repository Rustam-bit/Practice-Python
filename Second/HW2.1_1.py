def func(str):
    s = 0
    k = 0
    for ch in str:
        if ch.isdigit():
            s = s + int(ch)
            k = k + 1
    return s / k


while str := input():
    print(func(str))
