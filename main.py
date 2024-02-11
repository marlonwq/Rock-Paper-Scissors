import tkinter
from tkinter import *
from tkinter import ttk

# import pillow
from PIL import Image

# cores --------------------------------
co0 = "#FFFFFF"  # white / branca
co1 = "#333333"  # black / preta
co2 = "#fcc058"  # orange / laranja
co3 = "#fff873"  # yellow / amarela
co4 = "#34eb3d"   # green / verde
co5 = "#e85151"   # red / vermelha
bottom = "#3b3b3b"

# Config Windows
janela = Tk()
janela.title("")
janela.geometry('260x280')
janela.configure(bg=bottom)

# Split windows

top_frame = Frame(janela, width=260, height=100, bg=co1, relief='raised')
top_frame.grid(row=0, column=0, sticky=NW)
lower_frame = Frame(janela, width=260, height=300, bg=co0, relief='flat')
lower_frame.grid(row=1, column=0, sticky=NW)

style = ttk.Style(janela)
style.theme_use('clam')

# User Frame
app_1 = Label(top_frame, text="You", height=1, anchor='center',
              font=('Ivy 10 bold'), bg=co1, fg=co0)
app_1.place(x=50, y=70)
app_line = Label(top_frame, text="", height=10, anchor='center',
                 font=('Ivy 10 bold'), bg=co0, fg=co0)
app_line.place(x=0, y=0)
app1_points = Label(top_frame, text="0", height=1,
                    anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app1_points.place(x=50, y=20)

# Division Frame
app_ = Label(top_frame, text=":", height=1,
             anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_.place(x=115, y=20)

# Machine Frame
app2_points = Label(top_frame, text="0", height=1,
                    anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app2_points.place(x=170, y=20)
app_2 = Label(top_frame, text="Pc", height=1, anchor='center',
              font=('Ivy 10 bold'), bg=co1, fg=co0)
app_2.place(x=173, y=70)
app_2ine = Label(top_frame, text="", height=10, anchor='center',
                 font=('Ivy 10 bold'), bg=co0, fg=co0)
app_2ine.place(x=255, y=0)

# Draw Line
app_ine = Label(top_frame, text="", width=255, anchor='center',
                font=('Ivy 1 bold'), bg=co4, fg=co0)
app_ine.place(x=0, y=95)

# Bottom Frame

janela.mainloop()
