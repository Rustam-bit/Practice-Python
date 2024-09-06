# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __getattribute__(self, item):
#         print(f"__getattribute__{item}")
#         if item == 'x':
#             raise AttributeError("Доступ запрещен")
#         else:
#             return object.__getattribute__(self, item)
#
#     def __setattr__(self, key, value):
#         # print(f"__setattr__{key} {value}")
#         # object.__setattr__(self, key, value)
#         self.__dict__[key] = value
#         if key not in ["x", "y", "z"]:
#             raise AttributeError("Нельзя объявлять новые атрибуты")
#         else:
#             self.__dict__[key] = value
#
#     def __getattr__(self, item):
#         print(f"__getattr__ {item}")
#         return -999
#
#     def __delattr__(self, item):
#         raise AttributeError("Нельзя удалять")
#         # print(f"__delattr__ {item}")
#
# if __name__ == '__main__':
#     p1 = Point(1, 1)
#     p1.x = 5
#     p1.y = 2
#     # print(p1.x)
#     # print(p1.y)
#     # p1.z = 10
#     print(p1.z)
#     del p1.z
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __getitem__(self, item):
        print(f"__getitem__ {item}")
        return self.marks[item]

    def __setitem__(self, key, value):
        print(f"__setitem__ {key} {value}")
        self.marks[key] = value

    def __delitem__(self, key):
        print(f"__delitem__ {key}")
        del self.marks[key]


class FRange:
    __slots__ = ("start","end","step")
    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step
        self.current_point = self.start

    def __next__(self):
        if self.current_point + self.step >= self.end:
            raise StopIteration
        else:
            self.current_point += self.step
        return self.current_point

    def __iter__(self):
        return self


if __name__ == '__main__':
    st = Student('Sergey', {'algebra': [5, 2, 3, 4, 5]})
    st["physics"] = [4, 4, 5, 5, 2]
    print(st.marks)
    del st["physics"]

    frange = FRange(0.1, 0.5, 0.1)
    for i in frange:
        print(i)

    # print(st.__dict__)