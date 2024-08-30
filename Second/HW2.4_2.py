def repeat_deco(n=1):
    def repeat(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                tmp = func(*args, **kwargs)
            return tmp

        return wrapper

    return repeat


code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)