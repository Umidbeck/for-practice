import  tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("TicTacToe")

        self.board = [''] * 9
        self.current_player = 'X'

        self.buttons = []
        for i in range(9):
            button = tk.Button(root, text = '', width=10, height=3, font=('Arial', 20),
                               command=lambda i=i : self.button_click(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def button_click(self, index):
        if self.board[index] == '':
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)

            if self.check_winner():
                messagebox.showinfo("Winner!", self.current_player)
                self.reset_game()
            elif '' not in self.board:
             messagebox.showinfo("Draw!", self.current_player)

            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'


    def check_winner(self):
        win_conditions = [
            [0,1,2],
            [3,4,5],
            [6,7,8],
            [0,3,6],
            [1,4,7],
            [2,5,8],
            [0,4,8],
            [2,4,6]
        ]

        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != '':
                return True

        return False

    def reset_game(self):
        self.board = [''] * 9
        for button in self.buttons:
            button.config(text='')
        self.current_player = 'X'

if __name__ == '__main__':
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()