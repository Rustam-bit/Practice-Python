# # # print(1 | 2)
# # # a = (
# # #     "python"
# # #     " is "
# # #     ' realy '
# # #     "exciting"
# # # )
# # # print(a)
# # # print("hello %s %d" % ("hi", 123))
# # # print("hello {} {} ".format("hey", 2222))
# # #
# # # var = "World"
# # # var2 = 123
# # # print(f"Hello, {var} {var2}")
# # # print(f"{10000:+,}")
# # #
# # # a = 1234.5678
# # # print(f"{a:.2f}")
# # #
# # # a = [1, 2, 3]
# # # print(a)
# # #
# # # a.reverse()
# # # print(a)
# # # b = a.copy()
# # # a.clear()
# # # print(a, b)
# # #
# # # a = [[0, 1]] * 3
# # # a[0][0] = 10
# # # print(a)
# # #
# # # b = [0, 1]
# # # a = [b] * 3
# # #
# # # var1, var2, [var3_1, var3_2, var3_3] = [1, "var2", [1, 2, 3]]
# # # print(var1, var2, var3_1, var3_2, var3_3)
# # # # распаковка
# # #
# # #
# # # a = list(range(10))
# # # print(a)
# # # b = [2 ** x for x in a if x % 2 == 0]
# # #
# # # b = []
# # # for x in a:
# # #     if x % 2 == 0:
# # #         b.append(2 ** x)
# # #
# # # c = tuple(int(x) for x in "a1b2c3def" if x.isdigit())
# # # print(c)
# # #
# # # strings = ["Hello", "world", "123"]
# # # joined = " ".join(strings)
# # # print(joined.split())
# # #
# # # # dictionary
# # #
# # # a = dict(one=1, two=2, three=3)
# # # b = {'one': 1, 'two': 2, 'three': 3}
# # # c = dict([('two', 2), ('one', 1), ('three', 3)])
# # # print(a == b == c)
# # #
# # # # a.items()
# # # for key, value in a.items():
# # #     print(key, value)
# # # f = {x: 2 ** x for x in range(10)}
# # # print(f)
# # #
# # # f[3] = -1
# # # print(f)
# # #
# # # a = {'one': 1, 'two': 2, 'three': 3}
# # # b = {'two': -2, 'three': -3, 'four': -4}
# # # a.update(b)
# # # print(a)
# # #
# # # a.update([('two', 2), ('three', 3)])
# # # print(a)
# # # del a['one']
# # # print(a)
# # #
# # # # неизменияемые строки, range и кортежи() - unmutible
# # # # mutible - списки[], словарь{} и множество{}
# # # # set and frozenset
# # # a = {1, 2, 3, 4, 1, 2, 3, 4}
# # # print(a < {1, 2, 3, 4, 5, 6, 7})
# # #
# # # a = frozenset([1, 2, 3, 4, 1, 2, 3, 2])
# # # print(a)
# # #
# # #
# # # def func(val, var=None):
# # #     var = var or []
# # #     var.append(val)
# # #     return var
# #
# # def my_decorator_n(number=1):
# #     def my_decorator(func):
# #         def wrapper(*args, **kwargs):
# #             print(f"Wrapper befor {number}")
# #             tmp = func(*args, **kwargs)
# #             print(f"Wrapper after {number}")
# #             return tmp
# #
# #         return wrapper
# #
# #     return my_decorator
# #
# #
# # @my_decorator_n()
# # def phone(model: str, charge: int = 100, storage: str = "128 gb", status="Working"):
# #     if not 0 <= charge <= 100:
# #         print("Incorrect charge data")
# #         return
# #     print(
# #         f"This {model} is {charge} percent charged"
# #         f"It has {storage} of storage, current status is {status}"
# #     )
# #
# #
# # phone("Iphone")
# # # a = func(1)
# # # b = func(2)
# # # c = func(3)
# # # print(a, b, c)
# # #
# # # l_func = lambda x: 2 ** x
# # #
# # # a = [1, 2, 3, 4, 5]
# # # b = sorted(a, key=lambda x: -x)
# # # print((l_func)(2))
# # #
# # #
# # # def create_generated(start=0):
# # #     num = start
# # #     while True:
# # #         yield num
# # #         num += 1
# # #
# # #
# # # generator = create_generated()
# # #
# # # for i in generator:
# # #     print(i)
# # #     if i >= 7:
# # #         # generator.throw(ValueError("unexpected value > 7"))
# # #         generator.close()
# # #
# # #
# # # def my_decorator(func):
# # #     print("Before wrapper def")
# # #
# # #     def wrapper(*args,**kwargs):
# # #         print("Before func call")
# # #         func(*args,**kwargs)
# # #         print("After func call")
# # #
# # #     print("After wrapper def")
# # #     return wrapper
# # #
# # #
# # # def my_func():
# # #     print("Hello world")
# # #
# # #
# # # my_func()
# # #
# # # print("_______________________")
# # #
# # # my_func_decorated = my_decorator(my_func())
# # #
# # # print("_______________________")
# # #
# # # my_func_decorated()
#
# def f():
#     a = 1
#     print(a)
# if __name__ == '__main__':
#     f()
#     print("11")
#
l = [2,4,6]
for i,el in enumerate(l):
    print(i,el)