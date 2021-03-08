import unittest

from Battleships.Map.Harta import *



class map_test(unittest.TestCase):

    def test_map(self):
        ob = Map(8)
        ob.missle(1,0)
        ob.missle(5,4)
        ob.missle(7,7)
        ob.place_ships(3,3,3,1,10)
        ob.place_ships(4,0,1,0,11)
        ob.place_ships(2,7,0,1,12)
        ob.missle(3,3)
        ob.missle(3,4)
        ob.missle(3,5)
        ob.missle(0,3)
        ob.missle(1,5)
        ob.missle(7,0)
        ob.missle(7,1)

        bt= ob.get_battlefield()


        assert bt[7][0] == 22
        assert bt[7][1] == 3
        assert bt[1][0] == 1
        #print(bt[3][3])
        assert bt[3][3] >= 20

        ob.place_ships(4,2,5,0,13)
        print (ob)
        print("\n\n\n")
    #test_map()

    def test_random(sefl):
        ob = Map(8)
        ob.random_place_ships()
        ob.missle(2,3)
        ob.missle(2,4)
        ob.missle(4,3)
        #ob.missle(100,100)
        ob.computer_hit([])
        #print(ob)

    #test_random()
