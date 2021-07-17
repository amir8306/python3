#def and average
# calculating the average of marks
def information(marks , name , last_name):
    sum = 0
    for i in marks:
        sum = sum + i 
    av = sum/10
    info = {"av" : av , "name" : name , "last_name" : last_name}
    return info
#creating a list
marks = []
# getting marks
for x in range(10):
    mark = int(input("please enter your mark ...> "))
    marks.append(mark)
a = information(marks , "amir" , "ahmadi" )
print(a)