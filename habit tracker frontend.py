import tkinter as tk
from habittrackerbackend import * 


root = tk.Tk()
root.geometry("500x500")
root.configure(bg="#8CCDD4")
canvas = tk.Canvas(root, height=500, width=500,highlightthickness=0,)
canvas.configure(bg= "#8CCDD4")
canvas.grid(row=0, column=0, sticky="nsew")
canvas.create_rectangle(2,0,500,100,fill="#4CB5E8",) #position will change lol

root.title("Habit Tracker")
title = tk.Label(root, text="dini's habit tracker", font=("Arial", 10), bg="lightblue", fg="white")
welcome = tk.Label(root, text="welcome back!", font=("Arial", 10), bg="lightblue", fg="white")
title.place(x=200, y=20)
welcome.place(x=205, y=50)  

add_habit = tk.Entry(root, font=("Arial", 10), bg="white", fg="black")
add_habit.place(x=200, y=130)

btn = tk.Button(root, text="Add", command=lambda:on_click(add_habit, tk))
btn.place(x=200, y=200)




root.mainloop()