habits = [] # list to store habits

import tkinter as tk
import random
import sqlite3

connection = sqlite3.connect('storage.db')

c = connection.cursor() 

c.execute 

y_pos = 110

# click event for add button
def on_click(add_habit, tk, canvas):
    global y_pos
    habit = add_habit.get()
    habits.append(habit)
    print(f"Habit Tracked!")
    canvas.create_text(50,y_pos+25, text=habit, font = ("Arial, 14"))
    create_habitcircles(canvas, y_pos)
    add_habit.delete(0, tk.END)
    y_pos += 80

# change colour of circle when clicked (to represent habit completion)
def on_circle_click(event, oval):
    canvas = event.widget
    clickeditem = canvas.find_withtag("current")[0]
    print(f"Clicked oval {clickeditem}")
    if canvas.itemcget(clickeditem, "fill") == "#CFFBCF": # if circle is already green (habit marked as done)
        canvas.itemconfig(clickeditem, fill = original_colours[clickeditem]) # revert to original colour stored in dictionary
    else:
        canvas.itemconfig(clickeditem, fill = "#CFFBCF") # change circle colour to green to indicate habit done

original_colours = {} # dictionary to store original colours of circles


# create 7 circles for each habit to represent days of the week
def create_habitcircles(canvas, y_pos):
    colour_gen = colour_generator()
    for i in range(7):
        new_colour = next(colour_gen)
        oval = canvas.create_oval(120 + i*100, y_pos, 170 + i*100, y_pos+50, fill = new_colour, width = 0)
        original_colours[oval] = new_colour # store original colour of circle in dictionary
        canvas.tag_bind(oval, "<Button-1>", lambda event, x=120 + i*70, y=y_pos: on_circle_click(event, oval)) # bind click event to each circle, passing original colour as argument
# random colour generator for circles for aesthetic purposes
def colour_generator():
    colours = ["#f6d4e3", "#4cb4f0", "#b0daec", "#d1ebf6", "#fefbba", "#ffffff"]
    while True:
        random.shuffle(colours)
        for colour in colours:
            yield colour # yield keyword allows function to return a value and later be resumed from where it left off- better memory usage


