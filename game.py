from tkinter import *
import random

#Hello there im Manuja A.K.A anonixli --im creating this using python

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50 #HELLO IM JUST ASSUMING THIS IS 50 FOR NOW
SPACE_SIZE = 50
BODY_PART_START = 3
SNAKE_COLOR = "#00f5c0" #   this is for my first version
FOOD_COLOR = "#FF0000" # RED FOR FOOD 
BG_COLOR = "#000000" #BLACK hmm... yh ig mybe ill create a light version as well... 0w0



class Snake:
    pass

class Food:
    pass

def next_turn():
    pass

def change_direct(new_direct):
    pass

def check_collisions():
    pass

def game_over():
    pass


window = Tk()
window.title("Annix Snake game")
window.resizable(False,False)

score = 0
direction = 'down'

label = Label(window, text="Score : {}".format(score), font=('Poppins', 20)) # so i know this might seems a lot but its just myself adding a text and a font-fam
label.pack() #pack is basically displaying

canvas = Canvas(window, bg=BG_COLOR, height= GAME_HEIGHT , width = GAME_WIDTH)
canvas.pack()


window.mainloop()
