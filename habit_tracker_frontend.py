import tkinter as tk
from habit_tracker_backend import * 



root = tk.Tk()
root.geometry("1920x1080")
root.configure(background= "#8CCDD4")

# welcome rectangle widget
frame = tk.Frame(width = 885, height= 266, bg = "#4CB5E8")
frame.pack(side = "top")


root.title("Habit Tracker")
title = tk.Label(root, text="dini's habit tracker", font=("Arial", 10), bg = "#4CB5E8",fg="white")
welcome = tk.Label(frame, text="welcome back!", font=("Arial", 10),bg = "#4CB5E8",fg="white")
title.place(x=894, y=78)
welcome.place(x=385, y=118)  

# habit tracking space
canvas = tk.Canvas(root, width = 1096, height = 623)
canvas.place(x = 444, y = 378)
canvas.create_line(100,100,100, 600, fill = "#8CCDD4", width = 4)


add_habit = tk.Entry(root, font=("Arial", 10), bg="white", fg="black")
add_habit.place(x=600, y=163, width = 340, height = 54)

btn = tk.Button(root, text="Add", command=lambda:on_click(add_habit, tk, canvas))
btn.config(bg = "#F8DAE7")
btn.place(x=953, y=163, width = 340, height = 54)

# days of the week
text = canvas.create_text(145,80, text="M", font = ("Arial, 14"))
text = canvas.create_text(250,80, text="T", font = ("Arial, 14"))
text = canvas.create_text(350,80, text="W", font = ("Arial, 14"))
text = canvas.create_text(450,80, text="T", font = ("Arial, 14"))
text = canvas.create_text(545,80, text="F", font = ("Arial, 14"))
text = canvas.create_text(645,80, text="S", font = ("Arial, 14"))
text = canvas.create_text(740,80, text="S", font = ("Arial, 14"))


root.mainloop()