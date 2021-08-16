class play_station:

    number_of_players = 0

    def __init__(self , name , last_name , age):
        self.name = name
        self.last_name = last_name
        self.age = age 
        self.console = 'ps4'
        play_station.number_of_players +=1
    
    def play_Fifa21(self):
        print(f"{self.name} started playing FIFA21 ...")

    def play_callofduty(self):
        print(f"{self.name} started playing CallOfDuty ...")




class xbox:

    number_of_players = 0

    def __init__(self , name , last_name , age ):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.console = xbox
        xbox.number_of_players +=1
    
    def play_forza_horizon4(self):
        print(f"{self.name} started playing forza_horizon4..... ")
    
    def play_pes2021(self):
        print(f"{self.name} started playing pes2021 ....")



class suggestion():

    number_of_suggestions = 0


    def __init__( self , name , last_name , age):
        self.name = name
        self.last_name = last_name
        self.age = age
        suggestion.number_of_suggestions +=1
        
    
    def give_a_game(self):
        if self.age >= 4 and self.age <= 10:
            print(f"{self.name} you can play (Fifa , pes , lego , NBA) ")
        elif self.age >=11 and self.age <= 15 :
            print(f"{self.name} you can play (coll_of_duty , ufc , Ratchet and Clank , Untitled Goose Game)")
        elif self.age >= 16 and self.age <= 30 :
            print(f"{self.name} you can play (Titanfall , Doom , The Last Guardian , Devil May Cry 5 , Assassin’s Creed , Detroit ,Final Fantasy XV , Final Fantasy XV)")
        



class game_style():
    
    
    number_of_buyers_the_game = 0
    def __init__(self , name , last_name , gener):
        self.name = name
        self.last_name = last_name
        self.gener = gener
        game_style.number_of_buyers_the_game +=1

    def buy_the_game(self):
        if self.gener == 'war_games' :
            print(f"{self.name} you can play(Titanfall , Doom , The Last Guardian ,  Devil May Cry 5 ,  Assassin’s Creed , coll_of_duty )")
        elif self.gener == 'sports_games' :
            print(f"{self.name} you can play (Fifa ,pes , ufc ,NBA)")



        



player3 = xbox('ali' , 'mosavi' , 20)
player4 = xbox('farzad' , 'ahmadi', 23)
player3.play_forza_horizon4()
player4.play_pes2021()
print(xbox.number_of_players)

player1 = play_station('amir' , 'ahmadi' , 17)
player2 = play_station('shayan' , 'alv' , 22)
player1.play_callofduty()
player2.play_Fifa21()
print(play_station.number_of_players)

player5 = suggestion('amir mahadi' , 'ahmadi' , 27)
player6 = suggestion('hesam' , 'akbari' , 30)
player5.give_a_game()
player6.give_a_game()
print(suggestion.number_of_suggestions)


player7 = game_style('hasti' , 'mirmiran' , 'war_games')
player8  = game_style('amir reza' , 'hadi' , 'sports_games')
player7.buy_the_game()
player8.buy_the_game()






