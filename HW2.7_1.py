def cache_deco(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return wrapper


def solution(func_map, func_filter, data):
    filtered_map = (func_map(i) for i in data if func_filter(i))

    for j, em in enumerate(filtered_map):
        if j % 2 == 0:
            yield em


code = []
while data := input():
  code.append(data)
code = "\n".join(code)
exec(code)