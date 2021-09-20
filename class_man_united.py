class man_united:

    info = []
    new_player = 0

    def __init__(self , name , last_name , age ):
        self.name = name
        self.last_name = last_name
        self.age = age
        man_united.new_player +=1
        self.number = man_united.new_player

    def color_of_shirt(self , place):
        if place == "home" :
            print("your shirt is red")
        elif place == "away" :
            print('your shirt is black')
        






    def salary(self,assistance, goal):
        money = 100000 + goal*5000 + assistance*2000
        print(money)


    def trophy(self , cup ):
        premier_league = 200000
        champions_league = 100000
        FA_cup = 5000
        if cup == "premier league":
            print(premier_league)
        elif cup == "champions league":
            print(champions_league)
        elif cup == "FA cup" :
            print(FA_cup)
        else:
            print("invalid cup")
        
        

    

player1 = man_united("cristian",'ronaldo',36)

player2 = man_united("Jesse " ,"Lingard" , 28)

player3 = man_united('Raphaël ' ,'Varanea' , 28)

print(player1.number)
print(player2.number)
print(player3.number)
player1.color_of_shirt('home')
player1.salary(4 , 5)
player2.trophy("premier league")



