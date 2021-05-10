#game with numbers
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
print("------------------- first one finished -------------------")

#finding even numbers in a list
list2 = []
for i in range(10):
    list1 = int(input('please Enter your nauber ...> '))
    list2.append(list1)

for x in list2:
    if x % 2 == 0:
        print(x)

print("------------------- second one finished -------------------")
#finding largest number in a list
red = [20 ,57 , 43 , 91 ,751 , 21 ,43]
red.sort()
print(red[-1])