def map(func, seq):
   gen = (func(i) for i in seq)
   return gen
func_in, seq_in = eval(input()), eval(input())

for x in map(func_in, seq_in):
   print(x)