import tkinter as tk

# test click event
def on_click():
    print("Habit Tracked!")


root = tk.Tk()
root.geometry("500x500")
canvas = tk.Canvas(root, height=500, width=500)
canvas.grid(row=0, column=0)
canvas.create_rectangle(2,0,500,100,fill="lightblue") #position will change lol

root.title("Habit Tracker")
title = tk.Label(root, text="dini's habit tracker", font=("Arial", 10), bg="lightblue", fg="white")
welcome = tk.Label(root, text="welcome back!", font=("Arial", 10), bg="lightblue", fg="white")
title.place(x=200, y=20)
welcome.place(x=205, y=50)  
# btn = tk.Button(root, text="Track Habit", command=on_click)
# btn.grid(row=0, column=1)




root.mainloop()