from Battleships.Map.Harta import *

class Get_comands_Exceptions(Exception):
    def __init__(self,mesaj):
        pass

class Ui:
    def __init__(self):
       pass

    def get_dimension(self):
        return input("Enter the dimension of the map")

    def get_coordinates(self):
        x = input("The x coordinate : ")
        y = input("The y coordinate : ")
        x.strip(" ")
        y.strip(" ")

        if not(x.isdigit() and y.isdigit()):
            raise Get_comands_Exceptions("Please insert numbers")

        x = int(x) -1
        y = int(y) -1
        return (x,y)
    def get_ship(self, l):
       # L = input("The lenght of the boat(it should be 2, 3 ,4 : ")
        print("Place the ship with the lenght " + str(l))
        x = input("The x coordinate : ")
        y = input("The y coordinate : ")
        d = input("The direction (0 for down and 1 for right) : ")
        return x,y,d

    def start(self):
        print("I am happy to see you, ready to sink some ships ? ")
        print("H - You hit a ship")
        print("S - you sunk a ship")
        print("X - you missed :( ")

    def Dimension_validator(self,dimension):

        if len (dimension) > 2 or not dimension.isdigit():
            raise Get_comands_Exceptions("The dimension does not corespond")
        dimension = int(dimension)
        if dimension > 20 or dimension < 5 :

            raise Get_comands_Exceptions("The dimension does not corespond")
        else:
            return 1

    def round_start(self,round):
        print("\t\t\tRound " + str(round) + " of 40")

    def random_or_not(self):
        print ("Let's get started! ")
        answer = input("How do you want to place your ships ? Do you want them to be random placed or no ? (Y/N) ")
        answer.strip(" ")
        answer= answer.lower()

        if len (answer) > 1:
            raise Get_comands_Exceptions("Give a answer as asked!(Y - yes , N - no)")


        if answer != 'y' and answer != 'n':
            raise Get_comands_Exceptions("Give a answer as asked!(Y - yes , N - no)")

        return answer
    def player_hit(self):
        print("Where do you want to launch the next missle ?")
        return self.get_coordinates()
    def computer_hit(self,x,y):
        print("The Computer fired a missle at x = " + str(x+1) + "  y = " +str(y+1))
    def print_player(self,nr):
        if nr == 1:
            print("\nYour battlefield : ")
        else:
            print("\nComputer battlefield: ")
    def win(self,nr):
        if nr == 2:
            print("You won!!! Congratulation! ")
        else :
            print("The computer won, but you can try again")


