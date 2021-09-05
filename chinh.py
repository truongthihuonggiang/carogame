from tkinter import *
from hcn import *
from banco import *
tk = Tk()
cas = Canvas (tk, height = 600, width = 800)
cas.pack()
banco = Banco()
banco.vehinh(cas)

#cas.create_rectangle(10,10,200,100,outline="black",fill="green")

# co = Co(40,40,80,80)
# co.giatri = -1
# co.vehinh(cas)


def callback_click(event):
     print ("clicked at", event.x, event.y     ) 
     banco.bamoco(cas,event.x,event.y)

# def dichchuyen(event):
#     h1.xoahinh(cas)
#     if event.keysym == "Up":
#         h1.dichlen()
#     elif event.keysym == "Down":
#         h1.dichxuong()
#     elif event.keysym == "Left":
#         h1.dichtrai()
#     elif event.keysym == "Right":
#         h1.dichphai()
#     h1.vehinh(cas)

# cas.bind_all('<KeyPress-Up>',dichchuyen)
# cas.bind_all('<KeyPress-Down>',dichchuyen)
# cas.bind_all('<KeyPress-Left>',dichchuyen)
# cas.bind_all('<KeyPress-Right>',dichchuyen)

cas.bind_all("<Button-1>", callback_click)
tk.mainloop()
