from tkinter import *
import winsound

root = Tk()
winsound.PlaySound("C:\\Users\\saisi\\OneDrive\\Desktop\\WISE_PROJECT\\bee_forest.wav",winsound.SND_ASYNC)
#winsound.PlaySound('bee_audio.wav',winsound.SND_ASYNC)
# Define a function to create a new window
def new_window():
    new_root = Toplevel()
    # Add widgets to the new window as desired
    # ...

# Define a function to quit the application
def quit_app():
    root.destroy()

# Load the background image
bg_img = PhotoImage(file="C:\\Users\\saisi\\OneDrive\\Desktop\\WISE_PROJECT\\page_1_bg.png")

# Create a label to display the background image
bg_label = Label(root, image=bg_img)
bg_label.pack()

# Load the image for the button
#button_img = PhotoImage(file="C:\\Users\\saisi\\OneDrive\\Desktop\\wise project\\bee3_image.png")
button_img1 = PhotoImage(file="C:\\Users\\saisi\\OneDrive\\Desktop\\WISE_PROJECT\\abc.png")
#button_img2 = PhotoImage(file="exit.jpeg")

# Create the button with the image
#button = Button(root, image=button_img)
#button2 = Button(root, image=button_img2, command=new_window)  # Call the new_window function when this button is clicked
button1 = Button(root, image=button_img1, command=quit_app)  # Call the quit_app function when this button is clicked

# Place the button on the background image
#button.place(x=1015, y=600)
button1.place(x=550, y=290)
#button2.place(x=750, y=450)

root.mainloop()


#import bee_complete
import tkinter as tk
import turtle
import random
from random import randint
import turtle
from time import sleep
# from tk import *
from _tkinter import *
import winsound 
#import winsound



tur=turtle.Screen()
#playsound('bee_audio.mp3')
screen=tur.getcanvas().winfo_toplevel()
#winsound.PlaySound('bee_audio.wav',winsound.SND_ASYNC)
#def play():



tur.bgpic("C:\\Users\\saisi\\OneDrive\\Desktop\\WISE_PROJECT\\Untitled.gif")
screen.attributes("-fullscreen",True)

winsound.PlaySound("C:\\Users\\saisi\\OneDrive\\Desktop\\WISE_PROJECT\\cocomelon.wav",winsound.SND_ASYNC)
n1 = int(turtle.textinput("Cell Details","Enter the first cell no: "))#int(input("Enter the first cell no: "))

turtle.tracer(1)

winsound.PlaySound("C:\\Users\\saisi\\OneDrive\\Desktop\\WISE_PROJECT\\cocomelon.wav",winsound.SND_ASYNC)
n2 = int(turtle.textinput("Cell Details","Enter the second cell no: "))#int(input("Enter the second cell no: "))


if n1 > n2:
    n1, n2 = n2, n1

n1x, n1y, n2x, n2y, x, y, k = 0, 0, 0, 0, 0, 0, 1


for i in range(1, n2):
    y -= 2
    k += 1
    if k == n1:
        n1x, n1y = x, y
    if k == n2:
        n2x, n2y = x, y
    for j in range(i - 1):
        x -= 1
        y -= 1
        k += 1
        if k == n1:
            n1x, n1y = x, y
        if k == n2:
            n2x, n2y = x, y
    for j in range(i):
        x -= 1
        y += 1
        k += 1
        if k == n1:
            n1x, n1y = x, y
        if k == n2:
            n2x, n2y = x, y
    for j in range(i):
        y += 2
        k += 1
        if k == n1:
            n1x, n1y = x, y
        if k == n2:
            n2x, n2y = x, y
    for j in range(i):
        x += 1
        y += 1
        k += 1
        if k == n1:
            n1x, n1y = x, y
        if k == n2:
            n2x, n2y = x, y
    for j in range(i):
        x += 1
        y -= 1
        k += 1
        if k == n1:
            n1x, n1y = x, y
        if k == n2:
            n2x, n2y = x, y
    for j in range(i):
        y -= 2
        k += 1
        if k == n1:
            n1x, n1y = x, y
        if k == n2:
            n2x, n2y = x, y

#print(n1)#, n1x, n1y)
#print(n2)#, n2x, n2y)

a = abs(n1x - n2x)
b = abs(n1y - n2y)
c = 0

while a > 0 or b > 0:
    if b > a:
        b -= 2
    else:
        a -= 1
        b -= 1

    c += 1
print(c)
t= turtle.Turtle()

t.hideturtle()

t.penup()
t.goto(150,10)
winsound.PlaySound("C:\\Users\\saisi\\OneDrive\\Desktop\\WISE_PROJECT\\abstract.wav",winsound.SND_ASYNC)
t.write(f"The distance between the two cells is {c}",align='center',font=('Times New Roman',45,'bold'))
#int(turtle.textinput("Output Dialog","The distance between the two cells is "))
#tur.write(c,align="center",font=('Times New Roman',12,'bold')

sleep(5)
tur.clear()

def next_screen(x,y):
    
    #tur.bgpic("next_screen.gif")
    button.hideturtle()
    #button.bgcolor("yellow")

button = turtle.Turtle()
turtle.Screen().bgcolor('bisque1')
button.hideturtle()
button.penup()
button.goto(0,-300)
#button.write("NEXT",align="center",font=("Arial",12,'bold'))


turtle.onscreenclick(next_screen)
#import visual2
#t.bye()



#t.bye()
#turtle.mainloop()turtle_1=turtle.RawTurtle(canvas)

#root=tk.Tk()
#root.title("Hexagons")
#canvas=turtle.Canvas(root,width=800,height=600)
#canvas.pack()


import tkinter as tk
import turtle
import random
from random import randint
import turtle
from time import sleep
# from tk import *
from _tkinter import *
#from playsound import playsound
import winsound

winsound.PlaySound("C:\\Users\\saisi\\OneDrive\\Desktop\\WISE_PROJECT\\bee_sound.wav",winsound.SND_ASYNC)
turtle.Screen().setup(width=0.5,height=0.75)
size = 30
circles = 100
#playsound('bee_audio.mp3')
turtle.speed('fastest')

turtle.colormode(255)

def move(length, angle):
                turtle.right(angle)
                turtle.forward(length)
#num=1

def hex(num):
        turtle.pendown()
        turtle.color( randint(0,255),randint(0,255),randint(0,255) )
        turtle.begin_fill()
        for i in range(6):
                move(size,-60)
        turtle.end_fill()
        turtle.penup()
        turtle.color('white')
        turtle.write(num,align="center",font=('Times New Roman',12,'bold'))
        
# start
turtle.penup()
num=1

for circle in range (circles):
        if circle == 0:
                hex(num)
                num +=1
                move(size,-60)
                move(size,-60)
                move(size,-60)
                move(0,180)
        for i in range (6):
                move(0,60)
                for j in range (circle+1):
                        hex(num)
                        num=num+1
                        move(size,-60)
                        move(size,60)
                move(-size,0)
        move(-size,60)
        move(size,-120)
        move(0,60)
turtle.exitonclick()