import functools
def cache_deco(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in cache:
            cache[cache_key] = func(*args, **kwargs)
        return cache[cache_key]

    return wrapper

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)
