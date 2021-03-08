#!/usr/bin/python
from functools import partial
import tkinter
from tkinter import *
from Battleships.UI.UI import *
import ui as ui
from Battleships.Map.Harta import *
from Battleships.UI.Game_start import *

Ui = Ui()
Game = tkinter.Tk()
# Code to add widgets will go here...
Game.title("Battleships")
Game.geometry('700x450')

comands = []
stack = []
barcip = []
barcic = []
computer = Map(10)
computer.random_place_ships()
battlefield =computer.get_battlefield()

player = Map(10)
player.random_place_ships()
#TODO PLACE SHIPS MANUALLY , cand apasa pe un buton, functia preia pozitia si restu
player_bt = player.get_battlefield()
row2 = []

def Ai_hit():
    x,y = player.computer_hit(stack)
    x = int(x)
    y = int(y)
    comands[x * 10 + y]()

    #button[y].config(state=DISABLED, bg="#CCFFFF", activebackground="#CCFFFF", relief=SUNKEN)

def popupmsg(msg):
    popup = tkinter.Tk()
    popup.wm_title("!")
    label = tkinter.Label(popup, text=msg, font=NORMAL)
    label.pack(side="top", fill="x", pady=10)
    B1 = tkinter.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    Game.destroy()
#popupmsg("MERGE")
def racheta_AI(i,j,player,button,barcic):
    try:
        mesaj = player.missle(i,j)

        if mesaj == "You hitted a ship":
            button[j].config(state=DISABLED, bg="red", activebackground="red", relief=SUNKEN)
            #TODO BAGA AICI STACK.APPEND(DIRECTION)
            stack.append((i, j + 1))
            stack.append((i, j - 1))
            stack.append((i + 1, j))
            stack.append((i - 1, j))
            # button[j].config(bg ="red",border = -1, activebackground ="red", relief = SUNKEN)
        elif mesaj == "You Sunk a ship. Good job!":
            button[j].config(state=DISABLED, bg="dark red", activebackground="dark red", relief=SUNKEN)
            barcic.append(1)
            if len(barcic) == 4:
                popupmsg("Computer wins!")
            stack.clear()

        else:
            button[j].config(state=DISABLED, bg="#CCFFFF", activebackground="#CCFFFF", relief=SUNKEN)
        #print(mesaj)
        print("Computer fired at x = " + str(i + 1) + " and y = " + str(j + 1) + '\n')
    except MapException as ME:
        print(ME)
        Ai_hit()

def racheta(i,j,computer,button,barcip):
    mesaj = computer.missle(i,j)
    #print(barcip)
    #photo = PhotoImage(file = r"D:\Facultate\github\a11-911-Benedek-RobertGeorge\Battleships\UI\photo" )
    #TODO ASK WHY THIS PHOTO DOES NOT WORK< HOW SHOULD I WRITE THE PATH"
    if mesaj == "You hitted a ship" :
        button[j].config(state = DISABLED,bg ="red", activebackground ="red", relief = SUNKEN)
        #button[j].config(bg ="red",border = -1, activebackground ="red", relief = SUNKEN)
    elif mesaj == "You Sunk a ship. Good job!":
        button[j].config(state = DISABLED,bg="dark red", activebackground="dark red", relief=SUNKEN)
        barcip.append(1)
        #print(len(barcip))
        if len(barcip) == 4:
            popupmsg("You won!")
    else:
        button[j].config(state = DISABLED, bg ="#CCFFFF", activebackground ="#CCFFFF", relief = SUNKEN)
    print(mesaj)
    print("You fired at x = " + str(i+1) + " and y = "+ str(j+1)+'\n')
    Ai_hit()




def pri():
    print(player)



br = tkinter.Button( Game , state=DISABLED,   text ="Computer", font = "Helvetica 16 bold italic",
                                  bg="WHITE", width=0, height=1,
                                 )
br.grid(row = 1, column = 5 )

pl = tkinter.Button( Game , state=DISABLED,   text ="Player", font = "Helvetica 16 bold italic",
                                  bg="WHITE", width=0, height=1,
                                 )
pl.grid(row = 1, column = 15 )

row = []
for i in range(0,10):
    row.append(Frame(Game))
    #row[i].grid(rowspan = 1,columnspan = 0 ,row = i +2 )
    button = []
    for j in range(0,10):
       # if battlefield[i][j] < 10:
            try :
                button.append(tkinter.Button(row[i],state = NORMAL,relief = RAISED, fg ="blue", activeforeground = "blue" ,command =  partial(racheta, i,j,computer,button,barcip), bg = "#37d3ff",width = 2,height =1,highlightthickness=4,highlightbackground="#37d3ff"))
            except MapException as ME:
                print(ME)
        #else :
            #button.append(tkinter.Button(row[i],state = NORMAL,relief = RAISED,fg ="blue", activeforeground = "blue" ,command = partial (racheta,i,j,computer,button), bg = "#324977",width = 2,height =1,highlightthickness=4,highlightbackground="#37d3ff"))

            button[j].grid(row = i,column = j)
    #print(computer)
    row [i].grid(row=i + 2, column=1, columnspan=20)


bridge = []
row3=[]
for i in range(0,12):
    row3.append(Frame(Game))

   # bridge.append(tkinter.Button(row3[i],relief = RAISED,state = DISABLED,width = 5,height = 1, bg = "black"))
    bridge.append(tkinter.Button(row3[i], state=DISABLED, relief=RAISED,
                                   bg="blue", width= 0, height=1,
                                 highlightthickness=4, ))

    bridge[i].grid(row = i, column =  0)
    row3[i].grid(row=i, columnspan=2,column = 9)



frame2 = Frame(Game )
frame2.grid(row = 10)

for i in range(0,10):
    row2.append(frame2)
    #row2[i].grid(row = i+2 ,column = 11 , columnspan = 10)
    button = []
    for j in range(0,10):
        if player_bt[i][j] < 10:
            try :
                button.append(tkinter.Button(row[i],state = DISABLED,relief = RAISED, fg ="blue", activeforeground = "blue" ,command =  partial(racheta_AI, i,j,player,button,barcic), bg = "#37d3ff",width = 2,height =1,highlightthickness=4,highlightbackground="#37d3ff"))
                comands.append(partial(racheta_AI,  i,j,player,button,barcic))
            except MapException as ME:
                print(ME)
        else :
            button.append(tkinter.Button(row[i],state = DISABLED,relief = RAISED,fg ="blue", activeforeground = "blue" ,command = partial (racheta_AI,i,j,player,button,barcic), bg = "#324977",width = 2,height =1,highlightthickness=4,highlightbackground="#37d3ff"))
            comands.append(partial(racheta_AI, i, j, player, button,barcic))

        button[j].grid(row = i,column = j + 15)
    row2[i].grid(row=i + 2, column=11, columnspan=20)
print(barcip)
Game.mainloop()