import math
import turtle
import pygame  
from tkinter import Tk, Label


pygame.mixer.init()


pygame.mixer.music.load('bday_present_for_danyel\heart\song_for_u.mp3')  
pygame.mixer.music.play(-1)  

def heart_a(theta_var):
    return 15 * math.sin(theta_var)**3

def heart_b(theta_var):
    return 12 * math.cos(theta_var) - 5 * \
           math.cos(2 * theta_var) - 2 * \
           math.cos(3 * theta_var) - \
           math.cos(4 * theta_var)


screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)


t.color("red")
t.begin_fill()  
for i in range(6000):
    t.goto(heart_a(i) * 20, heart_b(i) * 20)
t.end_fill()  


t.penup()
t.goto(0, -20)  
t.pendown()


t.hideturtle() 


root = Tk()
root.title("Heart with Text")


label = Label(root, text="I love you", fg="white", bg="black", font=("Arial", 24, "bold"))
label.pack(pady=20) 

def close_window():
    pygame.mixer.music.stop()  
    turtle.bye() 
    root.destroy()  

root.protocol("WM_DELETE_WINDOW", close_window) 

root.mainloop()
