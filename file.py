# writting in to a file (evrythings will be delete and only new lines will save)
with open("/home/amir/Documents/coding/class/testfile.txt" , 'w') as file1:
    amir = file1.write("hello my name is amirmehdi")
# append is like writting but it won't delete anything 

with open("/home/amir/Documents/coding/class/testfile.txt" , 'a') as file3:
    cont = file3.write("and this is a new line for learning ...")
# it will read the content of the file.
with open("/home/amir/Documents/coding/class/testfile.txt") as file2:
    content = file2.read()
    print(content)
