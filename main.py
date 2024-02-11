"""
This module contains the main code for the Rock-Paper-Scissors game.
"""

# Importing Libraries
from tkinter import Tk, Frame, Label, ttk, NW, Button, CENTER
from PIL import ImageTk, Image

# cores --------------------------------
CO0 = "#FFFFFF"  # white / branca
CO1 = "#333333"  # black / preta
CO2 = "#fcc058"  # orange / laranja
CO3 = "#fff873"  # yellow / amarela
CO4 = "#34eb3d"  # green / verde
CO5 = "#e85151"  # red / vermelha
BOTTOM = "#3b3b3b"

# Config Windows
janela = Tk()
janela.title("")
janela.geometry('260x280')
janela.configure(bg=BOTTOM)

# Config Split windows

top_frame = Frame(janela, width=260, height=100, bg=CO1, relief='raised')
top_frame.grid(row=0, column=0, sticky=NW)

# colors --------------------------------
CO0 = "#FFFFFF"  # white / branca
CO1 = "#333333"  # black / preta
CO2 = "#fcc058"  # orange / laranja
CO3 = "#fff873"  # yellow / amarela
CO4 = "#34eb3d"   # green / verde
CO5 = "#e85151"   # red / vermelha
BOTTOM = "#3b3b3b"

# Config Windows
janela = Tk()
janela.title("")
janela.geometry('260x280')
janela.configure(bg=BOTTOM)

# Config Split windows
top_frame = Frame(janela, width=260, height=100, bg=CO1, relief='raised')
top_frame.grid(row=0, column=0, sticky=NW)

lower_frame = Frame(janela, width=260, height=300, bg=CO0, relief='flat')
lower_frame.grid(row=1, column=0, sticky=NW)

style = ttk.Style(janela)

style.theme_use('clam')

# Config User Frame
app_1 = Label(top_frame, text="You", height=1, anchor='center',
              font=('Ivy 10 bold'), bg=CO1, fg=CO0)
app_1.place(x=50, y=70)
app_line = Label(top_frame, text="", height=10, anchor='center',
                 font=('Ivy 10 bold'), bg=CO0, fg=CO0)
app_line.place(x=0, y=0)
app1_points = Label(top_frame, text="0", height=1,
                    anchor='center', font=('Ivy 30 bold'), bg=CO1, fg=CO0)
app1_points.place(x=50, y=20)

# Config  Division Frame
app_ = Label(top_frame, text=":", height=1,
             anchor='center', font=('Ivy 30 bold'), bg=CO1, fg=CO0)
app_.place(x=115, y=20)

# Config  Machine Frame
app2_points = Label(top_frame, text="0", height=1,
                    anchor='center', font=('Ivy 30 bold'), bg=CO1, fg=CO0)
app2_points.place(x=170, y=20)
app_2 = Label(top_frame, text="Pc", height=1, anchor='center',
              font=('Ivy 10 bold'), bg=CO1, fg=CO0)
app_2.place(x=173, y=70)
app_2ine = Label(top_frame, text="", height=10, anchor='center',
                 font=('Ivy 10 bold'), bg=CO0, fg=CO0)

# Config  Buttons
icon_1 = Image.open('image/HandRock.png')
icon_1 = icon_1.resize((50, 50), Image.Resampling.NEAREST)
icon_1 = ImageTk.PhotoImage(icon_1)

b_icon1 = Button(lower_frame, width=50, image=icon_1,
                 compound='CENTER', bg=CO0, fg=CO0, font=('Ivy 10 bold'), anchor='center', relief='flat')
b_icon1.place(x=15, y=60)

janela.mainloop()
