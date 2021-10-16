num = int(input("please enter your number...>  "))

list_num=[]
for i in range(100):
    if num > 1:
        x = num%2
        list_num.append(x)
        num = num//2
    else:
        list_num.append(num)
        break
#print(list_num[::-1])

finall = ''
for a in list_num[::-1]:
    finall += str(a)
print(int(finall))

