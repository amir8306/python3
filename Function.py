def fuctor(a):
    sum = 1
    for i in range(1,a+1):
        sum = sum*i

    print(sum)


def average():
    sum_av = 0
    for i in range(10):
        marks = int(input('please enter your marks...> '))
        sum_av = sum_av + marks
    print(sum_av/10)


average()
average()


fuctor(5)
fuctor(7)
fuctor(15)