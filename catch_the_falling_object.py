import tkinter as tk
import random

WIDTH = 400
HEIGHT = 500

class CatchGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Catch The Falling Object")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='lightblue')
        self.canvas.pack()

        self.score = 0
        self.lives = 3

        self.box = self.canvas.create_rectangle(170, 460, 230, 489, fill='blue')

        self.object = self.canvas.create_oval(0, 0, 30,30, fill='red')
        self.reset_object()

        self.label = tk.Label(root, text = f"Score: {self.score} Hayot: {self.lives}", font=("Arial", 14))
        self.label.pack()

        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)

        self.update()

    def reset_object(self):
        x = random.randint(20, WIDTH - 40)
        self.canvas.coords(self.object, x, 0, x + 30, 30)

    def move_left(self, event):
        self.canvas.move(self.box, -20, 0)

    def move_right(self, event):
        self.canvas.move(self.box, 20, 0)

    def update(self ):
        self.canvas.move(self.object, 0, 5)
        obj_coords = self.canvas.coords(self.object)
        box_coords = self.canvas.coords(self.box)

        if self.check_collision(obj_coords, box_coords):
            self.score += 1
            self.reset_object()

        elif obj_coords[3] >=HEIGHT:
            self.lives -= 1
            self.reset_object()

        self.label.config(text = f"Ball: {self.score} Hayot: {self.lives}")

        if self.lives > 0:
            self.root.after(15, self.update)
        else:
            self.label.config(text = "O‘yin tugadi! ❌")
            self.canvas.create_text(WIDTH/2, HEIGHT/2, text="Game Over", fill = 'red', font=("Arial", 24))

    def check_collision(self, obj, box):
        return (
                obj[2] > box[0] and
                obj[0] < box[2] and
                obj[3] >= box[1] and
                obj[1] <= box[3]
        )

root = tk.Tk()
game = CatchGame(root)
root.mainloop()
