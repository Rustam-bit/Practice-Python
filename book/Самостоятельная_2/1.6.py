a,b,c = int(input()),int(input()),int(input())
if a + b <= c or a + c < b or b + c < a:
    print(False)
else:
    print(True)