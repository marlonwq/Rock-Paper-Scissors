import tkinter
from tkinter import *
from tkinter import ttk

# cores --------------------------------
co0 = "#FFFFFF"  # white / branca
co1 = "#333333"  # black / preta
co2 = "#fcc058"  # orange / laranja
co3 = "#fff873"  # yellow / amarela
co4 = "#34eb3d"   # green / verde
co5 = "#e85151"   # red / vermelha

bottom = "#3b3b3b"

janela = Tk()
janela.title("")
janela.geometry('260x280')
janela.configure(bg=bottom)

frame_cima = Frame(janela, width=260, height=100, bg=co1, relief='raised')
frame_cima.grid(row = 0, column =0, sticky = NW)

frame_baixo = Frame(janela, width=260, height=300, bg=co0, relief='flat')
frame_baixo.grid(row = 1, column =0, sticky = NW)

style = ttk.Style(janela)
style.theme_use('clam')

janela.mainloop()