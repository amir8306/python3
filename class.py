class school:
    def __init__(self ,  name , last_name , average , teachre , fild ):
        self.name1 = name
        self.last_name1 = last_name
        self.average1 = average
        self.teachre1 = teachre
        self.fild1 = fild
    
    
    def fild(self):
        if self.fild1 == "math":
            print("red")
        elif self.fild1 == "Science":
            print("blue")
        elif self.fild1 == "human":
            print("brown")

    def infor(self):
        print(self.name1)


a = school('amir' , 'ahmadi' , 18 , 'ali' , 'math')
print(a.fild())
print(a.infor())
