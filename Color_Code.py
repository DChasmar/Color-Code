# ColorCode

import tkinter as tk
import random

GAME_WIDTH = 400
GAME_HEIGHT = 600
BG = "#f6f6f6"
COLORS = ["#e52e19", "#ec8848", "#eae156", "#259462", "#136ae5", "#8871ea"]
INPUTS = ['r','o','y','g','b','p']
COLOR_OUTCOMES = ['black', 'white']
OUTCOMES = ['keep', 'move']

class Game(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.master.title("Color Code")
        self.master.geometry(f"{GAME_WIDTH}x{GAME_HEIGHT}")
        #self.master.resizable(False, False)

        self.main_canvas = tk.Canvas(bg = BG, width=GAME_WIDTH, height=GAME_HEIGHT)
        #self.main_canvas.configure(highlightthickness=0, borderwidth=0)
        self.main_canvas.pack(fill="both", side="right",expand=True)

        self.guess_number = 0
        self.score = 0
        self.game_over = False
        self.u = ["black", "black", "black", "black"]
        self.wins = 0
        self.losses = 0
        self.helpful = False
        
        for i in range(10):
            for j in range(4):
                self.main_canvas.create_oval(110 + 40*j, 100+ 40*i, 140 + 40*j, 130 + 40*i, 
                                             outline = "black", fill = "white", width = 2, tag=f'c_{j+(4*i)}')

        self.main_canvas.create_text(185, 520, text = "You Win!", font = ('Arial', 40), fill='black', justify = "center", state='hidden', tag='you_win')
        self.main_canvas.create_text(185, 520, text = "Game Over.", font = ('Arial', 40), fill='black', justify = "center", state='hidden', tag='game_over')

        self.main_canvas.create_text(300, 40, text = f'Wins: {self.wins}', font = ('Arial', 20), fill='black', anchor = "w", tag='wins')
        self.main_canvas.create_text(300, 65, text = f'Losses: {self.losses}', font = ('Arial', 20), fill='black', anchor = "w", tag='losses')

        self.main_canvas.create_oval(20, 30, 60, 70, outline = "black", fill = BG, width = 1, tag = "help")
        self.main_canvas.create_text(40, 50, text = '?', font = ('Arial', 25), fill='black', tag='?')

        self.main_canvas.create_polygon(40, 72, 48, 80, 90, 80, 90, 420, 10, 420, 10, 80, 32, 80, 40, 72, 
                                        fill=BG, width=2, outline='black', state='hidden', tag='info_polygon')
        for i in range(6):
            self.main_canvas.create_oval(50, 90 + 40*i, 80, 120 + 40*i, width=1, outline='black', fill=COLORS[i], state = 'hidden', tag=f'colorinfo_{i}')
            self.main_canvas.create_text(30, 105 + 40*i, text=f'{INPUTS[i]} =', state = 'hidden', font= ('Arial', 20), tag=f'textinfo_{i}')
        
        for i in range(2):
            self.main_canvas.create_oval(18, 348 + 40*i, 28, 358 + 40*i, width=1, outline='black', fill=COLOR_OUTCOMES[i], state = 'hidden', tag=f'coloroutcomes_{i}')
            self.main_canvas.create_text(60, 350 + 40*i, text=f'{OUTCOMES[i]}', state = 'hidden', font= ('Arial', 20), tag=f'textoutcomes_{i}')

        self.master.bind('<r>', lambda event: self.letter_pressed('r'))
        self.master.bind('<o>', lambda event: self.letter_pressed('o'))
        self.master.bind('<y>', lambda event: self.letter_pressed('y'))
        self.master.bind('<g>', lambda event: self.letter_pressed('g'))
        self.master.bind('<b>', lambda event: self.letter_pressed('b'))
        self.master.bind('<p>', lambda event: self.letter_pressed('p'))

        self.master.bind('<BackSpace>', lambda event: self.backspace())
        self.main_canvas.tag_bind('?', '<ButtonPress-1>', self.help)
        self.main_canvas.tag_bind('help', '<ButtonPress-1>', self.help)

        (self.c1, self.c2, self.c3, self.c4) = self.random_color()

        self.mainloop()

    def random_color(self):

        c1 = random.choice(COLORS)
        c2 = random.choice(COLORS)
        c3 = random.choice(COLORS)
        c4 = random.choice(COLORS)
        self.main_canvas.create_oval(110, 40, 140, 70, outline = "black", fill = c1, width = 2)
        self.main_canvas.create_oval(150, 40, 180, 70, outline = "black", fill = c2, width = 2)
        self.main_canvas.create_oval(190, 40, 220, 70, outline = "black", fill = c3, width = 2)
        self.main_canvas.create_oval(230, 40, 260, 70, outline = "black", fill = c4, width = 2)

        self.main_canvas.create_rectangle(100, 35, 270, 75, outline = "black", fill = BG, width = 2, tag = "rect")
        self.main_canvas.create_text(185, 55, text = "Color Code", font = ('Arial', 22), justify = "center", tag = "mast")

        c = [c1, c2, c3, c4]

        return c

    def check_guess(self, u):
        g1 = False
        g2 = False
        g3 = False
        g4 = False
        if self.score < 10:
            correct = 0
            wrong_place = 0
            if self.c1 == u[0]:
                correct = correct + 1
            elif self.c1 == u[1] != self.c2:
                wrong_place = wrong_place + 1
                g2 = True
            elif self.c1 == u[2] != self.c3:
                wrong_place = wrong_place + 1
                g3 = True
            elif self.c1 == u[3] != self.c4:
                wrong_place = wrong_place + 1
                g4 = True
            if self.c2 == u[1]:
                correct = correct + 1
            elif self.c2 == u[0] != self.c1:
                wrong_place = wrong_place + 1
                g1 = True
            elif self.c2 == u[2] != self.c3 and g3 == False:
                wrong_place = wrong_place + 1
                g3 = True
            elif self.c2 == u[3] != self.c4 and g4 == False:
                wrong_place = wrong_place + 1
                g4 = True
            if self.c3 == u[2]:
                correct = correct + 1
            elif self.c3 == u[0] != self.c1 and g1 == False:
                wrong_place = wrong_place + 1
                g1 = True
            elif self.c3 == u[1] != self.c2 and g2 == False:
                wrong_place = wrong_place + 1
                g2 = True
            elif self.c3 == u[3] != self.c4 and g4 == False:
                wrong_place = wrong_place + 1
                g4 = True
            if self.c4 == u[3]:
                correct = correct + 1
            elif self.c4 == u[0] != self.c1 and g1 == False:
                wrong_place = wrong_place + 1
            elif self.c4 == u[1] != self.c2 and g2 == False:
                wrong_place = wrong_place + 1
            elif self.c4 == u[2] != self.c3 and g3 == False:
                wrong_place = wrong_place + 1
            for i in range(correct):
                self.main_canvas.create_oval((300 + 20*i), (110 + self.score * 40), (310 + 20*i), (120 + self.score * 40), 
                                             outline = "black", fill = "black", width =1, tag='keep')
            for j in range(wrong_place):
                self.main_canvas.create_oval((300 + 20*(j + correct)), (110 + self.score * 40), (310 + 20*(j + correct)), (120 + self.score * 40), 
                                             outline = "black", fill = "white", width =1, tag='move')
            self.score += 1
            if correct == 4:
                self.main_canvas.delete("rect")
                self.main_canvas.delete("mast")
                self.main_canvas.itemconfig('you_win', state='normal')
                self.wins += 1
                self.main_canvas.itemconfig('wins', text = f'Wins: {self.wins}')
                self.game_over = True
            elif self.score == 10:
                self.main_canvas.delete("rect")
                self.main_canvas.delete("mast")
                self.main_canvas.itemconfig('game_over', state='normal')
                self.losses += 1
                self.main_canvas.itemconfig('losses', text = f'Losses: {self.losses}')
                self.game_over = True

    def choose_color(self, new_color):
        if new_color == 'r':
            self.main_canvas.itemconfig(f'c_{self.guess_number}', fill = '#e52e19')
            self.u[self.guess_number % 4] = "#e52e19"
        if new_color == 'o':
            self.main_canvas.itemconfig(f'c_{self.guess_number}', fill = '#ec8848')
            self.u[self.guess_number % 4] = "#ec8848"
        if new_color == 'y':
            self.main_canvas.itemconfig(f'c_{self.guess_number}', fill = '#eae156')
            self.u[self.guess_number % 4] = "#eae156"
        if new_color == 'g':
            self.main_canvas.itemconfig(f'c_{self.guess_number}', fill = '#259462')
            self.u[self.guess_number % 4] = "#259462"
        if new_color == 'b':
            self.main_canvas.itemconfig(f'c_{self.guess_number}', fill = '#136ae5')
            self.u[self.guess_number % 4] = "#136ae5"
        if new_color == 'p':
            self.main_canvas.itemconfig(f'c_{self.guess_number}', fill = '#8871ea')
            self.u[self.guess_number % 4] = "#8871ea"
        self.guess_number += 1
        if self.guess_number % 4 == 0 and self.guess_number > 0:
            self.check_guess(self.u)
        return self.guess_number

    def reset_game(self):
        for i in range(40):
            self.main_canvas.itemconfig(f'c_{i}', fill = 'white')
        self.game_over = False
        (self.c1, self.c2, self.c3, self.c4) = self.random_color()
    
    def letter_pressed(self, e):
        if e in INPUTS and self.game_over == False:
            self.choose_color(e)
        elif e in INPUTS and self.game_over == True:
            for i in range(40):
                self.main_canvas.itemconfig(f'c_{i}', fill = 'white')
            self.main_canvas.delete('keep')
            self.main_canvas.delete('move')
            self.main_canvas.itemconfig('you_win', state='hidden')
            self.main_canvas.itemconfig('game_over', state='hidden')
            self.game_over = False
            self.guess_number = 0
            self.score = 0
            self.u = ["black", "black", "black", "black"]
            (self.c1, self.c2, self.c3, self.c4) = self.random_color()
    def backspace(self):
        if self.guess_number % 4 != 0:
            self.guess_number -= 1
            self.main_canvas.itemconfig(f'c_{self.guess_number}', fill = 'white')
    
    def help(self, event):
        if self.helpful == False:
            self.main_canvas.itemconfig('info_polygon', state='normal')
            for i in range(6):
                self.main_canvas.itemconfig(f'colorinfo_{i}', state='normal')
                self.main_canvas.itemconfig(f'textinfo_{i}', state='normal')
            for i in range(2):
                self.main_canvas.itemconfig(f'coloroutcomes_{i}', state='normal')
                self.main_canvas.itemconfig(f'textoutcomes_{i}', state='normal')
            self.helpful = True
        elif self.helpful == True:
            self.main_canvas.itemconfig('info_polygon', state='hidden')
            for i in range(6):
                self.main_canvas.itemconfig(f'colorinfo_{i}', state='hidden')
                self.main_canvas.itemconfig(f'textinfo_{i}', state='hidden')
            for i in range(2):
                self.main_canvas.itemconfig(f'coloroutcomes_{i}', state='hidden')
                self.main_canvas.itemconfig(f'textoutcomes_{i}', state='hidden')
            self.helpful = False
        
def main():
    Game()

if __name__ == "__main__":
    main()