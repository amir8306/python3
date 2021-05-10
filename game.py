print("hello welcome to play")
a = int(input())
b = int(input())
for i in range(20):
    c = int((a + b)/2)
    print(c)
    result = int(input())
    if result == 0 :
        break
    elif result == 1:
        a = c
    elif result == 2 :
        b = c