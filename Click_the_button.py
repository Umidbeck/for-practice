import tkinter as tk
import  random
import time

score = 0
start_time = time.time()
game_duration = 30

def click_button():
    global score
    score += 1
    label_score.config(text=f"Ball: {score}")
    move_button()

def move_button():
    x = random.randint(50, 300)
    y = random.randint(50, 300)
    button.place(x=x, y=y)

def update_timer():
    remaining_time = game_duration - int(time.time() - start_time)
    if remaining_time > 0:
        label_timer.config(text=f"Qolgan vaqt: {remaining_time}s")
        root.after(1000, update_timer)
    else:
        button.place_forget()
        label_timer.config(text="O'yin tugadi")

root = tk.Tk()
root.title("Button Click")
root.geometry("400x400")

label_score = tk.Label(root, text="Ball: 0", font=("Arial", 14))
label_score.pack()

label_timer = tk.Label(root,text="Qolgan vaqt: 30s", font=("Arial", 14),)
label_timer.pack()
button = tk.Button(root, text="Bos !", command=click_button, font=("Arial", 12))
button.place(x=150, y=150)

update_timer()
root.mainloop()