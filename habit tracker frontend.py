import tkinter as tk
from habittrackerbackend import * 


root = tk.Tk()
root.geometry("1920x1080")

# welcome rectangle widget
frame = tk.Frame(width = 885, height= 266, bg = "#4CB5E8")
frame.pack(side = "top")


root.title("Habit Tracker")
title = tk.Label(root, text="dini's habit tracker", font=("Arial", 10), bg = "#4CB5E8",fg="white")
welcome = tk.Label(frame, text="welcome back!", font=("Arial", 10),bg = "#4CB5E8",fg="white")
title.place(x=894, y=78)
welcome.place(x=385, y=118)  


add_habit = tk.Entry(root, font=("Arial", 10), bg="white", fg="black")
add_habit.place(x=600, y=163, width = 340, height = 54)

btn = tk.Button(root, text="Add", command=lambda:on_click(add_habit, tk))
btn.config(bg = "#F8DAE7")
btn.place(x=953, y=163, width = 340, height = 54)





root.mainloop()