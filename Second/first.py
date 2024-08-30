def chekced(left,data,right):
    return left<=data<=right
left = int(input())
right = int(input())
while data:=input():
    numbers = int(data)
    if not chekced(left,numbers,right):
        print("False")
        exit()
print("True")