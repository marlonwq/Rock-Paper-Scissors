from tkinter import Tk, Frame, Label, Button, NW
from PIL import Image, ImageTk

class Screen:
    """
    This class represents the screen of the game.
    """

    FONT_NAME = 'Ivy'
    FONT_SIZE_SMALL = 10
    FONT_SIZE_LARGE = 30
    WHITE = "#FFFFFF"
    BLACK = "#333333"
    BOTTOM = "#3b3b3b"

    def __init__(self):
        self.janela = Tk()
        self.janela.title("")
        self.janela.geometry('260x280')
        self.janela.configure(bg=self.BOTTOM)

        self.top_frame = Frame(self.janela, width=260,
                               height=100, bg=self.BLACK, relief='raised')
        self.top_frame.grid(row=0, column=0, sticky=NW)

        self.user_label_text = "You"
        self.user_label = Label(
            self.top_frame, text=self.user_label_text, height=1, anchor='center',
            font=(self.FONT_NAME, self.FONT_SIZE_SMALL, 'bold'), bg=self.BLACK, fg=self.WHITE
        )
        self.user_label.place(x=50, y=70)

        self.user_points_text = "0"
        self.user_points = Label(
            self.top_frame, text=self.user_points_text, height=1,
            anchor='center', font=(self.FONT_NAME, self.FONT_SIZE_LARGE, 'bold'), bg=self.BLACK, fg=self.WHITE
        )
        self.user_points.place(x=50, y=20)

        self.divider_text = ":"
        self.divider = Label(
            self.top_frame, text=self.divider_text, height=1,
            anchor='center', font=(self.FONT_NAME, self.FONT_SIZE_LARGE, 'bold'), bg=self.BLACK, fg=self.WHITE
        )
        self.divider.place(x=115, y=20)

        self.machine_points_text = "0"
        self.machine_points = Label(
            self.top_frame, text=self.machine_points_text, height=1,
            anchor='center', font=(self.FONT_NAME, self.FONT_SIZE_LARGE, 'bold'), bg=self.BLACK, fg=self.WHITE
        )
        self.machine_points.place(x=170, y=20)

        self.machine_label_text = "Pc"
        self.machine_label = Label(
            self.top_frame, text=self.machine_label_text, height=1, anchor='center',
            font=(self.FONT_NAME, self.FONT_SIZE_SMALL, 'bold'), bg=self.BLACK, fg=self.WHITE
        )
        self.machine_label.place(x=173, y=70)

        top_frame = Frame(self.janela, width=260, height=100, bg=self.BLACK, relief='raised')
        top_frame.grid(row=0, column=0, sticky=NW)

        self.lower_frame = Frame(
            self.janela, width=260, height=300, bg=self.WHITE, relief='flat'
        )
        self.lower_frame.grid(row=1, column=0, sticky=NW)

        self.paper_icon = Image.open('image/HandPaper.png')
        self.rock_icon = Image.open('image/HandRock.png')
        self.rock_img = ImageTk.PhotoImage(self.rock_icon)
        self.rock_button = Button(
            self.lower_frame, width=50, height=10, image=self.rock_img, compound='center',
            bg=self.WHITE, fg=self.WHITE, font=(self.FONT_NAME, self.FONT_SIZE_SMALL, 'bold'),
            anchor='center', relief='flat'
        )
        self.rock_button.grid(row=15, column=60)

    def start(self):
        """
        Start the game.
        """
        self.janela.mainloop()


class Game:
    """
    This class represents the game.
    """

    def __init__(self):
        self.screen = Screen()

    def start(self):
        """
        Start the game.
        """
        self.screen.start()