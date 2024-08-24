def func(str):
    if str[0] == '!':
        return str.upper().replace("!", "").replace("@", "").replace("#", "").replace("%", "")
    return str.lower().replace("!", "").replace("@", "").replace("#", "").replace("%", "")
while str:=input():
    print(func(str))