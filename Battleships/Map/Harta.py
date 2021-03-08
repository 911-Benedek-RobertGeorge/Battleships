from texttable import Texttable
import random
from Battleships.Map.Exceptions import Battlefield_exception



class MapException(Battlefield_exception):
    def __init__(self,mesaj):
        pass


class Map:
    def __init__(self,dimension):
        """make the map for ships"""
        self._battlefield = [[0 for col in range(dimension+1)]for line in range(dimension+1)]
        self._dimension = dimension

    def missle(self,x,y):

        ''' the function need the coordinates for a missle and it will be  marked and returns the mesage:hit mis sunk'''
        mesaj = ""

        if x > self._dimension - 1 or x < 0 or y > self._dimension - 1 or y < 0:
            raise MapException("The coordinates are not in the battlefield")
        if self._battlefield[x][y] == 1 or self._battlefield[x][y] > 20 or self._battlefield[x][y] == 3:
            raise MapException("You hitted here already, try another spot")
        if self._battlefield[x][y] >= 10:
            self._battlefield[x][y] += 10
            mesaj += "You hitted a ship"
            if self.verify_sink(x,y,self._battlefield[x][y] - 10) == 1:
                self._battlefield[x][y] = 3
                mesaj = "You Sunk a ship. Good job!"
        else:
            self._battlefield[x][y] = 1
            mesaj = "You missed, but dont worry you have more chances! "
        return mesaj


    def verify_sink(self,x,y,name):
        '''it verifies if a ship will be sinked after the missle'''
        x_direction = [0,1,0,-1]
        y_direction = [1,0,-1,0]
        xd = -2
        for i in range(0,4):
            if not (x > self._dimension - 1 or x < 0 or y > self._dimension - 1 or y < 0) :
                value = self._battlefield[x+x_direction[i]][y+y_direction[i]]
                if value == name :
                    return 0
                if value == name+10 :
                    xd = x_direction[i]
                    yd = y_direction[i]
                    break
        if xd == -2:
            return 0
        if xd == 0:
            for i in range(0,self._dimension):
                if self._battlefield[x][i] == name:
                    return 0
        else :
            for i in range(0, self._dimension):
                if self._battlefield[i][y] == name:
                    return 0
        return 1
        #TODO cv mai ok




    def random_place_ships(self):
        """ will place 3 random ships with the name L + 10 -2 (10,11,12)"""
        L = 5
        while L > 1:
            x = random.randint(0,self._dimension)
            y = random.randint(0,self._dimension)
            d = random.randint(0,1)
            name = 10 + L - 2
            if (self.Validator_place_ships(L,x,y,d) == 1) :
                self.place_ships(L,x,y,d,name)
                L -= 1





    def Validator_place_ships(self,L,x,y,d):
        '''make sure that the ship will be palced corectly'''
        xd = 0
        if d == 0:
            xd = 1
        for row in range(x, x +1 -xd + xd * L):
            for col in range(y, y -d + L * d +1 ):

                if self._battlefield[row][col] >= 10:
                    return 0
                elif row > self._dimension-1 or row < 0 or col > self._dimension-1 or col < 0:
                    return 0
        return 1


    def place_ships(self,L,x,y,d,name):
        """
        :param L: the lenght of the ship
        :param x: x coordinate
        :param y: y coordinate
        :param d: the direction: 0 if it will be to the bottom , and 1 if it will be to the right
        :param name : a unique number for ships name >= 10
        """
        if self.Validator_place_ships(L,x,y,d) == 1:
            xd = 0
            if d == 0:
                xd = 1
            for row in range(x, x + 1 -xd + xd * L):
                for col in range(y,y+1 - d +L*d):
                    self._battlefield[row][col] = name
        else:
            raise MapException("The ship intersects another ship or doesnt fit in the battlefield")

    def get_battlefield(self):
        return self._battlefield

    def computer_hit(self, stack):

        if len(stack) == 0:
            x = random.randint(1,self._dimension)
            y = random.randint(1,self._dimension)
            x = x - 1
            y = y - 1
            if self.computer_hit_validator(x,y) == 1:
                return (x,y)
            else:
                return self.computer_hit(stack)
        else:
            x,y = stack[len(stack)-1]
            if self.computer_hit_validator(x,y) == 1:
                return (x,y)
            else:
                stack.pop()
                return self.computer_hit(stack)

    def computer_hit_validator(self ,x,y):

        if x > self._dimension - 1 or x < 0 or y > self._dimension - 1 or y < 0:
            return 0
        #print(self._battlefield[x][y])
        if self._battlefield[x][y] >= 20:
            return 0
        if self._battlefield[x][y] == 1:
            return 0
        if self._battlefield[x][y] == 0 or (self._battlefield[x][y] >= 10 and self._battlefield[x][y] <20):
            return 1

        return 0



    def computer_map(self):

        pass
    def __str__(self):
        '''making the texttable for the battlefield'''
        t = Texttable()
        header = [' ']

        for h in range(1,self._dimension+1):
            header.append( h )

        t.header(header)
        index = 1

        for row in range(0,self._dimension+0):
            data = []
            data.append(index)
            index += 1
            for val in self._battlefield[row][0:-1]:
                if val >= 10 and val <20:
                    data.append("S" + str(val) )

                elif val == 3:
                    data.append('S')
                elif val == 1:
                    data.append('X')
                elif val >= 20 :
                    data.append('H')
                else:
                    data.append(' ')
            t.add_row( data)
        return t.draw()

