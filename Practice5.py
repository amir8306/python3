num = input("please enter your number....>  ")

list_num = []

for i in num:
    list_num.append(int(i))

sum = 0 
b=0

for x in list_num[::-1]:
    a = x*(2**b)
    b+=1
    sum+=a

print(sum)