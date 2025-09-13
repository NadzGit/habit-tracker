habits = []

# test click event
def on_click(add_habit, tk):
    habit = add_habit.get()
    habits.append(habit)
    print(f"Habit Tracked!")
    for i in range(len(habits)):
        print(habits[i])
    add_habit.delete(0, tk.END)

