from tkinter import Tk, Frame, Label, Button, NW
from PIL import Image, ImageTk

<<<<<<< Updated upstream

class Screen:
    def __init__(self):
        # Constants
        self.FONT_NAME = 'Ivy'
        self.FONT_SIZE_SMALL = 10
        self.FONT_SIZE_LARGE = 30
=======
# Importing Libraries
from tkinter import Tk, Frame, Label, ttk, NW, Button
from PIL import Image
from PIL import ImageTk

# colors
CO0 = "#FFFFFF"  # white / branca
CO1 = "#333333"  # black / preta
CO2 = "#fcc058"  # orange / laranja
CO3 = "#fff873"  # yellow / amarela
CO4 = "#34eb3d"  # green / verde
CO5 = "#e85151"  # red / vermelha
BOTTOM = "#3b3b3b"
>>>>>>> Stashed changes

        # Colors
        self.WHITE = "#FFFFFF"
        self.BLACK = "#333333"
        self.BOTTOM = "#3b3b3b"

<<<<<<< Updated upstream
        # Config Windows
        self.janela = Tk()
        self.janela.title("")
        self.janela.geometry('260x280')
        self.janela.configure(bg=self.BOTTOM)

        # Top Frame
        self.top_frame = Frame(self.janela, width=260,
                               height=100, bg=self.BLACK, relief='raised')
        self.top_frame.grid(row=0, column=0, sticky=NW)

        # Labels and Points for User
        self.user_label_text = "You"
        self.user_label = Label(self.top_frame, text=self.user_label_text, height=1, anchor='center',
                                font=(self.FONT_NAME, self.FONT_SIZE_SMALL, 'bold'), bg=self.BLACK, fg=self.WHITE)
        self.user_label.place(x=50, y=70)
        self.user_points_text = "0"
        self.user_points = Label(self.top_frame, text=self.user_points_text, height=1,
                                 anchor='center', font=(self.FONT_NAME, self.FONT_SIZE_LARGE, 'bold'), bg=self.BLACK, fg=self.WHITE)
        self.user_points.place(x=50, y=20)

        # Divider
        self.divider_text = ":"
        self.divider = Label(self.top_frame, text=self.divider_text, height=1,
                             anchor='center', font=(self.FONT_NAME, self.FONT_SIZE_LARGE, 'bold'), bg=self.BLACK, fg=self.WHITE)
        self.divider.place(x=115, y=20)

        # Labels and Points for Machine
        self.machine_points_text = "0"
        self.machine_points = Label(self.top_frame, text=self.machine_points_text, height=1,
                                    anchor='center', font=(self.FONT_NAME, self.FONT_SIZE_LARGE, 'bold'), bg=self.BLACK, fg=self.WHITE)
        self.machine_points.place(x=170, y=20)
        self.machine_label_text = "Pc"
        self.machine_label = Label(self.top_frame, text=self.machine_label_text, height=1, anchor='center',
                                   font=(self.FONT_NAME, self.FONT_SIZE_SMALL, 'bold'), bg=self.BLACK, fg=self.WHITE)
        self.machine_label.place(x=173, y=70)
=======
# Config Split windows
top_frame = Frame(janela, width=260, height=100, bg=CO1, relief='raised')
top_frame.grid(row=0, column=0, sticky=NW)
>>>>>>> Stashed changes

        # Lower Frame
        self.lower_frame = Frame(
            self.janela, width=260, height=300, bg=self.WHITE, relief='flat')
        self.lower_frame.grid(row=1, column=0, sticky=NW)

        # Rock Button
        self.rock_icon = Image.open('image/HandRock.png')
        self.rock_icon = self.rock_icon.resize((50, 50), Image.NEAREST)
        self.rock_img = ImageTk.PhotoImage(self.rock_icon)
        self.rock_button = Button(self.lower_frame, width=50, height=10, image=self.rock_img, compound='center',
                                  bg=self.WHITE, fg=self.WHITE, font=(self.FONT_NAME, self.FONT_SIZE_SMALL, 'bold'), anchor='center', relief='flat')
        self.rock_button.grid(row=15, column=60)
        #ad

    def start(self):
        self.janela.mainloop()


class Game:
    def __init__(self):
        self.screen = Screen()

<<<<<<< Updated upstream
    def start(self):
        self.screen.start()


game = Game()
game.start()
=======
# Config  Machine Frame
app2_points = Label(top_frame, text="0", height=1,
                    anchor='center', font=('Ivy 30 bold'), bg=CO1, fg=CO0)
app2_points.place(x=170, y=20)
app_2 = Label(top_frame, text="Pc", height=1, anchor='center',
              font=('Ivy 10 bold'), bg=CO1, fg=CO0)
app_2.place(x=173, y=70)
app_2ine = Label(top_frame, text="", height=10, anchor='center',
                 font=('Ivy 10 bold'), bg=CO1, fg=CO0)
app_2line.place(x=0, y=0)

# Config  Buttons
icon_1 = Image.open('image/HandRock.png')
size = 128, 128
icon_1 = icon_1.resize(size, Image.Resampling.BOX)
icon_1 = ImageTk.PhotoImage(icon_1)
b_icon1 = Button(lower_frame, width=50, image=icon_1, compound='center',
                 bg=CO0, fg=CO0, font=('Ivy 10 bold'), anchor='center', relief='flat')

janela.mainloop()
>>>>>>> Stashed changes
