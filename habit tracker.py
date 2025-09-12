import tkinter as tk

root = tk.Tk()
root.title("Habit Tracker")
label = tk.Label(root, text="Welcome to Habit Tracker")
label.grid(row=0, column=0)
btn = tk.Button(root, text="Track Habit")
btn.grid(row=0, column=1)


root.mainloop()