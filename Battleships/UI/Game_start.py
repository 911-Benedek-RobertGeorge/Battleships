from Battleships.Map.Harta import *
from Battleships.UI.UI import *

def Start():
    """here the game will start"""


    ui = Ui()
    #dimension = int(input("Select the level (5 - 20) : "))


    stop = 0
    while  stop != 1 :
        try:
                dimension = input("Select the level (5 - 20) : ")
                stop = (ui.Dimension_validator(dimension) == 1)


                dimension = int(dimension)
        except Get_comands_Exceptions as UE:
            print(UE)
    #setup
    player = Map(dimension)
    AI = Map(dimension)
    AI.random_place_ships()
    stop = 1
    while stop :
        try:
            answer = ui.random_or_not()
            stop = 0

        except Get_comands_Exceptions as UE:
            print(UE)
    if answer == 'y':
        player.random_place_ships()
    else:

        l = 2
        #place the ships
        while l < 5:
            try:
                    x, y, d = ui.get_ship(l)
                    x = int(x)
                    y = int(y)
                    d = int(d)
                    x -= 1
                    y -= 1
                    player.place_ships(l, x, y, d, 10 + l - 2)
                    l += 1
            except Exception as Ex:
                print(Ex)
                print(player)

    match_is_not_won = 1
    stack = []
    ui.start() # -> message
    player_ships = 0
    ai_ships = 0
    while match_is_not_won :
        #repeating still someon won
        # ui.computer_hit()
        miss = 1
        while miss:
            #repeat until you shoot inside map or on a free spot
            try :
                x, y = ui.player_hit()
                mesaj = AI.missle(x, y)
                print("\n\n\n"+  mesaj + "\n")
                if mesaj == "You Sunk a ship. Good job!":
                    player_ships += 1
                miss = 0
                ui.print_player(2)
                print(AI)
            except MapException as ME:
                print(ME)
            except Get_comands_Exceptions as CE:
                print(CE)
        if player_ships == 3:
            match_is_not_won = 0
            #ui.win(2)
        ui.print_player(1)

        x,y = player.computer_hit(stack)
        ui.computer_hit(x,y)
        mesaj = player.missle(x,y)
        if mesaj == "You hitted a ship":
            stack.append((x,y+1))
            stack.append((x,y-1))
            stack.append((x+1,y))
            stack.append((x-1,y))
        elif mesaj =="You Sunk a ship. Good job!":
            ai_ships += 1
            stack.clear()
        print(player)
        if ai_ships == 3:
            match_is_not_won = 0
            #ui.win(1)
    if ai_ships == 3:
        ui.win(1)
    else :
        ui.win(2)
#TODO HUNT MODE, dupa un hit verifica toate 4 directii, cand da de una buna, merge doar pe pozitia linia aia/col
    #max 40 rounds




#Start()