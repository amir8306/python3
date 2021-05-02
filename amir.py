print('hello welcom to school')
average = int(input('please enter your average ....> '))
math = int(input('please enter your math ......> '))
if average > 19.5 or math == 20:
    print('you are accepted')
elif average > 16 and math > 18:
    print('you are accepted')
elif average > 18 and math > 16:
    print('you are accepted')
else:
    print("you aren't accepted")