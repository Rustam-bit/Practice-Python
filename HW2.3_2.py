def filter(func, seq):
    gen = (i for i in seq if func(i))
    return gen


func_in, seq_in = eval(input()), eval(input())

for x in filter(func_in, seq_in):
    print(x)
